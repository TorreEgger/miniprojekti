from viite import Viite
from database import Database

class ViiteRepo:
    def __init__(self, database):
        self.database = database

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