import sqlite3
from viite import Viite

class Database:
    def __init__(self, db_nimi = ":memory:"):
        self.viite_lisatty = "Viite lisätty!"
        self.lisaaminen_epaonnistui = "Lisääminen epäonnistui"
        self.db_nimi = db_nimi
        self.conn = sqlite3.connect(self.db_nimi,  check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        print("Yhdistetty tietokantaan: ", self.db_nimi)

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS viitteet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            viite TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            booktitle TEXT,
            journal TEXT,
            volume TEXT,
            pages TEXT,
            publisher TEXT                
        )                    
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kentat (
            viiteId TEXT NOT NULL,
            field TEXT NOT NULL,
            value TEXT NOT NULL,
            PRIMARY KEY (viiteId, field),
            FOREIGN KEY (viiteId) REFERENCES viitteet(id) ON DELETE CASCADE                    
        )                    
        """)

        self.conn.commit()

    def insert_defaults(self):
        self.cursor.execute("""
        INSERT OR IGNORE INTO viitteet (viite, type, author, title, year, booktitle) 
                            VALUES (
                            "VPL11", 
                            "inproceedings", 
                            "Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti",
                            "Extreme Apprenticeship Method in Teaching Programming for Beginners.",
                            2011,
                            "SIGCSE '11: Proceedings of the 42nd SIGCSE technical symposium on Computer science education")                
        """)

        self.cursor.execute("""
        INSERT OR IGNORE INTO viitteet (viite, type, author, title, year, publisher) 
                            VALUES (
                            "Martin09", 
                            "book", 
                            "Martin, Robert",
                            "Clean Code: A Handbook of Agile Software Craftsmanship",
                            2008,
                            "Prentice Hall")                
        """)
        self.cursor.execute("""
        INSERT OR IGNORE INTO viitteet (viite, type, author, title, year, journal, volume, pages) 
                            VALUES (
                            "CBH91", 
                            "article", 
                            "Allan Collins and John Seely Brown and Ann Holum",
                            "Cognitive apprenticeship: making thinking visible",
                            1991,
                            "American Educator",
                            "6",
                            "38--46")                
        """)
        self.cursor.execute("""
        INSERT OR IGNORE INTO kentat (viiteId, field, value) VALUES ("VPL11", "lisakentta", "lisäkenttä")                 
        """)
        self.conn.commit()

    def lisaa_viiteolio(self, viite: Viite):
        try:
            self.cursor.execute("""
            INSERT INTO viitteet (viite, type, author, title, year, booktitle, journal, volume, pages, publisher)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)                    
            """, (viite.viite, 
                viite.viitetyyppi, 
                viite.author, 
                viite.title, 
                viite.year, 
                viite.booktitle, 
                viite.journal,
                viite.volume,
                viite.pages,
                viite.publisher))
            
            if viite.lisakentat:
                for key, value in viite.lisakentat.items():
                    self.cursor.execute(
                    "INSERT INTO kentat (viiteId, field, value) VALUES (?, ?, ?)",
                    (viite.viite, key, str(value))
                    )

            self.conn.commit()
            return self.viite_lisatty
        except sqlite3.Error as e:
            return f"{self.lisaaminen_epaonnistui}: {e}"

    #tämä huomioi vain pakolliset kentät, käytä mieluummin lisaa_viiteolio
    def lisaa_viite(self, data: dict):
        try:
            self.cursor.execute("""
                INSERT INTO viitteet (viite, type, author, title, year)
                             VALUES (?, ?, ?, ?, ?)                 
         """, (data["viite"], data["type"], data["author"], data["title"], data["year"]))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print('epäonnistui')

    def hae_viite(self, viite):
        self.cursor.execute("""
        SELECT * FROM viitteet
        WHERE viite = ?
        """, (viite,))
        return self.cursor.fetchone()
    
    def lisaa_kentta(self, viite, kentta, arvo):
        self.cursor.execute("""
        INSERT INTO kentat (viiteId, field, value) VALUES (?, ?, ?)
        ON CONFLICT (viiteId, field) DO UPDATE SET value = excluded.value;                  
        """, (viite, kentta, arvo))
    
    def hae_lisakentat(self, viite):
        self.cursor.execute("""
        SELECT * FROM kentat
        WHERE viiteId = ?                    
        """, (viite,))
        return self.cursor.fetchall()

	# Hakee kaikki viitteet listaamista varten
    def hae_kaikki(self):
        self.cursor.execute("""
        SELECT * FROM viitteet
        """)
        return self.cursor.fetchall()

	# Poistaa yksittäisen viitteen sen viitetiedon avulla
    def poista_viite(self, viite):
        self.cursor.execute("""
        DELETE FROM viitteet
        WHERE viite = ?
        """, (viite,))
        self.conn.commit()