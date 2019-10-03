while True:

    respuesta = input("Quieres continuar? Si/No ")
    if respuesta.lower() == "si":
        print (respuesta)
    if respuesta.lower() == "no":
        print ("Adiós.")
        break
    else:
        print ("No te he entendido.")
        (respuesta)