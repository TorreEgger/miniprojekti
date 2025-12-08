# pylint: skip-file

# Stubi-tietokannalle mitä käytetään Robot-testaukseen
# Tänne lisätään ViiteRepon komentoja testausta varten

class StubDB:
    def __init__(self, data=None):
        self.data = data or []

    def hae_kaikki(self):
        return self.data
    
    def hae_viite(self, viitetunnus):
        for viite in self.data:
            if viite.get("viite") == viitetunnus:
                return viite
        return None
    
    def hae_lisakentat(self, viite):
        return []