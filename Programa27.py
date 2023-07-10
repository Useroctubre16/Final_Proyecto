def programa27():
    print("Programa 27. identificacion de un numero \n")

    value = 1
    while value <= 10:
        
        n1 = float(input("Ingrese un numero: "))
        if n1 > 0:
            print("El numero que a ingresado es un numero positivo ")
        if n1 < 0:
            print("El numero que ingreso es negativo ")
        if n1 == 0:
            print("El numero que a ingresado es cero ")

        print(value)
        value +=  1

    print("Fin del programa")
programa27()