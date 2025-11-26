# Miniprojekti
Ryhmän 6 toteuttama miniprojekti

Projektin backlog: https://jyu-my.sharepoint.com/:x:/g/personal/kirskaxt_jyu_fi/IQAegL_ux5ZjSpN1c-rVZH4CAadPDwjwBHSxYaUqLI5SDEg?e=omyNjP

# Definition Of Done (DOD)

Jotta voimme määrittää jonkun vaatimuksen olevan valmis, seuraamme seuraavaa listausta:
* Se on suunniteltu tarkoin. Tarkoittaen, että se on sirpaloitu eri tehtäviksi ja sen olemassaolo on tärkeää koko ohjelmalle.
* Ohjelmakoodi: Koodi on selkeää, nimeämiskäytänteen mukaista ja Pylint ei anna virheilmoituksia.
* Testaus: Ohjelmakoodia on testattu yksikkötesteillä (ja ne menevät läpi) sekä myöskin automatisoiduilla testeillä (nekin menevät läpi).
* Dokumentaatio: Kirjoitetut toiminnallisuudet on oltava dokumentoitu selkeästi, jotta muutkin kuin kirjoittaja(t) pystyvät sitä ymmärtämään.
* Integraatio: Toiminallisuuksien tulee olla integroitu ohjelmistoon ja ne eivät saa olla ristiriidassa keskenään.
* Tuotantoon vieminen: Lopuksi koodi tulee viedä säilöön! Jos toteutusta on tehty eri haarassa kuin (main/master), niin tulee tehdä merge näiden eri haarojen välille.

# Asennusohjeet

Varmista ensin nämä asiat: 
* Pythonista vähintään versio (3.14). Jos ei ole, niin asenna täältä uusi (https://www.python.org/downloads/)
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
