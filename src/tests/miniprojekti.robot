# Robot testaustiedosto, käyttää MiniprojektiLibrary.py-tiedostoa testien tekemiseen
# Laajenna MiniprojektiLibrary.py-tiedostoa tarpeen vaatiessa
# Käyttäjän syötteet putkena esim listaa -> y -> poistu

*** Settings ***
Library    ../MiniprojektiLibrary.py

*** Test Cases ***

Listaa Viitteet BibTeX-Muodossa
    Create Test Project
    Set User Inputs    listaa    y    poistu
    Run Application
    Output Should Contain    @inproceedings{abc
    Output Should Contain    author = {Kalle}
    Output Should Contain    title = {Testi}

Listaa Viitteet Normaali
    Create Test Project
    Set User Inputs    listaa    n    poistu
    Run Application
    Output Should Contain    viite: abc
    Output Should Contain    author: Kalle

Listaa Viitteet Virheinput
    Create Test Project
    Set User Inputs    listaa    a    poistu
    Run Application
    Output Should Contain    , mitään ei tulosteta