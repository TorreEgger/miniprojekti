#Robot-testitiedosto viitteen poistamisen testaamiseen

*** Settings ***
Library    ../HakuLibrary.py

*** Test Cases ***

Käyttäjä saa virheilmoituksen epäonnistuneesta poistosta
    Create Test Env
    Set User Inputs  poista  abc  poistu
    Run Application
    Output Should Contain  Poistettavaa viitettä ei löytynyt

Käyttäjä pystyy poistamaan viitteen tietokannasta
    Create Test Env
    Set User Inputs  poista  aaa  poistu
    Run Application
    Output Should Contain  Viite poistettu
