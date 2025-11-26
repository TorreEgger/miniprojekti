from viite import Viite

# Hakee tällä hetkellä vain suoraan listasta, ei sql-tietokannasta

class ViiteRepo:
    def __init__(self, viitteet):
        self.viitteet = viitteet

    def hae_tunnisteella(self, tunniste):
        for viite in self.viitteet:
            if viite.viite == tunniste:  # viite-luokassa ei ole vielä tunniste attribuuttia --> vaihdetaan viite.tunniste, kun on
                return viite
        return None