def programa30():
    Value = 1
    while Value <=5:
        print(Value)
        c1 = float(input("Ingrese la calificacion: "))

        if c1 >= 90:
            print("La Calificacion es A")
        elif c1 >= 80:
            print("La calificacion es B")
        elif c1 >= 70:
            print("La calificacion es C")
        elif c1 >= 60:
            print("La calificacion es D")
        else:
            print("la calificacion es F")
        Value += 1

    print("\n Fin del programa")
programa30()