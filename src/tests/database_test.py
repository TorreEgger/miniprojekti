import unittest
from database import Database

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_table()
        self.db.insert_defaults()

    def tearDown(self):
        self.db.conn.close()

    def test_lisatty_viite_on_tietokannassa(self):
        uusi = {"viite": "joku123", "type": "inproceedings", "author": "jonne", "title": "luokat ovat olioita", "year": 2025}

        self.db.lisaa_viite(uusi)
        rivi = self.db.hae_viite("joku123")
        self.assertEqual(uusi["viite"], rivi[1])