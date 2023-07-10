def programa1():
    print("programa 1 \n.Sucesion de valores \n")
    a = 7
    b = 0
    c = 0
    b = a
    c = b
    a = a
    return a,b,c
def programa2():
    print("\n programa2.Secuencias de variables")
    a = 10
    b = 0
    aux = 0
    aux = a
    a = b
    b = aux
    return a,b,aux
def programa3():
    print("programa 3. sumar y dividir")

    A = float(input("Leer A: "))
    B = float(input("Leer B: "))
    C = float(input("Leer C: "))
        
    D = (A + B + C)/3
    DR = round(D,2)

    return  DR
def programa4():   
    print("Programa que calcula el area de un tiangulo \n")
    Base = input("Escriba el valor de la Base: ")
    Altura = input("Escriba el valor de la Altura: ")

    B = float(Base)
    A = float(Altura)

    Area = (B * A)/2
    DR = round(Area, 2)
    return DR
def programa5():
    print("Programa 5. \n Programa que calcula el perimetro del un triangulo \n")
    AB = float(input("Escriba el valor AB: "))
    BC = float(input("Escriba el valor BC: "))
    CD = float(input("Escriba el valor CD: "))
    DA = float(input("Escriba el valor DA: "))

    PR = round (AB + BC + CD + DA, 2)
    return PR
def programa6(): 
    print("Programa 6. \n Programa que calcula el area de un trapecio \n")
    Base1 = float(input("Escriba el valor de Base1 "))
    Base2 =  float(input("Escriba el valor de Base2 "))
    Altura = float(input("Escriba el valor de Altura "))

    R = ((Base1 + Base2)* Altura)/2
    RR = round(R,2)
    return RR
def programa7():    
    print("Programa 7. \n Programa que calcula el volumen de un prisma rectangular \n")
    Largo = float(input("Escriba el valor de Largo: "))
    Ancho = float(input("Escriba el valor de Ancho: "))
    Altura = float(input("Escriba el valor de Altura: "))

    Vol = Largo * Ancho * Altura
    VolR = round(Vol,4)
    return VolR
def programa8():
    print("Programa 8. \n Programa que resuelve ecuaciones \n")
    x = float(input("Escriba el valor de x: "))

    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) -5 - (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) - 5) / 7)

    print("El resultado de A es: ",round(A,2))
    print("El resultado de B es: ",round(B,2))
    print("El resultado de C es: ",round(C,2))
    print("El resultado de D es: ",round(D,2))
    print("El resultado de E es: ",round(E,2))
    print("El resultado de F es: ",round(F,2))
    return ()
def programa9():  
    print("Programa 9. \n Programa que resuelve ecuaciones \n")
    A1 = float(input("Escriba el valor de A: "))
    B1 = float(input("Escriba el valor de B: "))
    T1 = float(input("Escriba el valor de C: "))

    C1 = (4 * A1) + (3 * B1)
    C2 = (21 * A1) - 18 + (8 * B1) - 5
    C3 = (4 * A1) + (3 * B1) + 7
    C4 = (2 * A1) + (3 * B1) - (C1**5)
    C5 = (2 * A1) + (3 * B1) - (C1**2)

    print("El resultado de C1 es: ",round(C1,2))
    print("El resultado de C2 es: ",round(C2,2))
    print("El resultado de C3 es: ",round(C3,2))
    print("El resultado de C4 es: ",round(C4,2))
    print("El resultado de C5 es: ",round(C5,2))
    return ()
def programa10():    
    print("Programa 10. \n Programa de converción \n")
    metros = input("Escribir los metros: ")

    DR = float(metros)

    pies = DR * 3.28
    pulgadas = DR / 39.37

    print("El resultado de pies es: ",round(pies,1))
    print("El resultado de pulgadas es: ",round(pulgadas,1))
    return()
def programa11():
    print("Programa 11. \n Programa de la regla de tres \n")
    V1 = float(input("Escribir la primera variable: "))
    V2 = float(input("Escribir la segunda variable: "))
    V3 = float(input("Escribir la tercera variable: "))

    V4 = (V2 * V3) / V1

    print("El cuarto valor es: ",round(V4,2))
    return()
def programa12():
    print("Programa 12. \n algoritmo que calcule el interés a pagar por un préstamo \n")
    monto = float(input("Escribir el monto: "))
    tasa = float(input("Escribir la taza: "))
    plazo = float(input("Escribir el plazo: "))

    tasaporcentaje = tasa * 100
    tasamensual = tasa/12
    cuota = monto * (tasamensual / (1-(1 + tasamensual)**(-plazo)))
    interesmensual = monto * tasamensual
    capitalmensual = cuota - interesmensual

    print("imprimir cuota: ",round(cuota,2))
    print("imprimir interes: ",round(interesmensual,2))
    print("imprimir capital: ",round(capitalmensual,2))
    return()
