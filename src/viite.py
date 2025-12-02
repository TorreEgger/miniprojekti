class Viite:
    def __init__(self, viite, viitetyyppi, author, title, year, 
        booktitle=None, journal=None, volume=None, pages=None, publisher=None):
        self.viite = viite
        self.viitetyyppi = viitetyyppi
        self.author = author
        self.title = title
        self.year = year
        self.booktitle = booktitle
        self.journal = journal
        self.volume = volume
        self.pages = pages
        self.publisher = publisher

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

        lines.append("}")

        return "\n".join(lines)
