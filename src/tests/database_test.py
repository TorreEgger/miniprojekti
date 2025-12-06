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


    def test_viitetta_ei_lisatty_koska_viite_loytyy_jo(self):
        viiteolio = Viite("VPL11", "article", "Pellonpää Erkki", "Hyvää itsenäisyyspäivää!", 2025)
        response = self.db.lisaa_viiteolio(viiteolio)
        self.assertNotEqual(response, self.db.viite_lisatty)

    def test_lisakenttien_hakeminen_onnistuu_jos_viitteella_on_niita(self):
        kentat = self.db.hae_lisakentat("VPL11")
        self.assertEqual(kentat[0]["field"], "lisakentta")

    def test_kaikki_lisatyt_viitteet_loytyvat(self):
        viitteet = self.db.hae_kaikki()
        self.assertEqual(len(viitteet), 3)

    def test_poistamisen_jalkeen_viitetta_ei_loydy(self):
        viite = "VPL11"
        loytyy = self.db.hae_viite(viite)
        self.assertTrue(loytyy)
        self.db.poista_viite(viite)
        loytyyko_viela = self.db.hae_viite(viite)
        self.assertFalse(loytyyko_viela)

    def test_viitteelle_voi_lisata_kenttia(self):
        kentta = "pages"
        arvo = "672"
        viite = "Martin09"
        self.db.lisaa_kentta(viite, kentta, arvo)
        lisatty = self.db.hae_lisakentat(viite)
        self.assertEqual(lisatty[0]["field"], "pages")
        self.assertEqual(lisatty[0]["value"], "672")

    def test_kentan_lisaaminen_uudestaan_paivittaa_arvoa(self):
        kentta = "pages"
        arvo = "672"
        viite = "Martin09"
        self.db.lisaa_kentta(viite, kentta, arvo)
        lisatty = self.db.hae_lisakentat(viite)
        self.assertEqual(lisatty[0]["value"], "672")

        arvo = "666"
        self.db.lisaa_kentta(viite, kentta, arvo)
        lisatty = self.db.hae_lisakentat(viite)
        self.assertEqual(lisatty[0]["value"], "666")

    def test_viitteen_poistaminen_poistaa_myos_lisakentat(self):
        viite = "VPL11"
        loytyy = self.db.hae_viite(viite)
        self.assertIsNotNone(loytyy)
        lisakentta_loytyy = self.db.hae_lisakentat(viite)
        self.assertIsNotNone(lisakentta_loytyy)

        self.db.poista_viite("VPL11")

        ei_loydy = self.db.hae_viite(viite)
        self.assertIsNone(ei_loydy)

        ei_kenttia = self.db.hae_lisakentat(viite)
        self.assertEqual(len(ei_kenttia), 0)