def programa13():
    print("Programa 13. \n algoritmo para calcular el salario neto de sus empleados \n")
    salariobruto = float(input("leer el salario bruto: "))

    SeguroSocial = salariobruto * 0.0514
    SegiuroEducativo = salariobruto * 0.02
    CuotaPrestamo = 50
    Salarioneto = (salariobruto - SeguroSocial - SegiuroEducativo - CuotaPrestamo)

    print("imprimir Salarioneto: ",round(Salarioneto,2))
    return()
def programa14():
    print("Programa 14. \n algoritmo para calcular el costo de la compra de combustible \n")
    Pgasolina = float(input("Escribir el precio de la gasolina: "))
    Litros = float(input("Escribir los litros: "))

    CostoSinImpuesto = Pgasolina * Litros
    CostoTotal = CostoSinImpuesto * 1.07

    print("imprimir CostoTotal: ",round(CostoTotal,2))
    return()
def programa15():
    print("Programa 15. \n Calcular la compra de 3 articulos")

    Articulo1 = float(input("ingrese el precio del primer articulo: "))
    Articulo2 = float(input("ingrese el precio del segundo articulo: "))
    Articulo3 = float(input("ingrese el precio del tercer articulo: ")) 

    Articulos = Articulo1 + Articulo2 + Articulo3
    Impuesto = Articulos * 0.07
    TotalCompra = Impuesto + Articulos

    print("imprimir el TotalCompra: ",round(TotalCompra,2))
    return()
def programa16():
    print("Programa 16. \n algoritmo para saber la nota final \n")
    Evaluacion1 = float(input("Escribir la primera Evaluacion: "))
    Evaluacion2 = float(input("Escribir la segunda Evaluacion: "))
    Evaluacion3 = float(input("Escribir la tercera Evaluacion: "))
    Evaluacion4 = float(input("Escribir la cuarta Evaluacion: "))
    Evaluacion5 = float(input("Escribir la quinta Evaluacion: "))

    N1 = Evaluacion1 / 0.020
    N2 = Evaluacion2 / 0.015
    N3 = Evaluacion3 / 0.025
    N4 = Evaluacion4 / 0.010
    N5 = Evaluacion5 / 0.030  

    EvaFinal = (N1 + N2 + N3 +N4 +N5) / 100

    print("imprimir la EvaFinal: ",round(EvaFinal,2))
    return()
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
    return()
def programa18():
    print("Programa 18. Interes compuesto\n")

    ci = float(input("ingrese la capital inicial: "))
    i = float(input("ingrese la tasa de interes: "))
    n = float(input("Ingrese el periiodo de ahorro: "))
    cf = ci * (1 + i) ** n
    print(f"La capital final es de, {round(cf,2)}")
    return()
def programa19():
    print("Programa 19. \n Calcular la compra de 5 articulos")

    Articulo1 = float(input("ingrese el precio del primer articulo: "))
    Articulo2 = float(input("ingrese el precio del segundo articulo: "))
    Articulo3 = float(input("ingrese el precio del tercer articulo: "))
    Articulo4 = float(input("ingrese el precio del cuarto articulo: "))
    Articulo5 = float(input("ingrese el precio del quinto articulo: "))
     
    Articulossinimpuesto = Articulo1 + Articulo2 + Articulo3 + Articulo4 + Articulo5
    ArticulosconImpuesto = Articulossinimpuesto * 0.07
    promedio = (Articulossinimpuesto)/5

    print("imprimir Articulos sin impuesto: ",round(Articulossinimpuesto,2))
    print("imprimir Articulos con impuesto: ",round(ArticulosconImpuesto,2))
    print("imprimir promedio: ",round(promedio,2))
    return()
def programa20():
    print("Programa 20. \n Calcular salario neto")

    salarioBruto = float(input("Ingrese el salario bruto"))

    totalSS = salarioBruto * 0.08
    totalSE = salarioBruto * 0.02
    totalIM = salarioBruto * 0.15
    totalP = 100

    salarioNeto = (salarioBruto - totalSS - totalSE - totalIM - totalP)
                   
    print("El salario neto a pagar es: ",round(salarioNeto,2))
    return()
def programa21():
    print("Programa 21. calcular si una persona paga impuestos")

    Salario = float(input ("Escriba el salrio: "))

    if Salario > 3000:
        impuesto = Salario * 1.07
        print ("esta persona debe abonar impuestos",impuesto)
    else:
        print("No debe abonar impuestos")

    print("\n Fin del programa")
    return()
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
    return()
def programa23():
    print("programa 23. calcular la edad \n")
    edad = float(input("Escribir la edad: "))
                  
    if edad <= 18:
        print("Es un adolecente - cierto")
    else:
        print("Es un adulto - falso")

    print("\n Fin del programa")
    return()
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
    return()
