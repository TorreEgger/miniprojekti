# Robot testitiedosto hakutoiminnon testaamiseen

*** Settings ***
Library    ../HakuLibrary.py

*** Test Cases ***

Käyttäjä Voi Filtteröidä Yhden Hakuehdon Perusteella
    Create Test Env
    Set User Inputs    hae year=2021    poistu
    Run Application
    Output Should Contain    ccc
    Output Should Contain    ddd
    Output Should Not Contain    aaa
    Output Should Not Contain    bbb

Käyttäjä Voi Filtteröidä Useamman Hakuehdon Perusteella
    Create Test Env
    Set User Inputs    hae author=kalle year=2022    poistu
    Run Application
    Output Should Contain    bbb
    Output Should Not Contain    ddd

Käyttäjä Ei Saa Tuloksia Jos Ei Löydy Vastaavia Viitteitä
    Create Test Env
    Set User Inputs    hae author=olavi    poistu
    Run Application
    Output Should Contain    Ei hakuehtoja vastaavia viitteitä