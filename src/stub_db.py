# pylint: skip-file

# Stubi-tietokannalle mitä käytetään Robot-testaukseen
# Tänne lisätään ViiteRepon komentoja testausta varten

class StubDB:
    def __init__(self, data=None, lisakentat=None):
        self.data = data or []
        self.lisakentat = lisakentat or {}

    def hae_kaikki(self):
        return self.data
    
    def hae_viite(self, viitetunnus):
        for viite in self.data:
            if viite.get("viite") == viitetunnus:
                return viite
        return None
    
    def hae_lisakentat(self, viite):
        return self.lisakentat.get(viite, [])

    def poista_viite(self, viite):
        return "Viite poistettu"
    
    def lisaa_viiteolio(self, viite):
        return "Viite lisätty!"