import unittest
from database import Database
from viite_repo import ViiteRepo
from viite import Viite


class TestLisays(unittest.TestCase):
        

     #Otetaan tieotkanta käyttöön ja alustetaan
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_table()
        self.lisays = ViiteRepo(self.db)
        

    #poistaminen onnistuu
    def test_lisays_onnistuu(self):
        viite = Viite(
             viite="JOU22",
             viitetyyppi="book",
             author="David Diaz",
             title="Vibora",
             year=2015
            )
         
        self.assertEqual(self.lisays.lisaa_viite(viite), "lisäys onnistui") #lisäys onnistuu
        self.lisays.lisaa_viite(viite)

        viite3 = self.db.hae_viite("JOU22")   
        self.assertEqual(viite3[1], "JOU22")  

    #poistaminen epäonnistuu virheellisillä tiedoilla
    def test_lisays_epaonnistuu_virheellisilla_tiedoilla(self):
        viite2 = Viite(
             viite="JOU23",
             viitetyyppi="book",
             author="David Diaz",
             title="Vibora",
             year=None
            )
        

        self.assertEqual(self.lisays.lisaa_viite(viite2), "lisäys ei onnistunut")


        



            

           

    