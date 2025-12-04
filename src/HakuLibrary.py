from viite import Viite
from viite_repo import ViiteRepo
from komentorivisovellus import Miniprojekti
from stub_io import StubIO
from stub_db import StubDB

class HakuLibrary:

    def create_test_env(self):
        db = StubDB([
            {
                "id":"1",
                "viite":"aaa",
                "type":"inproceedings",
                "author":"Pekka",
                "title":"Testi",
                "year":2023,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            },
            {
                "id":"2",
                "viite":"bbb",
                "type":"book",
                "author":"Kalle",
                "title":"TestiX",
                "year":2022,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            },
            {
                "id":"3",
                "viite":"ccc",
                "type":"inproceedings",
                "author":"Matti",
                "title":"TestiY",
                "year":2021,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            },
            {
                "id":"4",
                "viite":"ddd",
                "type":"inproceedings",
                "author":"Kalle",
                "title":"TestiZ",
                "year":2021,
                "booktitle": None,
                "journal": None,
                "volume": None,
                "pages": None,
                "publisher": None
            }
        ])
        self.io = StubIO()
        self.repo = ViiteRepo(db)
        self.app = Miniprojekti(self.io, self.repo)

    def set_user_inputs(self, *inputs):
        self.io.inputs = list(inputs)
    
    def run_application(self):
        self.app.suorita()

    def output_should_contain(self, expected):
        if not any(expected in line for line in self.io.outputs):
            raise AssertionError(f"'{expected}' ei löytynyt .\nOutput: {self.io.outputs}")

    def output_should_not_contain(self, text):
        if any(text in line for line in self.io.outputs):
            raise AssertionError(f"'{text}' löytyi, vaikka ei pitäisi.\nOutput: {self.io.outputs}")
