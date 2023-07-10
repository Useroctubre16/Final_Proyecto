def programa38():
    print("Programa 38. calcular el perimetro de un triangulo \n")

    import FunciónB

    V1 = input("Escriba el valor AB: ")
    V2 = input("Escriba el valor BC: ")
    V3 = input("Escriba el valor CD: ")
    V4 = input("Escriba el valor DA: ")

    AB = float(V1)
    BC = float(V2)
    CD = float(V3)
    DA = float(V4)

    PR = FunciónB.perimetro_de_un_triangulo(AB,BC,CD,DA)
    print(f"El perimetro del triangulo es,{PR}")

    print("\n Fin del progama")
programa38()