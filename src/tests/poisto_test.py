import unittest
from database import Database
from poisto import Poisto

class TestPoisto(unittest.TestCase):
             
        #Otetaan tieotkanta käyttöön ja alustetaan
        def setUp(self):
            self.db = Database(":memory:")
            self.db.create_table()

            #sopiva testidata
            self.db.lisaa_viite({
            "viite": "JJQ12",
            "type": "book",
            "author": "Matti Martikainen",
            "title": "Parhaat kesäkaupungit",
            "year": 1988              
            })

            # Alustukset
            self.poisto = Poisto()
            self.poisto.db = self.db


        #testataan että poistaminen onnistuu databasen poista_viitteellä
        def test_poistaminen_onnistuu_tietokannan_metodilla(self):
              viite = self.db.hae_viite("JJQ12")
              self.assertEqual(viite[1], "JJQ12")

              self.db.poista_viite("JJQ12")
              jalkeen = self.db.hae_viite("JJQ12")
              self.assertEqual(jalkeen, None)  


        #testataan että poistaminen onnistuu poisto-luokan metodilla
        #tätä tarvii varmaan viilata vielä
        def test_poistaminen_onnistuu_poisto_luokan_metodilla(self):

            viite = self.db.hae_viite("JJQ12")
            self.assertEqual(viite[1], "JJQ12")

            self.assertEqual(self.poisto.poista_viite("JJQ12"), 'viite poistettu') #poisto-luokassa onnistunut poisto ilmoitetaan tällä, ehkä jokin parempi keino pitäisi tehdä?
            self.assertEqual(self.poisto.poista_viite("JJ"), 'ei löytynyt') #poisto-luokassa ilmoitetaan näin, jos poistettavaa viitettä ei löydy