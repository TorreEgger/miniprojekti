while True:
    kasky = input("Anna käsky: ")
    # print(kasky)
    
    if kasky == "poistu":
        break
    
    # Viitteiden lisääminen
    if kasky == "a":
        print("1")
        print("")
        continue

    # Tallennettujen viitteiden listaaminen
    if kasky == "b":
        print("2")
        print("")
        continue

    # Tallennettujen viitteiden poistaminen tietokannasta
    if kasky == "c":
        print("3")
        print("")
        continue

    # Yksittäisen viitteen hakeminen listasta
    if kasky == "d":
        print("4")
        print("")
        continue

    else:
        print("Anna kunnollinen käsky.")
        print("")