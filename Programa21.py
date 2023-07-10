def programa21():
    print("Programa 21. calcular si una persona paga impuestos")

    Salario = float(input ("Escriba el salrio: "))

    if Salario > 3000:
        impuesto = Salario * 1.07
        print ("esta persona debe abonar impuestos",impuesto)
    else:
        print("No debe abonar impuestos")

    print("\n Fin del programa")
programa21()