import unittest
from database import Database
from viite_repo import ViiteRepo
from viite import Viite

class TestPoisto(unittest.TestCase):
             
        #Otetaan tieotkanta käyttöön ja alustetaan
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_table()
        self.metodi = ViiteRepo(self.db)



    #testataan että poistaminen onnistuu viite_repon poistamis-metodilla
    def test_poistaminen_onnistuu_viiterepon_metodilla(self):
        viite = Viite(
        viite="JOU22",
        viitetyyppi="book",
        author="David Diaz",
        title="Vibora",
        year=2015
        )

        self.metodi.lisaa_viite(viite)

        self.assertEqual(self.metodi.poista_viite("JOU22"), "viite poistettu")


    #testataan että poistaminen onnistuu viite_repon poistamis-metodilla
    def test_poistaminen_ei_onnistu_jos_viitetta_ei_loydy(self):

        self.assertEqual(self.metodi.poista_viite("HAUKI"), "ei löytynyt")
