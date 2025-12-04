from database import Database
from viite_repo import ViiteRepo


class Poisto:
    def __init__(self, db_nimi=":memory:"):
        self.db = Database(db_nimi)

    def poista_viite(self, viite):

        #testataan ekaksi, että poistettava viite on olemassa
        haku = self.db.hae_viite(viite)
        if haku is None:
            return 'ei löytynyt' 
        
        # jos viite löytyy tietokannasta, tehdään sen poistaminen
        self.db.poista_viite(viite)
        return'viite poistettu'