print("VIENVENIDO A MI MENU DE PROGRMAS ESPERO TE LLAME LA ATENCIÓN")

print("\nPrograma #1")
import funcion4
RS = funcion4.letras()
print("\n Fin del progama")

print("\n Programa #2")
import funcion4
DR = funcion4.variables()
print("\n Fin del progama")

print("\n Programa #3")
import funcion4
A = float(input("Leer A: "))
B = float(input("Leer B: "))
C = float(input("Leer C: "))
T = funcion4.numeros_variables(A,B,C)
print("\n Fin del progama")

print("\n Programa #4")
import funcion4
Base = float(input('escribir la base: '))
Altura = float(input('escribir la altura: '))
Area = funcion4.calcular_triangulo(Base,Altura)
print(Area)
print("\n Fin del progama")

print("\n Programa #5")
import funcion4
V1 = float(input("Escriba el valor AB: "))
V2 = float(input("Escriba el valor BC: "))
V3 = float(input("Escriba el valor CD: "))
V4 = float(input("Escriba el valor DA: "))
PR = funcion4.perimetro_de_un_triangulo(V1,V2,V3,V4)
print(f"El perimetro del triangulo es,{PR}")
print("\n Fin del progama")

print("\nPrograma #6")
import funcion4
Base1 = float(input("Escriba el valor de Base1 "))
Base2 = float(input("Escriba el valor de Base2 "))
Altura = float(input("Escriba el valor de Altura "))
RR = funcion4.calcula_area_de_un_trapecio(Base1,Base2,Altura)
print(f"El area de un trapecio es,{RR}")
print("\n Fin del progama")

print("\nPrograma #7")
import funcion4
Largo = float(input("Escriba el valor de Largo: "))
Ancho  = float(input("Escriba el valor de Ancho: "))
Altura = float(input("Escriba el valor de Altura: "))
VolR = funcion4.volumen_de_un_prisma_rectangular(Largo,Ancho,Altura)
print("El volumen de un prisma rectangular es ",VolR )

print("\nPrograma #8")
import funcion4
H1 = float(input("Escriba el valor de x "))
T = funcion4.resuelve_ecuaciones(H1)
print(f"El resultado de las ecuaciones es",T)
print("\n Fin del progama")

print("\nPrograma #9")
import funcion4
A1 = float(input("Escriba el valor de A "))
B1 = float(input("Escriba el valor de B "))
T1 = float(input("Escriba el valor de C "))
R = funcion4.segundas_ecuaciones(A,B,C)
print(f"El resultado de las ecuaciones es",R)
print("\n Fin del progama")

print("\nPrograma #10")
import funcion4
metros = float(input("Escribir los metros: "))
conv = funcion4.converción(metros)
print("\n Fin del progama")

print("\nPrograma #11")
import funcion4
V1 = float(input("Escribir la primera variable: "))
V2 = float(input("Escribir la segunda variable: "))
V3 = float(input("Escribir la tercera variable: "))
V4 = funcion4.regla_de_tres(V1,V2,V3)
print(f"La conversion da el resultado de",round(V4,2))
print("\n Fin del progama")

print("\nPrograma #12")
import funcion4
monto = float(input("Escribir el monto: "))
tasa = float(input("Escribir la taza: "))
plazo = float(input("Escribir el plazo: "))
totales = funcion4.calcular_cuota(monto,tasa,plazo)
print(f"la cuota por interes es,{totales}")
print("\n Fin del progama")

print("\nPrograma #13")
import funcion4
SB = float(input("leer el salario bruto: "))
SalarioN = funcion4.salario_neto_de_empleados(SB)
print(f"imprimir Salarioneto,{round(SalarioN,2)} ")
print("\n Fin del progama \U0001f606")

print("\nPrograma #14")
import funcion4
Pgasolina = float(input("Escribir el precio de la gasolina: "))
Litros = float(input("Escribir los litros: "))
CT = funcion4.compra_de_combustible(Pgasolina,Litros)
print(f"El costo total de la gasolina es, {CT}")
print("\n Fin del progama")

print("\nPrograma #15")
import funcion4
A1 = float(input("ingrese el precio del primer articulo: "))
A2 = float(input("ingrese el precio del segundo articulo: "))
A3 = float(input("ingrese el precio del tercer articulo: "))
total = funcion4.compra_de_3_articulos(A1,A2,A3)
print(f"El total de la compra es {total}")
print("\n Fin del progama")

print("\n Programa #16")
import funcion4
Eva1 = float(input("Escribir la primera Evaluacion: "))
Eva2 = float(input("Escribir la segunda Evaluacion: "))
Eva3 = float(input("Escribir la tercera Evaluacion: "))
Eva4 = float(input("Escribir la cuarta Evaluacion: "))
Eva5 = float(input("Escribir la quinta Evaluacion: "))
EvaFinal = funcion4.nota_final(Eva1,Eva2,Eva3,Eva4,Eva5)
print("imprimir la Evaluación Final: ",round(EvaFinal,2))
print("\n Fin del progama")

print("\n Programa #17")
import funcion4
Centimetros = float(input("Escriba los centimetros: "))
Metros = float(input("Escriba los metros: "))
Kilogramos = float(input("Escriba los Kilogramos: "))
Gramos = float(input("Escriba los gramos: "))
R = funcion4.converciones_medidas(Kilogramos,Metros,Gramos,Centimetros)
print("\n Fin del progama")

