"""Ohjelma joka tulostaa tietokannan jokaisen alkion"""

# pylint: disable=too-few-public-methods

from database import Database


class Listaus:
    """Luokka joka vastaa rivien tulostuksesta"""

    def __init__(self, db_nimi=":memory:"):
        """Alustaa Listaus-olion ja luo Database-instanssin."""
        self.db = Database(db_nimi)

    def listaa_kaikki(self):
        """Tulostaa kaikki tietokannasta löytyvät rivit."""
        rivit = self.db.hae_kaikki()

        for rivi in rivit:
            print("-----")
            print(f"viite:  {rivi[1]}")
            print(f"type:   {rivi[2]}")
            print(f"author: {rivi[3]}")
            print(f"title:  {rivi[4]}")
            print(f"year:   {rivi[5]}")
