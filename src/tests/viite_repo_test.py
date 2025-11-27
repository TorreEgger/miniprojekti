import unittest
from unittest.mock import Mock
from viite_repo import ViiteRepo
from viite import Viite

class TestHakuMock(unittest.TestCase):

    def setUp(self):
        # Mock-database
        self.mock_db = Mock()
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

