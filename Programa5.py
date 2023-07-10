def programa5():
    print("Programa 5. \n Programa que calcula el perimetro del un triangulo \n")
    V1 = input("Escriba el valor AB: ")
    V2 = input("Escriba el valor BC: ")
    V3 = input("Escriba el valor CD: ")
    V4 = input("Escriba el valor DA: ")

    AB = float(V1)
    BC = float(V2)
    CD = float(V3)
    DA = float(V4)

    PR = (AB + BC + CD + DA)
    PR = round(AB + BC + CD + DA, 2)

    PR = AB + BC + CD + DA
    PR = round(PR)

    print("El area de un rectangulo es:",PR)
programa5()