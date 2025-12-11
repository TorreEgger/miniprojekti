# https://dl.acm.org/doi/10.1145/2380552.2380613
# https://dl.acm.org/doi/10.5555/3721488.3721494
# https://dl.acm.org/doi/10.1145/3711083

from bs4 import BeautifulSoup # type: ignore
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore


def acmhaku(acm):
    if acm.startswith("https://dl.acm.org/doi/10."): 
        options = Options()
        #options.add_argument("--headless")
        dr = webdriver.Chrome(options)
        dr.get(acm)
        #dr.get('https://dl.acm.org/doi/10.1145/2380552.2380613')
        bs = BeautifulSoup(dr.page_source,"html.parser")
        # otsikko
        title1 = str(bs.title)
        title2 = title1.replace("<title>", "").replace("</title>", "")
        title3 = title2.partition("|")
        title = title3[0]
        # tekijät
        tagGN = bs.find_all("span", property="givenName")
        authorGN = str(tagGN)
        author1GN = authorGN.replace('<span property="givenName">', "").replace("</span>", "").replace("[", "").replace("]", "")
        author1GN = author1GN.split(',')
        tagFN = bs.find_all("span", property="familyName")
        authorFN = str(tagFN)
        author1FN = authorFN.replace('<span property="familyName">', "").replace("</span>", "").replace("[", "").replace("]", "")
        author1FN = author1FN.split(',')
        i = 0
        l = (len(author1GN))/2
        authors = []
        while i < l:
            authors.append(author1GN[i] + " " + author1FN[i])
            i = i + 1
            continue
        # vuosi
        vuosi = bs.find_all("span", class_="core-date-published")
        vuosi1 = str(vuosi)
        vuosi2 = vuosi1.replace("</span>]", "")
        year = vuosi2[-4:]
        # sivumäärä
        sivut = bs.find("span", property="pageStart")
        sivut1 = str(sivut)
        sivut2 = sivut1.replace('<span property="pageStart">', "").replace("</span>", "")
        sivut3 = bs.find("span", property="pageEnd")
        sivut4 = str(sivut3)
        sivut5 = sivut4.replace('<span property="pageEnd">', "").replace("</span>", "")
        if sivut2 == sivut5:
            pages = sivut2
        else:
            pages = sivut2 + "-" + sivut5
        # volyymi
        volyme = "ACM"
        # lehti
        lehti1 = title3[2]
        lehti = lehti1[1:]

        return title, authors, year, pages, volyme, lehti

    else:
        print("")
        print("Anna kunnollinen ACM-linkki.")
        return 0