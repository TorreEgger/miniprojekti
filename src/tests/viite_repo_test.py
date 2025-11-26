import unittest
from viite_repo import ViiteRepo
from viite import Viite


class TestHaku(unittest.TestCase):

    def setUp(self):
        self.viite1 = Viite("abc")
        self.viite2 = Viite("xyz")
        self.repo = ViiteRepo([self.viite1, self.viite2])

    def test_haku_loytaa_viitteen(self):
        tulos = self.repo.hae_tunnisteella("xyz")
        self.assertIs(tulos, self.viite2)

    def test_palauttaa_none_jos_ei_loydy(self):
        tulos = self.repo.hae_tunnisteella("ei ole olemassa")
        self.assertIsNone(tulos)

