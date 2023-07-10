def programa11():
    print("Programa 11. \n Programa de la regla de tres \n")
    A = input("Escribir la primera variable: ")
    B = input("Escribir la segunda variable: ")
    C = input("Escribir la tercera variable: ")

    V1 = float(A)
    V2 = float(B)
    V3 = float(C)

    V4 = (V2 * V3) / V1

    print("El cuarto valor es: ",round(V4,2))
programa11()