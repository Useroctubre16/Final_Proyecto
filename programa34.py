def programa34():
    print("Programa 34. saber cual de los tres numero es mayor \n")
    a = 0
    b = 0
    c = 0
    NUMEROS = 4
    while NUMEROS <=4:
        a = int(input("escribir el numero: "))
        b = int(input("escribir el numero: "))
        c = int(input("escribir el numero: "))
        if a > b and a > c:
           print("el valor mayo es a: ",a)
        if b > a and b > c:
           print("el valor mayo es b: ",b)
        if c > a and c > b:
           print("el valor mayo es c: ",c)
           NUMEROS = 1
           break
    print(f"El numero mayor es",{a,b,c})  
    print("\n Fin del programa")
programa34()