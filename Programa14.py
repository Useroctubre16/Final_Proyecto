def programa14():
    print("Programa 14. \n algoritmo para calcular el costo de la compra de combustible \n")
    PG = input("Escribir el precio de la gasolina: ")
    L = input("Escribir los litros: ")

    Pgasolina = float(PG)
    Litros = float(L)

    CostoSinImpuesto = Pgasolina * Litros
    CostoTotal = CostoSinImpuesto * 1.07

    print("imprimir CostoTotal: ",round(CostoTotal,2))
programa14()
