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
        kaikki_viitteet = self.database.hae_kaikki()
        tulokset = []

        for viite in kaikki_viitteet:
            match = True
            for kentta, arvo in hakuehdot.items():
                if kentta not in viite or viite[kentta] != arvo:
                    match = False
                    break
            
            if match:
                tulokset.append(viite)
        
        return tulokset