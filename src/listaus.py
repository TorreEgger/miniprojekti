from database import Database

class Listaus:
    def setUp(self):
        rivit = self.db.hae_kaikki()
        for rivi in rivit:
            print("-----")
            print(f"viite:  {rivi[1]}")
            print(f"type:   {rivi[2]}")
            print(f"author: {rivi[3]}")
            print(f"title:  {rivi[4]}")
            print(f"year:   {rivi[5]}")
