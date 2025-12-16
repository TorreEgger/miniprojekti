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
        
        self.viite2 = Viite(viite="BER",
                            viitetyyppi="article",
                            author="Bart Mäkinen",
                            title="Opportunity costs",
                            year=1984,
                            journal="Cost-effective",
                            volume="9",
                            pages="28"
                            )
        
        self.viite3 = Viite(viite="BYR",
                            viitetyyppi="inproceedings",
                            author="Dax Smith",
                            title="Running effectively",
                            year=2002,
                            booktitle="Running together"
                            )       

    def test_voi_tehda_uuden_viitteen(self):
        self.assertEqual(self.viite.viite, "LCVB")
        self.assertEqual(self.viite.viitetyyppi, "book")
        self.assertEqual(self.viite.author, "Larman, Craig and Vodde, Bas")
        self.assertEqual(self.viite.year, 2008)
        self.assertEqual(self.viite.publisher, "Addison-Wesley Professional")
        self.assertEqual(self.viite.lisakentat["extra"], "extra")


    def test_journal_bibtex_muodossa(self):
        testi = self.viite2.to_bibtex()
        self.assertIn("journal = {Cost-effective}", testi)


    def test_volume_bibtex_muodossa(self):
        testi = self.viite2.to_bibtex()
        self.assertIn("volume = {9}", testi)


    def test_pages_bibtex_muodossa(self):
        testi = self.viite2.to_bibtex()
        self.assertIn("pages = {28}", testi)


    def test_booktitle_bibtex_muodossa(self):
        testi = self.viite3.to_bibtex()
        self.assertIn("booktitle = {Running together}", testi)


    def test_viite_bibtexiksi_antaa_oikeanlaisen_tulosteen(self):
        bibtex = self.viite.to_bibtex()
        self.assertTrue(bibtex.startswith("@book{"))
        self.assertTrue(bibtex.endswith("}"))

    def test_viite_merkkijonoksi_antaa_oikeanlaisen_tuloksen(self):
        mjono = self.viite.merkkijonoksi()

        self.assertTrue(mjono.startswith("viite"))
        self.assertTrue(mjono.endswith("extra"))
