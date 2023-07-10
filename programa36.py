def programa36():
    print("programa 36. Secuencias de numeros que tengan un mensaje")
    print("--------------------------------------------------------- \n")
    for numero in range(1,11):
        if numero %2 == 0:
            print("El número", numero, "es un multiplo de 2.")
        elif numero == 5:
            print("El número", numero, "es impar y es la mitad de diez.")
        else:
            print("El número", numero, "es impar .")
            
    print("\n Fin del programa")
programa36()