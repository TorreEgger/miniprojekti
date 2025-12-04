# pylint: skip-file

# MiniprojektiLibrary.py
# Kirjastotiedosto Robot Framework-testejä varten

from viite_repo import ViiteRepo
#from viite import Viite
from komentorivisovellus import Miniprojekti
from stub_io import StubIO
from stub_db import StubDB

class MiniprojektiLibrary:

    # Testiprojektin luonti
    def create_test_project(self):
        # testidataa
        db = StubDB([
            {"viite":"abc",
            "type":"inproceedings",
            "author":"Kalle",
            "title":"Testi",
            "year":2023,
            "booktitle": None, # Nonet tarvitaan tai muuten hajoaa testaus
            "journal": None,
            "volume": None,
            "pages": None,
            "publisher": None}
        ])
        self.io = StubIO()
        self.repo = ViiteRepo(db)
        self.app = Miniprojekti(self.io, self.repo)

    #Käyttäjän inputtien asetus
    def set_user_inputs(self, *inputs):
        self.io.inputs = list(inputs)

    def run_application(self):
        self.app.suorita()

    # Tulostuksen tarkistus
    def output_should_contain(self, expected):
        if not any(expected in line for line in self.io.outputs):
            raise AssertionError(f"'{expected}' ei löytynyt tulosteista.\nTulosteet: {self.io.outputs}")