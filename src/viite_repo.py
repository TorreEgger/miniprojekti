from viite import Viite

class ViiteRepo:
    def __init__(self, database):
        self.database = database

    # Hakee tietokannasta viitteellä ja palauttaa viiteolion tai tyhjän, jos ei löydy
    def hae_viitteella(self, viite):
        row = self.database.hae_viite(viite)
        if not row:
            return None
        
        rivit = self.database.hae_lisakentat(viite)
        kentat = {}
        for rivi in rivit:
            kentat[rivi["field"]] = rivi["value"]

        viite = Viite(viite = row["viite"], 
                        viitetyyppi = row["type"], 
                        author = row["author"], 
                        title = row["title"], 
                        year = row["year"],
                        booktitle = row["booktitle"],
                        journal = row["journal"],
                        pages = row["pages"],
                        volume = row["volume"],
                        publisher = row["publisher"],
                        lisakentat = kentat)
        
        return viite
    
    # Palauttaa viitteen nimeä vastaavan viitteen databasesta
    def hae_viite(self, viite):
        tulos = self.database.hae_viite(viite)
        if not tulos:
            return None
        
        return tulos

    # Palauttaa hakuehtoja vastaavat viitteet databasesta
    def hae_viite_hakuehdoilla(self, **hakuehdot):
        rows = self.database.hae_kaikki()

        if not rows:
            return []

        # Jos mock-datasta tulee dict-lista, käytetään sellaisenaan
        if isinstance(rows[0], dict):
            kaikki = rows
        else:
            # Muunna tuple -> dict käyttäen cursor.descriptionia
            columns = [col[0] for col in self.database.cursor.description]
            kaikki = [dict(zip(columns, row)) for row in rows]

        # Haetaan lisäkenttien tiedot ja muunnetaan ne dict muotoisiksi hakuehdoiksi
        for viite in kaikki:
            viite_id = viite.get("viite")
            lisarivit = self.database.hae_lisakentat(viite_id)

            if not isinstance(lisarivit, (list, tuple)):
                lisarivit = []

            for rivi in lisarivit:
                if len(rivi) >= 3:
                    field = rivi[1]
                    value = rivi[2]
                    viite[field] = value

        tulokset = []

        for viite in kaikki:
            match = True

            for kentta, arvo in hakuehdot.items():

                data_arvo = viite.get(kentta)

                # Jos kenttä on None
                if data_arvo is None:
                    data_arvo = ""
                    match = False
                    break

                # Author-kentälle
                if kentta == "author":
                    if arvo not in viite[kentta].lower():
                        match = False
                        break
                
                # Muille useamman kuin yhden sanan kentille. Yksi merkkijonoon sisältyvä sana riittää myös.
                elif kentta in ("title", "booktitle", "publisher", "journal", "pages"):
                    if arvo.lower() not in data_arvo.lower():
                        match = False
                        break

                # Loput (yhden sanan) kentät
                else:
                    if str(viite[kentta]) != str(arvo):
                        match = False
                        break
                    
            if match:
                tulokset.append(viite)
        
        return tulokset
    

    def poista_viite(self, viite):

        #testataan ekaksi, että poistettava viite on olemassa
        haku = self.database.hae_viite(viite)
        if haku is None:
            return 'ei löytynyt' 
        
        # jos viite löytyy tietokannasta, tehdään sen poistaminen
        self.database.poista_viite(viite)
        return'viite poistettu'
    

    def lisaa_viiteolio(self, viite: Viite):
        response = self.database.lisaa_viiteolio(viite)
        return response

    def lisaa_viite(self, viite: Viite):

        viitetiedot = {
            "viite": viite.viite,
            "type": viite.viitetyyppi,
            "author": viite.author,
            "title": viite.title,
            "year": viite.year,
            "booktitle": viite.booktitle,
            "journal":  viite.journal,
            "volume": viite.volume,
            "pages": viite.pages,
            "publisher": viite.publisher
        }

        self.database.lisaa_viite(viitetiedot)

        #testataan, että lisäys onnistuu
        lisattu_viite = self.database.hae_viite(viitetiedot["viite"])

        if lisattu_viite is None:
            return 'lisäys ei onnistunut'
        return 'lisäys onnistui'

    def listaa_kaikki(self):
        tulokset = self.database.hae_kaikki()
        if not tulokset:
            return "Tietokanta on tyhjä\n"
        
        rivit = []
        rivit.append("Hakutulokset:\n")

        for viite in tulokset:
            #rivit.append(f"ID: {viite['id']}")
            rivit.append(f"viite: {viite['viite']}")
            rivit.append(f"type: {viite['type']}")
            rivit.append(f"author: {viite['author']}")
            rivit.append(f"title: {viite['title']}")
            rivit.append(f"year: {viite['year']}")

            # Valinnaiset kentät:
            valinnaiset = ["booktitle", "journal", "volume", "pages", "publisher"]
            for k in valinnaiset:
                if viite[k]:
                    rivit.append(f"{k.capitalize()}: {viite[k]}")
            
            lisakentat = self.database.hae_lisakentat(viite['viite'])

            for row in lisakentat:
                field = row["field"]
                value = row["value"]
                rivit.append(f"{field.capitalize()}: {value}")
            
            
            rivit.append("")
        
        return "\n".join(rivit)
    
    def listaa_kaikki_bibtex(self):
        tulokset = self.database.hae_kaikki()

        if not tulokset:
            return "Tietokanta on tyhjä\n"

        rivit = []
        rivit.append("Hakutulokset BibTeX-muodossa:\n")

        for viite in tulokset:
            viitetunnus = self.hae_viitteella(viite['viite'])
            rivit.append(viitetunnus.to_bibtex())
            rivit.append("")
            
        return "\n".join(rivit)