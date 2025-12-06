import unittest
from unittest.mock import Mock
from viite_repo import ViiteRepo
from database import Database
from viite import Viite

class TestHakuMock(unittest.TestCase):

    def setUp(self):
        # Mock-database
        self.mock_db = Mock()

        self.mock_db.cursor = Mock()
        self.mock_db.cursor.description = [
            ("viite",), ("type",), ("author",), ("title",), ("year",), 
            ("booktitle",), ("journal",), ("volume",), ("pages",), ("publisher",)
        ]

        # Mock dataa
        self.testiviitteet = [
            {
                "viite": "abc",
                "type": "inproceedings",
                "author": "jaska",
                "title": "Otsikko1",
                "year": 2023,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            },
            {
                "viite": "def",
                "type": "inproceedings",
                "author": "kalle",
                "title": "Otsikko2",
                "year": 2025,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            },
            {
                "viite": "ghi",
                "type": "inproceedings",
                "author": "kalle",
                "title": "Otsikko2",
                "year": 2023,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            }
        ]

        # Mock palautusarvo
        self.mock_db.hae_kaikki.return_value = self.testiviitteet
        # Mock-database repo
        self.repo = ViiteRepo(self.mock_db)

        # In memory db, koska Toukolle mockit liian vaikeita
        db = Database()
        db.create_table()
        db.insert_defaults()
        self.db_repo = ViiteRepo(db)

    def test_hae_viite_loytaa_viitteen(self):
        # Mockataan db.hae_viite palauttamaan sqlite-tuple
        self.mock_db.hae_viite.return_value = {
            "viite": "abc",
            "type": "inproceedings",
            "author": "jonne",
            "title": "Otsikko",
            "year": 2025 
        }

        viite = self.repo.hae_viite("abc")
        self.mock_db.hae_viite.assert_called_once_with("abc")

        # Tarkistetaan tulos
        self.assertEqual(viite["viite"], "abc")
        self.assertEqual(viite["type"], "inproceedings")
        self.assertEqual(viite["author"], "jonne")
        self.assertEqual(viite["title"], "Otsikko")
        self.assertEqual(viite["year"], 2025)
        
    def test_hae_viite_palauttaa_none_jos_ei_loydy(self):
        self.mock_db.hae_viite.return_value = None
        viite = self.repo.hae_viite("xyz")
        self.mock_db.hae_viite.assert_called_once_with("xyz")
        self.assertIsNone(viite)

    def test_hae_viitteella_palauttaa_viite_olion_jos_loytyy(self):
        # Mockataan database.hae_viite palauttamaan rivi
        viite = self.db_repo.hae_viitteella("CBH91")
        
        # Tarkistetaan, että palautui Viite-olio
        self.assertIsNotNone(viite)
        self.assertEqual(viite.viite, "CBH91")
        self.assertEqual(viite.viitetyyppi, "article")
        self.assertEqual(viite.author, "Allan Collins and John Seely Brown and Ann Holum")
        self.assertEqual(viite.title, "Cognitive apprenticeship: making thinking visible")
        self.assertEqual(viite.year, 1991)

    def test_hae_viitteella_palauttaa_none_jos_ei_loydy(self):
        self.mock_db.hae_viite.return_value = None
        viite = self.repo.hae_viitteella("tuntematon")
        self.mock_db.hae_viite.assert_called_once_with("tuntematon")
        self.assertIsNone(viite)

    # Hakuehdoilla viitteen hakemisen testit
    def test_haku_authorilla(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(author="kalle")
        self.assertEqual(len(tulokset), 2)
        self.assertTrue(all(v["author"] == "kalle" for v in tulokset))

    def test_haku_vuodella(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(year=2023)
        self.assertEqual(len(tulokset), 2)
        self.assertTrue(all(v["year"] == 2023 for v in tulokset))

    def test_haku_author_ja_vuosi(self):           
        tulokset = self.repo.hae_viite_hakuehdoilla(author="kalle", year=2025)
        self.assertEqual(len(tulokset), 1)
        self.assertEqual(tulokset[0]["viite"], "def")

    def test_haku_tyhjilla_ehdoilla_palauttaa_kaikki(self):
        tulokset = self.repo.hae_viite_hakuehdoilla()
        self.assertEqual(len(tulokset), len(self.testiviitteet))

    def test_ei_loydy_jos_hakuehto_ei_vastaa_mitaan(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(author="olematon")
        self.assertEqual(tulokset, [])

    # Kaikkien viitteiden listauksien testit
    def test_listaa_kaikki_palauttaa_tyhjan_viestin_jos_ei_tuloksia(self):
        # Mockataan tyhjä tietokanta
        self.mock_db.hae_kaikki.return_value = []

        tulos = self.repo.listaa_kaikki()
        self.assertEqual(tulos.strip(), "Tietokanta on tyhjä")
        
    def test_listaa_kaikki_palauttaa_oikean_muotoisen_listauksen(self):
        # Mockataan testiviitteet takaisin käyttöön
        self.mock_db.hae_kaikki.return_value = self.testiviitteet

        tulos = self.repo.listaa_kaikki()

        # Tarkista että otsikko on
        self.assertIn("Hakutulokset:", tulos)

        # Tarkistetaan että jokaisen viitteen pakolliset kentät esiintyvät
        for v in self.testiviitteet:
            self.assertIn(f"viite: {v['viite']}", tulos)
            self.assertIn(f"type: {v['type']}", tulos)
            self.assertIn(f"author: {v['author']}", tulos)
            self.assertIn(f"title: {v['title']}", tulos)
            self.assertIn(f"year: {v['year']}", tulos)

        # Valinnaiset kentät ovat None eikä niiden pitäisi näkyä
        self.assertNotIn("Booktitle:", tulos)
        self.assertNotIn("Journal:", tulos)
        self.assertNotIn("Volume:", tulos)
        self.assertNotIn("Pages:", tulos)
        self.assertNotIn("Publisher:", tulos)

    def test_viiteolion_saa_lisakentat(self):
        lisakentat = {
            "language": "English",
            "ISBN": "9780134757599"
        }
        uusi = Viite("joku42", "book", "Fowler, Martin", "Refactoring", 2019, lisakentat=lisakentat)

        response = self.db_repo.lisaa_viiteolio(uusi)
        self.assertEqual(response, "Viite lisätty!")
        viite = self.db_repo.hae_viitteella("joku42")
        self.assertEqual(viite.lisakentat["language"], "English")
