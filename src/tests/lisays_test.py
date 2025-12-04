import unittest
from database import Database


class TestLisays(unittest.TestCase):
        

     #Otetaan tieotkanta käyttöön ja alustetaan
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_table()
        


    #käytännössä sama kuin poistossa, mutta ilman poistamista
    def test_lisays_onnistuu(self):
            
        
        self.db.lisaa_viite({
            "viite": "JJQ12",
            "type": "book",
            "author": "Matti Martikainen",
            "title": "Parhaat kesäkaupungit",
            "year": 1988              
            })

        viite = self.db.hae_viite("JJQ12")
        self.assertEqual(viite[1], "JJQ12")

    
    def test_lisays_virheellisella_viittella_ei_onnistu(self):
        self.db.lisaa_viite({
            "viite": "JJQ13",
            "type": "book",
            "author": "Matti Martikainen",
            "title": "Parhaat kesäkaupungit",
            "year": None             
            })

        viite2 = self.db.hae_viite("JJQ13")
        self.assertEqual(viite2, None)

            

           

    