def programa25():
    print ("Progrma 26.\n calculadora de descuento")

    producto = input("Escribir el nombre del producto: ")
    precio = float(input("Escribir el precio del producto: "))
    Pdescuento = float(input("Escribir el descuento a aplicar: "))

    if precio >= 50:
        porciento =  Pdescuento / 100
        descuento = precio * porciento
        preciofinal = precio - descuento
        print("El precio final del prducto es", round(preciofinal,2))
    else:
        print("¡Oferta especial!")
       
    print("\n Fin del programa")
    return()
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
    return()
def programa27():
    print("Programa 27. identificacion de un numero \n")

    value = 1
    while value <= 10:
        n1 = float(input("Ingrese un numero: "))
        if n1 > 0:
            print("El numero que a ingresado es un numero positivo ")
        if n1 < 0:
            print("El numero que ingreso es negativo ")
        if n1 == 0:
            print("El numero que a ingresado es cero ")
        print(value)
        value +=  1

    print("Fin del programa")
    return()
def programa28():
    print("Programa. \nCalificacion")

    cal = float(input("Ingrese la calificacion: "))

    if cal >= 90:
        print("La Calificacion es A")
    elif cal >= 80:
        print("La calificacion es B")
    elif cal >= 70:
        print("La calificacion es C")
    elif cal >= 60:
        print("La calificacion es D")
    else:
        print("la calificacion es F")

    print("Fin del programa")
    return()
def programa29():
    def funcion_prueba():
        print('programa 29 uso del for in range')
        for i in range(10):
            if i == 7:
                break
            print(i)
    funcion_prueba()
    return()
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
    return()
def programa31():
    print("programa 31. \n")
    value = 1
    while value < 8:    
        num = float(input("ingrese el numero: "))
        if num == 10:
          print("el programa debe acabar")   
          break
        print(value)
        value = value + 1
    print("\n Fin del programa")
    return()
def programa32():
    print("PROGRMA 32.secuencias de numeros")
    num = 1
    while num != 10:
        num += 2
        print(num)
    return()
def programa33():
    print('programa 33')
    precio = 1
    subtotal = 0

    while precio <= 5:
        articulo = float(input("Ingrese el precio del artículo " + str(precio) + ": "))
        subtotal += articulo
        precio += 1

    impuesto = subtotal * 0.07
    total = subtotal + impuesto

    print("Subtotal: ", subtotal)
    print("Impuesto (1.07): ", impuesto)
    print("Total: ", total)
    return()
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
    return()
def programa35():
    print("Programa 35. saber cuando un numero es impar o par \n")
    numeros = int(input("ingresar numero: "))

    while numeros <= 15:
        if numeros %2 == 0:
            print(f"el numero {numeros} es par")
        else:
            print(f"el numero {numeros} es impar")
        numeros += 1
    print("Fin del programa")
    return()
def programa36():
    print("programa 36. Secuencias de numeros que tengan un mensaje")
    print("--------------------------------------------------------- \n")
    for numero in range(1,11):
        if numero %2 == 0:
            print("El número", numero, "es un multiplo de 2.")
        elif numero == 5:
            print("El número", numero, "es impar y es la mitad de diez.")
        else:
            print("El número", numero, "es impar .")
            
    print("\n Fin del programa")
    return()
def programa37():
    print("programa 37. introduicir tres articulos y saber el 7% \n")
    producto = 5
    compra_total = 0

    while producto < 6:
        precio_del_producto = float(input("ingrese el precio del producto: "))
        precio_del_producto = float(input("ingrese el precio del producto: "))
        precio_del_producto = float(input("ingrese el precio del producto: "))
        precio_del_producto = float(input("ingrese el precio del producto: "))
        precio_del_producto = float(input("ingrese el precio del producto: "))
        a_impuesto = precio_del_producto * 0.07
        impuesto = a_impuesto + precio_del_producto
        compra_total += impuesto
        producto += 1
        
    print(f"El total a pagar es de {round(compra_total,2)}")

    print("\n Fin del programa")
    return()
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
    return()
def programa39():
    def suma_numeros_pares():
        print('programa 39')
        suma = 0
        n1 = 1
        while n1 != 20:
            n1 = int(input("Valor: "))
            if n1 != 0:
                if n1 % 2 == 0:
                    suma = suma + n1
        print ("La suma total de numeros pares: ",suma)
    suma_numeros_pares()
    return()
def programa40():
    print("programa 40. calcular el area de un triángulo")
    import FunciónB
    Base = float(input("escribir la base: "))
    Altura = float(input("escribir la altura: "))
    Area = FunciónB.calcular_area_triangulo(Base,Altura)    
    print(f"El area de un triangulo es", Area)
    return()









