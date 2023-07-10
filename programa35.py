def programa35():
    print("Programa 35. saber cuando un numero es impar o par \n")
    numeros = int(input("ingresar numero: "))

    while numeros <= 15:
        if numeros %2 == 0:
            print(f"el numero {numeros} es par")
        else:
            print(f"el numero {numeros} es impar")
        numeros += 1
    print("Fin del programa")
programa35()
    