def programa22():   
    print("Programa 22. calculo de temperatura")

    temperatura = float(input("Escriba la temperatura:"))

    if temperatura < 20:
        if temperatura <10:
            print("Nivel Azul")
        else:
            print("Nivel Verde")
    else:
        if temperatura < 30:
            print("Nivel Naranja")
        else:
            print("Nivel Rojo")
programa22()            
