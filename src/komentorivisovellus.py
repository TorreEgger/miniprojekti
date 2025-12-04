# from 'file' import 'function'
from viite_repo import ViiteRepo
from database import Database
from viite import Viite

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
            if kasky == "lisaa":
                self._io.kirjoita("")
                viite = self._io.lue("Syötä viite:")          
                viitetyyppi = self._io.lue("Syötä viitetyyppi:")
                tekijä = self._io.lue("Syötä tekijä(t):")
                otsikko = self._io.lue("Syötä otsikko:")
                vuosi = self._io.lue("Syötä julkaisuvuosi:")
                if viitetyyppi == "inproceedings":
                    booktitle = self._io.lue("Syötä otsikko:")
                    lisattava_viite = Viite(
                        viite=viite,
                        viitetyyppi=viitetyyppi,
                        author=tekijä,
                        title=otsikko,
                        booktitle=booktitle,
                        year=vuosi
                    )
                    self.repo.database.lisaa_viiteolio(lisattava_viite)
                    self._io.kirjoita("Viite lisätty!")
                if viitetyyppi == "article":
                    volyymi = self._io.lue("Syötä volyymi:")
                    sivut = self._io.lue("Syötä sivumäärä:")
                    lehti = self._io.lue("Missä lehdessä julkaistu?:")
                    lisattava_viite = Viite(
                        viite=viite,
                        viitetyyppi=viitetyyppi,
                        author=tekijä,
                        title=otsikko,
                        year=vuosi,
                        journal=lehti,
                        volume=volyymi,
                        pages=sivut
                    )
                    self.repo.database.lisaa_viiteolio(lisattava_viite)
                    self._io.kirjoita("Viite lisätty!")
                if viitetyyppi == "book":
                    julkaisija = self._io.lue("Syötä julkaisija:")
                    lisattava_viite = Viite(
                        viite=viite,
                        viitetyyppi=viitetyyppi,
                        author=tekijä,
                        title=otsikko,
                        year=vuosi,
                        publisher=julkaisija
                    )
                    self.repo.database.lisaa_viiteolio(lisattava_viite)
                    self._io.kirjoita("Viite lisätty!")
                continue

            # Tallennettujen viitteiden listaaminen
            if kasky == "listaa":
                self._io.kirjoita("")
                onkobib = self._io.lue("Haluatko listan BibTeX-muodossa? (y/n):")
                if onkobib == "y":
                    tulokset = self.repo.listaa_kaikki_bibtex()
                    self._io.kirjoita(tulokset)
                    continue
                if onkobib == "n":
                    tulokset = self.repo.listaa_kaikki()
                    self._io.kirjoita(tulokset)
                    continue
                self._io.kirjoita("Annoit virheellisen komennon, mitään ei tulosteta")
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

            # Viitteen hakeminen viitteen nimellä tai hakuehtoja käyttäen
            if kasky.startswith("hae"):

                if kasky.strip() =="hae":
                    tunnus = self._io.lue("Syötä viite:")
                    viite = self.repo.hae_viitteella(tunnus)

                    if not viite:
                        self._io.kirjoita("Viitettä ei löytynyt")
                    else:
                        self._io.kirjoita("")
                        self._io.kirjoita(viite.viite)
                        self._io.kirjoita(viite.title)
                        self._io.kirjoita("")
                    continue

                ehto_teksti = kasky[4:]
                osat = ehto_teksti.split()
                hakuehdot = {}
                i = 0

                while i < len(osat):
                    osa = osat[i]
                    if "=" in osa:
                        kentta, arvo = osa.split("=", 1)
                        i += 1
                        while i < len(osat) and "=" not in osat[i]:
                            arvo += " " + osat[i]
                            i += 1
                        if kentta in ("author", "title", "booktitle", "publisher"):
                            hakuehdot[kentta] = arvo.lower()
                        else:
                            hakuehdot[kentta] = arvo
                        continue
                    i += 1

                tulokset = self.repo.hae_viite_hakuehdoilla(**hakuehdot)
                if not tulokset:
                    self._io.kirjoita("Ei hakuehtoja vastaavia viitteitä \n")
                    continue

                self._io.kirjoita("\nHakutulokset:\n")
                for viite in tulokset:
                    self._io.kirjoita(f"ID: {viite['id']}")
                    self._io.kirjoita(f"viite: {viite['viite']}")
                    self._io.kirjoita(f"type: {viite['type']}")
                    self._io.kirjoita(f"author: {viite['author']}")
                    self._io.kirjoita(f"title: {viite['title']}")
                    self._io.kirjoita(f"year: {viite['year']}")

                    # Valinnaiset kentät:
                    valinnaiset = ["booktitle", "journal", "volume", "pages", "publisher"]
                    for k in valinnaiset:
                        if viite[k]:
                            self._io.kirjoita(f"{k.capitalize()}: {viite[k]}")
                    self._io.kirjoita("")
                continue
            
            # ACM-tietokannasta viitteen tiedot
            if kasky in {'acm', 'ACM'}:
                self._io.kirjoita("")
                acm = self._io.lue("Anna ACM-linkki: ")
                self._io.kirjoita("")
                continue
            
            if kasky == "help":
                self._io.kirjoita("")
                self._io.kirjoita("poistu                     -poistuu ohjelmasta")
                self._io.kirjoita("lisaa                      -antaa kentät uuden viitteen lisäämistä varten")
                self._io.kirjoita("hae                        -avulla haetaan tietty viite")
                self._io.kirjoita("hae ehto1=abc ehto2=xyz    -hakee ehtojen perusteella")
                self._io.kirjoita("poista [viite]             -avulla poistetaan tietty viite")
                self._io.kirjoita("listaa                     -listaa kaikki viitteet")
                self._io.kirjoita("acm/ACM                    -hakee ACM-tietokannasta viitteen tiedot")
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