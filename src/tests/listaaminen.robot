# Robot testaustiedosto, käyttää MiniprojektiLibrary.py-tiedostoa testien tekemiseen
# Laajenna MiniprojektiLibrary.py-tiedostoa tarpeen vaatiessa
# Käyttäjän syötteet putkena esim listaa -> y -> poistu

*** Settings ***
Library    ../HakuLibrary.py

*** Test Cases ***

Listaa Viitteet BibTeX-Muodossa
    Create Test Env
    Set User Inputs    listaa    y    poistu
    Run Application
    Output Should Contain    @inproceedings{ccc
    Output Should Contain    author = {Matti}
    Output Should Contain    title = {TestiY}
    Output Should Contain    editor = {Veikko}

Listaa Viitteet Normaali
    Create Test Env
    Set User Inputs    listaa    n    poistu
    Run Application
    Output Should Contain    viite: ccc
    Output Should Contain    author: Matti
    Output Should Contain    Editor: Veikko

Listaa Viitteet Virheinput
    Create Test Env
    Set User Inputs    listaa    a    poistu
    Run Application
    Output Should Contain    , mitään ei tulosteta