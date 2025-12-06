import unittest
from viite import Viite

class TestViite(unittest.TestCase):
    def setUp(self):
        self.viite = Viite(viite="LCVB", 
                      viitetyyppi="book", 
                      author="Larman, Craig and Vodde, Bas", 
                      title="Scaling Lean and Agile Development",
                      year=2008,
                      publisher="Addison-Wesley Professional",
                      lisakentat={"extra": "extra"})

    def test_voi_tehda_uuden_viitteen(self):
        self.assertEqual(self.viite.viite, "LCVB")
        self.assertEqual(self.viite.viitetyyppi, "book")
        self.assertEqual(self.viite.author, "Larman, Craig and Vodde, Bas")
        self.assertEqual(self.viite.year, 2008)
        self.assertEqual(self.viite.publisher, "Addison-Wesley Professional")
        self.assertEqual(self.viite.lisakentat["extra"], "extra")

    def test_viite_bibtexiksi_antaa_oikeanlaisen_tulosteen(self):
        bibtex = self.viite.to_bibtex()
        self.assertTrue(bibtex.startswith("@book{"))
        self.assertTrue(bibtex.endswith("}"))