print("\n Programa #18")
import funcion4
ci = float(input("ingrese la capital inicial: "))
i = float(input("ingrese la tasa de interes: "))
n = float(input("Ingrese el periiodo de ahorro: "))
ct = funcion4.Interes_compuesto(ci,i,n)
print(f"el intere compuesto es, {ct}")
print("\n Fin del progama")

print("\n Programa #19")
import funcion4
ar1 = float(input("ingrese el precio del primer articulo: "))
ar2 = float(input("ingrese el precio del segundo articulo: "))
ar3 = float(input("ingrese el precio del tercer articulo: "))
ar4 = float(input("ingrese el precio del cuarto articulo: "))
ar5 = float(input("ingrese el precio del quinto articulo: "))
sucompra = funcion4.compra_de_5_articulos(ar1,ar2,ar3,ar4,ar5)
print(f"El total de su compra es, {sucompra}")
print("\n Fin del progama")

print("\n Programa #20")
import funcion4
SB = float(input("Ingrese el salario bruto: "))
salario = funcion4.programa_20(SB)
print("El salario neto a pagar es: ",round(salario,2))
print("\n Fin del progama")

print("\n Programa #21")
import funcion4
Salario = float(input ("Escriba el salrio: "))
if Salario > 3000:
    impuesto = funcion4.si_una_persona_paga_impuestos(Salario)
    print (f"esta persona debe abonar impuestos,{impuesto}")
else:
    print("No debe abonar impuestos")
print("\n Fin del programa")

print("\n Programa #22")
import funcion4
temperatura = float(input("Escriba la temperatura:"))
temperatura = funcion4.calculo_de_temperatura(temperatura)
print("\n Fin del progama")

print("\n Programa #23")
import funcion4
edad = float(input("Escribir la edad: "))
funcion4.calcular_edad(edad)
print("\n Fin del programa")

print("\n Programa #24")
import funcion4
a = int(input("escribir el numero: "))
b = int(input("escribir el numero: "))
c = int(input("escribir el numero: "))
T = funcion4.numero_es_mayor(a,b,c)
print(T)
print("\n Fin del progama")

print("\n Programa #25")
import funcion4
producto = input("Escribir el nombre del producto: ")
precio = float(input("Escribir el precio del producto: "))
Pdescuento = float(input("Escribir el descuento a aplicar: "))
H = funcion4.calculadora_de_descuento(precio,Pdescuento)
print(H)
print("\n Fin del progama")

print("\n Programa #26")
import funcion4
long1 = float(input("Ingrese la longitud del primer lado de un triangulo: "))
long2 = float(input("Ingrese la longitud del segundo lado de un triangulo: "))
long3 = float(input("Ingrese la longitud del tercer lado de un triangulo: "))
M = funcion4.casificacion_de_triangulo(long1,long2,long3)
print(M)
print("\n Fin del programa")

print("\n Programa #27")
import funcion4
value = 1
G = funcion4.identifica_numero(value)
print(G)
print("\n Fin del programa")

print("\n Programa #28")
import funcion4
cal = float(input("Ingrese la calificacion: "))
nota =  funcion4.notas(cal)
print(nota)
print("\n Fin del programa")

print("\n Programa #29")
import funcion4
print('programa 29 uso del for in range')
E = funcion4.funcion_prueba()
print(E)
print("\n Fin del programa")

print("\n Programa #30")
import funcion4
Value = 1
Y = funcion4.programa30(Value)
print(Y)
print("\n Fin del programa")

print("\n Programa #31")
import funcion4
value = 1
S = funcion4.programa31(value)
print(S)
print("\n Fin del programa") 

print("\n Programa #32")
import funcion4
num = 1
D = funcion4.programa32(num)
print(D)
print("\n Fin del programa")

print("\n Programa #33")
import funcion4
precio = 1
subtotal = 0
Resultado = funcion4.articulo_precio(precio,subtotal)
print(Resultado)
print("\n Fin del programa")

print("\n Programa #34")
import funcion4
a = 0
b = 0
c = 0
NUMEROS = 4
Q= funcion4.tresnumeroesmayor(NUMEROS)
print(Q)  
print("\n Fin del programa")

print("\n Programa #35")
import funcion4
numeros = int(input("ingresar numero: "))
A = funcion4.es_impar_par(numeros)
print(A)
print("\n Fin del programa")

print("\n Programa #36")
import funcion4
B = funcion4.numeros_con_mensaje()
print(B)
print("\n Fin del programa")

print("\n Programa #37")
import funcion4
producto = 5
compra_total = 0
F = funcion4.articulos_saber_el_7(producto,compra_total)
print(F)
print("\n Fin del programa")

print("\n Programa #38")
import funcion4
AB = float(input("Escriba el valor AB: "))
BC = float(input("Escriba el valor BC: "))
CD = float(input("Escriba el valor CD: "))
DA = float(input("Escriba el valor DA: "))
PR = funcion4.perimetro_de_un_triangulo(AB,BC,CD,DA)
print(f"El perimetro del triangulo es,{PR}")
print("\n Fin del progama")

print("\n Programa #39")
import funcion4
suma = 0
n1 = 1
P = funcion4.suma_numeros_pares(n1,suma)
print(P)
print("\n Fin del progama")

print("\n Programa #40")
import funcion4
Base = float(input("escribir la base: "))
Altura = float(input("escribir la altura: "))
Area = funcion4.calcular_area_triangulo(Base,Altura)
print(f"El area de un triangulo es", Area)
print("\n Fin del progama")

print("\n GRACIAS POR VER MIS CODIGOS \U00031F609")




