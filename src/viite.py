class Viite:
    def __init__(self, viite, viitetyyppi, author, title, year, 
        booktitle=None, journal=None, volume=None, pages=None, publisher=None, lisakentat=None):
        self.viite = viite
        self.viitetyyppi = viitetyyppi
        self.author = author
        self.title = title
        self.year = year
        self.booktitle = booktitle          #
        self.journal = journal              #  nämä voitaisiin varmaan lisätä
        self.volume = volume                #  myös lisänkenttiin, jätän
        self.pages = pages                  #  ne toistaiseksi tähän, kun ne 
        self.publisher = publisher          #  ovat vielä käytössä muualla koodissa
        if lisakentat is None:
            self.lisakentat = {}
        else:
            self.lisakentat = lisakentat
    def merkkijonoksi(self):
        #kaikille yhteiset kentät
        lines = [f"viite: {self.viite}",
                 f"type: {self.viitetyyppi}",
                 f"author: {self.author}",
                 f"title: {self.title}",
                 f"year: {self.year}"]
        
        #varmistetaan taaksepäin yhteensopivuus
        if self.journal:
            lines.append(f"journal: {self.journal}")
        if self.booktitle:
            lines.append(f"booktitle: {self.booktitle}")
        if self.volume:
            lines.append(f"volume: {self.volume}")
        if self.pages:
            lines.append(f"pages: {self.pages}")
        if self.publisher:
            lines.append(f"publisher: {self.publisher}")

        #lisäkentät
        if self.lisakentat:
            for key, value in self.lisakentat.items():
                lines.append(f"{key}: {value}")

        #nivotaan yhteen uusille riveille
        return "\n".join(lines)
    
    def to_bibtex(self):
        lines = [f"@{self.viitetyyppi}{{{self.viite},",
                 f"    author = {{{self.author}}},",
                 f"    title = {{{self.title}}},"
                 ]
        #tehdään tarkistukset valinnaisille kentille
        if self.journal:
            lines.append(f"    journal = {{{self.journal}}},")

        lines.append(f"    year = {{{self.year}}},")
        if self.booktitle:
            lines.append(f"    booktitle = {{{self.booktitle}}}")
        if self.volume:
            lines.append(f"    volume = {{{self.volume}}}")

        if self.pages:
            lines.append(f"    pages = {{{self.pages}}}")
        if self.publisher:
            lines.append(f"    publisher = {{{self.publisher}}}")

        if self.lisakentat:
            for key, value in self.lisakentat.items():
                lines.append(f"    {key} = {{{value}}}")

        lines.append("}")

        return "\n".join(lines)
