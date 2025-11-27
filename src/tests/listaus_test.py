import unittest
import io
import sys
from database import Database
from listaus import Listaus


class TestListaus(unittest.TestCase):

    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_table()

        # testiviitteet
        self.db.lisaa_viite({
            "viite": "ABC123",
            "type": "book",
            "author": "John Doe",
            "title": "Testikirja",
            "year": 2020
        })

        self.db.lisaa_viite({
            "viite": "XYZ999",
            "type": "article",
            "author": "Jane Smith",
            "title": "Toinen testijuttu",
            "year": 2022
        })

        # Listaus-luokan olio
        self.listaus = Listaus()
        self.listaus.db = self.db

    def test_listaus_tulostaa_oikein(self):
        # Kaapataan print-output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # suoritetaan tulostus
        self.listaus.listaa_kaikki()

        # palautetaan stdout normaaliksi
        sys.stdout = sys.__stdout__

        tuloste = captured_output.getvalue()

        # Tarkistetaan että molemmat viitteet löytyvät
        self.assertIn("viite:  ABC123", tuloste)
        self.assertIn("author: John Doe", tuloste)
        self.assertIn("title:  Testikirja", tuloste)

        self.assertIn("viite:  XYZ999", tuloste)
        self.assertIn("author: Jane Smith", tuloste)
        self.assertIn("title:  Toinen testijuttu", tuloste)

        # Tarkistetaan että erotusviivat (-----) tulostuvat kahta viitettä varten
        self.assertEqual(tuloste.count("-----"), 2)