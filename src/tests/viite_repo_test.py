import unittest
from unittest.mock import Mock
from viite_repo import ViiteRepo

class TestHakuMock(unittest.TestCase):

    def setUp(self):
        # Mock-database
        self.mock_db = Mock()

        # Mock dataa
        self.testiviitteet = [
            {
                "viite": "abc",
                "type": "inproceedings",
                "author": "jaska",
                "title": "Otsikko1",
                "year": 2023,
            },
            {
                "viite": "def",
                "type": "inproceedings",
                "author": "kalle",
                "title": "Otsikko2",
                "year": 2025,
            },
            {
                "viite": "ghi",
                "type": "inproceedings",
                "author": "kalle",
                "title": "Otsikko2",
                "year": 2023,
            }
        ]

        # Mock palautusarvo
        self.mock_db.hae_kaikki.return_value = self.testiviitteet
        # Mock-database repo
        self.repo = ViiteRepo(self.mock_db)

    def test_haku_loytaa_viitteen(self):
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
        
    def test_palauttaa_none_jos_ei_loydy(self):
        self.mock_db.hae_viite.return_value = None
        viite = self.repo.hae_viite("xyz")
        self.mock_db.hae_viite.assert_called_once_with("xyz")
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
