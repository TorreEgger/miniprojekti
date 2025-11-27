from viite import Viite
from database import Database

class ViiteRepo:
    def __init__(self, database):
        self.database = database

    def hae_viite(self, viite):
        tulos = self.database.hae_viite(viite)
        if not tulos:
            return None
        
        return tulos