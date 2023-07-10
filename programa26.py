def programa26():
    print("Programa 27. \n clasificación de un triángulo")

    long1 = float(input("Ingrese la longitud del primer lado de un triangulo: "))
    long2 = float(input("Ingrese la longitud del segundo lado de un triangulo: "))
    long3 = float(input("Ingrese la longitud del tercer lado de un triangulo: "))

    if (long1 == long2 and long1 == long3):
       print("El triángulos es equilatero")
       
    elif (long2 == long1 or long2 == long3 or long2 == long3):
       print("El triángulo es isosceles")
       
    else:
        print("El triangulo es escaleno")
        
    print("\n Fin del programa")
programa26()
