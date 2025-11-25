import sqlite3

class Database:
    def __init__(self, db_nimi = ":memory:"):
        self.db_nimi = db_nimi
        self.conn = sqlite3.connect(self.db_nimi)
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
            year INTEGER NOT NULL
        )                    
        """)
        self.conn.commit()

    def insert_defaults(self):
        self.cursor.execute("""
        INSERT OR IGNORE INTO viitteet (viite, type, author, title, year) 
                            VALUES (
                            "VPL11", 
                            "inproceedings", 
                            "Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti",
                            "Extreme Apprenticeship Method in Teaching Programming for Beginners.",
                            2011)                
        """)
        self.conn.commit()

    def lisaa_viite(self, data: dict):
        self.cursor.execute("""
            INSERT INTO viitteet (viite, type, author, title, year)
                            VALUES (?, ?, ?, ?, ?)                 
        """, (data["viite"], data["type"], data["author"], data["title"], data["year"]))
        self.conn.commit()

    def hae_viite(self, viite):
        self.cursor.execute("""
        SELECT * FROM viitteet
        WHERE viite = ?
        """, (viite,))
        return self.cursor.fetchone()

