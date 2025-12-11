#Robot testitiedosto hakutoiminnon testaamiseen

*** Settings ***
Library    ../HakuLibrary.py

*** Test Cases ***

Käyttäjä voi lisätä viitteen tietokantaan
    Create Test Env
    Set User Inputs    lisaa  Design Data Governance  journal  Khatri Vijay  Design Data Governance  2010  n  poistu
    Run Application
    Output Should Contain  Viite lisätty!
