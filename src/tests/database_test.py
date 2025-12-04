import unittest
from database import Database
from viite import Viite

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_table()
        self.db.insert_defaults()

    def tearDown(self):
        self.db.conn.close()

    def test_lisatty_viite_on_tietokannassa(self):
        uusi = {"viite": "joku123", 
                "type": "inproceedings", 
                "author": "jonne", 
                "title": "luokat ovat olioita", 
                "year": 2025}

        self.db.lisaa_viite(uusi)
        rivi = self.db.hae_viite("joku123")
        self.assertEqual(uusi["viite"], rivi[1])

    def test_kursorin_kenttiin_voi_viitata_nimella(self):
        rivi = self.db.hae_viite("VPL11")

        self.assertEqual(rivi ["type"], "inproceedings")

    def test_viitteen_lisaaminen_oliona(self):
        viiteolio = Viite("zimmerman2002becoming", 
                          "article", 
                          "Zimmerman, Barry J", 
                          "Becoming a self-regulated learner: An overview", 
                          2002, 
                          journal="Theory into practice", 
                          volume="42", 
                          pages="64--70", 
                          publisher="Taylor & Francis")

        self.db.lisaa_viiteolio(viiteolio)

        rivi = self.db.hae_viite("zimmerman2002becoming")
        self.assertEqual(rivi["type"], viiteolio.viitetyyppi)
        self.assertEqual(rivi["pages"], viiteolio.pages)