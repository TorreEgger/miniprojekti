# from 'file' import 'function'
from viite_repo import ViiteRepo
from database import Database

class KonsoliIO:
    def lue(self, teksti):
        return input(teksti).strip()
    
    def kirjoita(self, teksti):
        print(teksti)

class Miniprojekti:
    def __init__(self, io, repo):
        self._io = io
        self.repo = repo

    def suorita(self):
        self._io.kirjoita("Kirjoita 'help' nähdäksesi annettavat käskyt")
        self._io.kirjoita("")

        while True:
            kasky = self._io.lue("Anna käsky: ")
    
            if kasky == "poistu":
                break
    
            # Viitteiden lisääminen
            if kasky == "a":
                self._io.kirjoita("")
                self._io.kirjoita("1")
                self._io.kirjoita("")
                continue

            # Tallennettujen viitteiden listaaminen
            if kasky == "b":
                self._io.kirjoita("")
                self._io.kirjoita("2")
                self._io.kirjoita("")
                continue

            # Tallennettujen viitteiden poistaminen tietokannasta
            if kasky == "poista":
                tunnus = self._io.lue("Syötä poistettava viite:")
                poistettava_viite = self.repo.hae_viitteella(tunnus)
                if poistettava_viite is None:
                    self._io.kirjoita("Poistettavaa viitettä ei löytynyt")
                else:
                    self._io.kirjoita("")
                    self.repo.poista_viite(tunnus)
                    self._io.kirjoita("Viite poistettu")
                continue

            # Yksittäisen viitteen hakeminen listasta
            if kasky == "hae":
                tunnus = self._io.lue("Syota viite:")
                viite = self.repo.hae_viitteella(tunnus)
                if not viite:
                    self._io.kirjoita("Viitettä ei löytynyt")
                else:
                    self._io.kirjoita("")
                    self._io.kirjoita(viite.viite)
                    self._io.kirjoita(viite.title)
                    self._io.kirjoita("")
                continue
            
            if kasky == "help":
                self._io.kirjoita("")
                self._io.kirjoita("poistu          -poistuu ohjelmasta")
                self._io.kirjoita("lisaa           -antaa kentät uuden viitteen lisäämistä varten")
                self._io.kirjoita("hae [viite]     -avulla haetaan tietty viite")
                self._io.kirjoita("poista [viite]  -avulla poistetaan tietty viite")
                self._io.kirjoita("listaa          -listaa kaikki viitteet")
                self._io.kirjoita("")
                continue

            if kasky == "bibtex":
                tunnus = self._io.lue("Syötä viite:")
                viite = self.repo.hae_viitteella(tunnus)
                if not viite:
                    self._io.kirjoita("Viitettä ei löytynyt")
                else:
                    self._io.kirjoita("")
                    self._io.kirjoita(viite.to_bibtex())
                    self._io.kirjoita("")

            else:
                self._io.kirjoita("")
                self._io.kirjoita("Anna kunnollinen käsky.")
                self._io.kirjoita("")

def main():
    io = KonsoliIO()
    db = Database("viitteet.db")    # tämä on gitignoressa ainakin toistaiseksi, jotta tietokanta pysyy "vakiona"
    db.create_table()
    db.insert_defaults()
    repo = ViiteRepo(db)
    miniprojekti = Miniprojekti(io, repo)


    miniprojekti.suorita()

if __name__ == "__main__":
    main()