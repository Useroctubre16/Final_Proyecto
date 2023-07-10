def programa7():    
    print("Programa 7. \n Programa que calcula el volumen de un prisma rectangular \n")
    D = input("Escriba el valor de Largo ")
    F = input("Escriba el valor de Ancho ")
    G = input("Escriba el valor de Altura ")

    Largo = float(D)
    Ancho = float(F)
    Altura = float(G)

    Vol = Largo * Ancho * Altura

    VolR = round(Vol,4)

    print("El volumen de un prisma rectangular es ",VolR )
programa7()
