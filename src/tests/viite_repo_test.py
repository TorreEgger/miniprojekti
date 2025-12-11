import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
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
            },
            {
                "viite": "jkl",
                "type": "article",
                "author": "Matti Meikalainen",
                "title": "Otsikko2",
                "year": 2020,
                "booktitle": "ISO OTSIKKO",
                "journal": None,
                "volume": None,
                "pages": "89",
                "publisher": "kotava"
            }
        ]

        # Mock palautusarvo
        self.mock_db.hae_kaikki.return_value = self.testiviitteet
        # Mock-database repo
        self.repo = ViiteRepo(self.mock_db)

        # Toinen DB ja testidataa tuple muunnoksen testausta varten
        self.db2 = MagicMock()
        self.db2.cursor = MagicMock()

        self.db2.cursor.description = [("viite",), ("author",), ("title",)]
        self.repo2 = ViiteRepo(self.db2)

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

    # Tuple -> dict muunnoksen testit
    def test_dict_kaytetaan_suoraan(self):
        rows = [{"viite": "TEST123", "author": "Owner", "title": "otsake"}]
        self.db2.hae_kaikki.return_value = rows
        tulos = self.repo2.hae_viite_hakuehdoilla()
        self.assertEqual(tulos, rows)
 
    def test_tuple_muuntuu_dict(self):
        rows = [("TEST345", "matti", "Otsake"), ("TEST678", "teppo", "Otsake2")]
        self.db2.hae_kaikki.return_value = rows
        tulos = self.repo2.hae_viite_hakuehdoilla()
        self.assertEqual(tulos[0]["viite"], "TEST345")
        self.assertEqual(tulos[0]["author"], "matti")
        self.assertEqual(tulos[0]["title"], "Otsake")

    def test_tyhjat_kentat_palauttaa_tyhjan(self):
        self.db2.hae_kaikki.return_value = [{"viite": None, "author": None, "title": None}]
        tulos = self.repo2.hae_viite_hakuehdoilla(author="author")
        self.assertEqual(tulos, [])

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

    def test_palauttaa_tyhjan_jos_kentta_none(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(journal=None)
        self.assertEqual(tulokset, [])
    
    def test_haku_pidemmalla_merkkijonolla_lowercase(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(author = "matti meikalainen")
        self.assertEqual(len(tulokset), 1)
        self.assertTrue(tulokset[0]["viite"], "jkl")

    def test_hae_viite_title_osuma(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(booktitle="otsikko")
        self.assertEqual(len(tulokset), 1)
        self.assertTrue(tulokset[0]["viite"], "jkl")

    def test_ei_osumaa_publisher(self):
        tulokset = self.repo.hae_viite_hakuehdoilla(publisher="olematon julkaisija")
        self.assertEqual(tulokset, [])

    def test_paluttaa_tyhjan_kun_ei_riveja(self):
        self.mock_db.cursor.execute = Mock()
        self.mock_db.cursor.fetchall.return_value = []
        tulos = self.repo.hae_viite_hakuehdoilla(author="olematon")
        self.assertEqual(tulos, [])

    def test_hae_viite_hakuehdoilla_lisaa_lisakentat(self):
        self.mock_db.hae_kaikki.return_value = [
            ("ABC", "article", "Matti", "Otsikko", 2024, None, None, None, None, None)
        ]
        self.mock_db.hae_lisakentat.return_value = [
            ("ABC", "lisa1", "value1"),
            ("ABC", "lisa2", "value2")
        ]
        tulos = self.repo.hae_viite_hakuehdoilla()
        self.assertTrue(len(tulos) > 0)
        viite = tulos[0]
        self.assertIn("lisa1", viite)
        self.assertEqual(viite["lisa1"], "value1")
        self.assertIn("lisa2", viite)
        self.assertEqual(viite["lisa2"], "value2")

    # Kaikkien viitteiden listauksien testit
    def test_listaa_kaikki_palauttaa_tyhjan_viestin_jos_ei_tuloksia(self):
        # Mockataan tyhjä tietokanta
        self.mock_db.hae_kaikki.return_value = []

        tulos = self.repo.listaa_kaikki()
        self.assertEqual(tulos.strip(), "Tietokanta on tyhjä")

    # Lisäkenttien tulostuksien testaus
    def test_listaa_kaikki_tulostaa_viitteen_ja_lisakentat(self):
        
        self.mock_db.hae_kaikki.return_value = [self.testiviitteet[0]]
        self.mock_db.hae_lisakentat.return_value = [
            {"field": "Isbn", "value": "12345"},
            {"field": "Editor", "value": "Veikko"}
        ]
        
        testi_tulos = self.repo.listaa_kaikki()

        odotetut_rivit = (
            "Hakutulokset:\n\n"
            "viite: abc\n"
            "type: inproceedings\n"
            "author: jaska\n"
            "title: Otsikko1\n"
            "year: 2023\n"
            "Isbn: 12345\n"
            "Editor: Veikko\n"
        )

        self.assertEqual(testi_tulos, odotetut_rivit)

        # Varmistetaan, että lisäkenttien hakua kutsuttiin oikealla arvolla
        self.mock_db.hae_lisakentat.assert_called_once_with("abc")
        
    # Lisäkenttien tulostuksien testaus BibTeX-versio
    def test_listaa_kaikki_tulostaa_viitteen_ja_lisakentat_bibtex(self):

        self.mock_db.hae_kaikki.return_value = [self.testiviitteet[0]]
        self.mock_db.hae_lisakentat.return_value = [
            {"field": "Isbn", "value": "12345"},
            {"field": "Editor", "value": "Veikko"}
        ]

        # Mockataan hae_viitteella palauttamaan samanlainen viiteolio koska käytetään viite-luokkaa
        viiteolio = Viite(
            "abc", "inproceedings", "jaska", "Otsikko1", 2023,
            lisakentat={"Isbn":"12345", "Editor":"Veikko"}
        )
        self.repo.hae_viitteella = Mock(return_value=viiteolio)

        testi_tulos = self.repo.listaa_kaikki_bibtex()

        odotetut = (
            "Hakutulokset BibTeX-muodossa:\n\n"
            "@inproceedings{abc,\n"
            "    author = {jaska},\n"
            "    title = {Otsikko1},\n"
            "    year = {2023},\n"
            "    Isbn = {12345}\n"
            "    Editor = {Veikko}\n"
            "}\n"
        )

        self.assertEqual(testi_tulos, odotetut)

    def test_listaa_kaikki_bibtex_muodossa_palauttaa_tyhjan_viestin_jos_ei_tuloksia(self):

        self.mock_db.hae_kaikki.return_value = []

        tulos = self.repo.listaa_kaikki_bibtex()
        self.assertEqual(tulos.strip(), "Tietokanta on tyhjä")


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

    
    def test_listaa_kaikki_saa_kentat(self):

        self.mock_db.hae_kaikki.return_value = [self.testiviitteet[0]]
        self.mock_db.hae_lisakentat.return_value = []
        
        testi_tulos = self.repo.listaa_kaikki()

        odotetut_rivit = (
            "Hakutulokset:\n\n"
            "viite: abc\n"
            "type: inproceedings\n"
            "author: jaska\n"
            "title: Otsikko1\n"
            "year: 2023\n"
        )

        self.assertEqual(testi_tulos, odotetut_rivit)


    def test_listaa_laikki_valinnaisetkentat(self):
        self.mock_db.hae_kaikki.return_value = [self.testiviitteet[3]]
        self.mock_db.hae_lisakentat.return_value = []

        testi_tulos = self.repo.listaa_kaikki()

        odotetut_rivit = (
            "Hakutulokset:\n\n"
            "viite: jkl\n"
            "type: article\n"
            "author: Matti Meikalainen\n"
            "title: Otsikko2\n"
            "year: 2020\n"
            "Booktitle: ISO OTSIKKO\n"
            "Pages: 89\n"
            "Publisher: kotava\n"
        )


        self.assertEqual(testi_tulos, odotetut_rivit)


