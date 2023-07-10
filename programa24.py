def programa24():
    print("Programa 24. saber cual de los tres numero es mayor \n")

    a = int(input("escribir el numero: "))
    b = int(input("escribir el numero: "))
    c = int(input("escribir el numero: "))
    if a > b and a > c:
        print("el valor mayo es a: ",a)
    if b > a and b > c:
        print("el valor mayo es b: ",b)
    if c > a and c > b:
        print("el valor mayo es c: ",c) 
           
    print("\n Fin del programa")
programa24()