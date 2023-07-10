def programa6(): 
    print("Programa 6. \n Programa que calcula el area de un trapecio \n")
    A = input("Escriba el valor de Base1 ")
    B = input("Escriba el valor de Base2 ")
    C = input("Escriba el valor de Altura ")

    Base1 = float(A)
    Base2 = float(B)
    Altura = float(C)

    R = ((Base1 + Base2)* Altura)/2

    RR = round(R,2)

    print("El area de un trapecio es ", RR)
programa6()