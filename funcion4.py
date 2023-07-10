def letras():
    a = 7
    b = 0
    c = 0
    b = a
    c = b
    a = a
    print(a, b, c)
def variables():
    a = 10
    b = 0
    aux = 0
    aux = a
    a = b
    b = aux
    print(a,b,aux)
def numeros_variables(A,B,C):
    D = (A + B + C)/3
    print(D) 
def calcular_triangulo(Base,Altura):
    c = (Base * Altura) / 2
    return c
def perimetro_de_un_triangulo(V1,V2,V3,V4):
     PR = (V1 + V2 + V3 + V4)
     return PR
def calcula_area_de_un_trapecio(Base1,Base2,Altura):
    R = ((Base1 + Base2)* Altura)/2
    return(R)
def volumen_de_un_prisma_rectangular(Largo,Ancho,Altura):
    Vol = Largo * Ancho * Altura
    return(Vol)
def resuelve_ecuaciones(x):
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) -5 - (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) - 5) / 7)
    return (A,B,C,D,E,F)
def segundas_ecuaciones(A,B,C):
    C1 = (4 * A) + (3 * B)
    C2 = (21 * A) - 18 + (8 * B) - 5
    C3 = (4 * A) + (3 * B) + 7 
    C4 = (2 * A) + (3 * B) - (C**5) 
    C5 = (2 * A) + (3 * B) - (C**2)
    return (A,B,C)
def converción(metros):
    pies = metros * 3.28
    pulgadas = metros / 39.37
    print(pies,pulgadas)
def regla_de_tres(V1,V2,V3):
    V4 = (V2 * V3) / V1
    return(V4)

def calcular_cuota(tasa,monto,plazo):
    tasaporentaje = tasa * 100
    tasamensual = tasa/12
    c = monto * (tasamensual / (1-(1 + tasamensual)**(-plazo)))
    im = monto * tasamensual
    cm = c - im
    return(c,im,cm)
def salario_neto_de_empleados(salariobruto):
    SS = salariobruto * 0.0514
    SE = salariobruto * 0.02
    CP = 50
    SN = (salariobruto - SS - SE - CP)
    return(SN)
def compra_de_combustible(Pgasolina,Litros):
    CostoSinImpuesto = Pgasolina * Litros
    CostoTotal = CostoSinImpuesto * 1.07
    return(CostoTotal)
def compra_de_3_articulos(Articulo1,Articulo2,Articulo3):
    Articulos = Articulo1 + Articulo2 + Articulo3
    Impuesto = Articulos * 0.07
    TotalCompra = Impuesto + Articulos
    return(TotalCompra)
def nota_final(Evalu1,Evalu2,Evalu3,Evalu4,Evalu5):
    N1 = Evalu1 / 0.020
    N2 = Evalu2 / 0.015
    N3 = Evalu3 / 0.025
    N4 = Evalu4 / 0.010
    N5 = Evalu5 / 0.030  
    EvaF = (N1 + N2 + N3 +N4 +N5) / 100
    return(EvaF)
def converciones_medidas(Kilogramos,Metros,Gramos,Centimetros):
    g = Kilogramos / 0.001
    Kg = Gramos / 1000
    cm = Metros / 0.01
    m = Centimetros/100
    print(g,Kg,cm,m)
def Interes_compuesto(ci,i,n):
    cf = ci * (1 + i) ** n
    return(cf)
def compra_de_5_articulos(Art1,Art2,Art3,Art4,Art5):
    Articulossinimpuesto = Art1 + Art2 + Art3 + Art4 + Art5
    ArticulosconImpuesto = Articulossinimpuesto * 0.07
    promedio = (Articulossinimpuesto)/5
    return(ArticulosconImpuesto,promedio)
def programa_20(salarioBruto):
    totalSS = salarioBruto * 0.08
    totalSE = salarioBruto * 0.02
    totalIM = salarioBruto * 0.15
    totalP = 100
    salarioNeto = (salarioBruto - totalSS - totalSE - totalIM - totalP)
    return(salarioNeto)
def si_una_persona_paga_impuestos(Salario):
    impuesto = Salario * 1.07
    print(impuesto)
def calculo_de_temperatura(temperatura):
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
def calcular_edad(edad):
    if edad <= 18:
        print("Es un adolecente - cierto")
    else:
        print("Es un adulto - falso")
def numero_es_mayor(a,b,c):
    if a > b and a > c:
        print("el valor mayo es a: ",a)
    if b > a and b > c:
        print("el valor mayo es b: ",b)
    if c > a and c > b:
        print("el valor mayo es c: ",c) 
    return()
def calculadora_de_descuento(precio,Pdescuento):
    if precio >= 50:
        porciento =  Pdescuento / 100
        descuento = precio * porciento
        preciofinal = precio - descuento
        print("El precio final del prducto es", round(preciofinal,2))
    else:
        print("¡Oferta especial!")
    return()
def casificacion_de_triangulo(long1,long2,long3):
    if (long1 == long2 and long1 == long3):
       print("El triángulos es equilatero")
    elif (long2 == long1 or long2 == long3 or long2 == long3):
       print("El triángulo es isosceles")
    else:
        print("El triangulo es escaleno")
    return()
def identifica_numero(value):
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
    return()
def notas(cal):
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
    return()
def funcion_prueba():
    for i in range(10):
        if i == 7:
            break
        print(i)
    return()
def programa30(Value):
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
    return()
def programa31(value):
    while value < 8:
        num = float(input("ingrese el numero: "))
        if num == 10:
          print("el programa debe acabar")   
          break
        print(value)
        value = value + 1
    return()
def programa32(num):
    while num != 10:
        num += 2
        print(num)
        break
    return()
def articulo_precio(precio,subtotal):
    while precio <= 5:
        articulo = float(input("Ingrese el precio del artículo: " + str(precio) + ": "))
        subtotal += articulo
        precio += 1
    impuesto = subtotal * 0.07
    total = subtotal + impuesto
    return(impuesto,total, subtotal)
def tresnumeroesmayor(NUMEROS):
    while NUMEROS <= 4:
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
    return()
def es_impar_par(numeros):
    while numeros <= 15:
        if numeros %2 == 0:
            print(f"el numero {numeros} es par")
        else:
            print(f"el numero {numeros} es impar")
        numeros += 1
    return()
def numeros_con_mensaje():
    for numero in range(1,11):
        if numero %2 == 0:
            print("El número", numero, "es un multiplo de 2.")
        elif numero == 5:
            print("El número", numero, "es impar y es la mitad de diez.")
        else:
            print("El número", numero, "es impar .")
    return()
def articulos_saber_el_7(producto,compra_total):
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
    return(compra_total,a_impuesto,impuesto)
def perimetro_de_un_triangulo(AB,BC,CD,DA):
     PR = (AB + BC + CD + DA)
     return PR
def suma_numeros_pares(n1,suma):
    while n1 != 20:
        n1 = int(input("Valor: "))
        if n1 != 0:
            if n1 % 2 == 0:
                suma = suma + n1           
    return(suma)
def calcular_area_triangulo(Base,Altura):
    c = (Base * Altura)/2
    return c