# Lähteet: https://ohjelmistotuotanto-jyu.github.io/riippuvuuksien_injektointi_python/
# ja https://github.com/ohjelmistotuotanto-jyu/tehtavat/tree/main/osa2/riippuvuuksien-injektointi-1/src
# Otettu kurssin mallikoodi ja sama nimi tiedostolle

class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)

    def kirjoita(self, teksti):
        print(teksti)
