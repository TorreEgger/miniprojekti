from database import Database
from viite import Viite


def kysy_viite():
    print("Syötä uuden viitteen tiedot: ")
    viite = input("viite ").strip()
    tyyppi = input("tyyppi").strip()
    author = input("kirjoittaja").strip()
    title = input("Otsikko").strip()
