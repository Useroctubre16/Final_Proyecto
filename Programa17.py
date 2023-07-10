def programa17():
    print("Programa 17. hacer conversiones de unidades de medida \n")

    Centimetros = float(input("Escriba los centimetros: "))
    Metros = float(input("Escriba los metros: "))
    Kilogramos = float(input("Escriba los Kilogramos: "))
    Gramos = float(input("Escriba los gramos: "))

    g = Kilogramos / 0.001
    Kg = Gramos / 1000
    cm = Metros / 0.01
    m = Centimetros/100

    print("El total de las conversiones es \n", round (g,2))
    print("El total de las conversiones es \n",round(Kg,2))
    print("El total de las conversiones es \n",round(cm,2))
    print("El total de las conversiones es \n",round(m,2))
programa17()