from viite import Viite

class ViiteRepo:
    def __init__(self, database):
        self.database = database

    # Hakee tietokannasta viitteellä ja palauttaa viiteolion tai tyhjän, jos ei löydy
    def hae_viitteella(self, viite):
        row = self.database.hae_viite(viite)
        if not row:
            return None
        viite = Viite(viite = row["viite"], 
                        viitetyyppi = row["type"], 
                        author = row["author"], 
                        title = row["title"], 
                        year = row["year"])
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

        # Jos mock-datasta tulee dict-lista, käytetään sellaisenaan
        if isinstance(rows[0], dict):
            kaikki = rows

        else:
            # Muunna tuple -> dict käyttäen cursor.descriptionia
            columns = [col[0] for col in self.database.cursor.description]
            kaikki = [dict(zip(columns, row)) for row in rows]

        tulokset = []

        for viite in kaikki:
            match = True

            for kentta, arvo in hakuehdot.items():

                data_arvo = viite.get(kentta)

                # Jos kenttä on None
                if data_arvo is None:
                    data_arvo = ""

                # Author-kentälle
                if kentta == "author":
                    if arvo not in viite[kentta].lower():
                        match = False
                        break
                
                # Muille useamman kuin yhden sanan kentille
                elif kentta in ("title", "booktitle", "publisher"):
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