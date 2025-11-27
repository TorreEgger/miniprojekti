# from 'file' import 'function'

class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)
    
    def kirjoita(self, teksti):
        print(teksti)

class Miniprojekti:
    def __init__(self, io):
            self._io = io

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
            if kasky == "c":
                self._io.kirjoita("")
                self._io.kirjoita("3")
                self._io.kirjoita("")
                continue

            # Yksittäisen viitteen hakeminen listasta
            if kasky == "d":
                self._io.kirjoita("")
                self._io.kirjoita("4")
                self._io.kirjoita("")
                continue
            
            if kasky == "help":
                self._io.kirjoita("")
                self._io.kirjoita("poistu   -poistuu ohjelmasta")
                self._io.kirjoita("")
                continue

            else:
                self._io.kirjoita("")
                self._io.kirjoita("Anna kunnollinen käsky.")
                self._io.kirjoita("")

def main():
    io = KonsoliIO()
    miniprojekti = Miniprojekti(io)

    miniprojekti.suorita()

if __name__ == "__main__":
    main()