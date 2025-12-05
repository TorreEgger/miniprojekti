# Miniprojekti
Ryhmän 6 toteuttama miniprojekti

[![CI](https://github.com/TorreEgger/miniprojekti/actions/workflows/main.yml/badge.svg)](https://github.com/TorreEgger/miniprojekti/actions/workflows/main.yml)
[![codecov](https://codecov.io/github/TorreEgger/miniprojekti/graph/badge.svg?token=6J8AK1UX64)](https://codecov.io/github/TorreEgger/miniprojekti)

Projektin backlog: https://jyu-my.sharepoint.com/:x:/g/personal/kirskaxt_jyu_fi/IQAegL_ux5ZjSpN1c-rVZH4CAadPDwjwBHSxYaUqLI5SDEg?e=omyNjP

# Definition Of Done (DOD)

Jotta voimme määrittää jonkun vaatimuksen olevan valmis, seuraamme seuraavaa listausta:
* Se on suunniteltu tarkoin. Tarkoittaen, että se on sirpaloitu eri tehtäviksi ja sen olemassaolo on tärkeää koko ohjelmalle.
* Ohjelmakoodi: Koodi on selkeää, nimeämiskäytänteen mukaista ja Pylint ei anna virheilmoituksia.
* Testaus: Ohjelmakoodia on testattu yksikkötesteillä (ja ne menevät läpi) sekä myöskin automatisoiduilla testeillä (nekin menevät läpi).
* Dokumentaatio: Kirjoitetut toiminnallisuudet on oltava dokumentoitu selkeästi, jotta muutkin kuin kirjoittaja(t) pystyvät sitä ymmärtämään.
* Integraatio: Toiminallisuuksien tulee olla integroitu ohjelmistoon ja ne eivät saa olla ristiriidassa keskenään.
* Tuotantoon vieminen: Lopuksi koodi tulee viedä säilöön! Jos toteutusta on tehty eri haarassa kuin (main/master), niin tulee tehdä merge näiden eri haarojen välille.
* Hyväksymiskriteerit täyttyy backlogin mukaan

# Asennusohjeet

Varmista ensin nämä asiat: 
* Pythonista vähintään versio (3.10). Jos ei ole, niin asenna täältä uusi (https://www.python.org/downloads/)
* Poetry asennettuna. Jos ei ole, niin katso täältä tarkemmat ohjeet (https://ohjelmistotuotanto-jyu.github.io/poetry#ratkaisuja-yleisiin-ongelmiin).

Näiden jälkeen tee seuraavat asiat:
* Kloonaa projekti itsellesi sopivassa hakemistossa
* Asenna tarvittavat riippuvuudet komennolla "poetry install --no-root"

Asennusohjeita varten katsottu kurssin omia ohjesivuja: (https://ohjelmistotuotanto-jyu.github.io/ongelmia/) sekä (https://ohjelmistotuotanto-jyu.github.io/poetry#ratkaisuja-yleisiin-ongelmiin)


# Käyttöohjeet

Testien suoritusta varten:
* Varmista aluksi että olet projektin juurihakemistossa (siellä missä pyproject.toml).
* Mene virtuaaliympäristöön komennolla "poetry shell"
* Suorita testit komennolla "pytest"

Ohjelman käynnistämistä varten:
* Käynnistä ohjelma komennolla "python(3) src/komentorivisovellus.py" jos olet projektin juurihakemistossa (siellä missä pyproject.toml)
* Jos menet src-hakemistoon, voit vaan antaa komennon "python(3) komentorivisovellus.py"

Ohjelman käyttämistä varten:
* Ohjelmalla on käytössä seuraavat komennot "lisää, hae, listaa, poista, bibtex ja help"
* lisää: tämän avulla lisätään viitteet
* hae: tämän avulla haetaan yksittäiset viitteet
* listaa: tämän avulla voidaan listata kaikki viitteet
* poista: tämän avulla voidaan poistaa tietty viite
* bibtex: tulostaa annetun viitten BibTeX -muodossa
* help: tämän avulla käyttäjä saa ohjeet ohjelman käyttöä varten


