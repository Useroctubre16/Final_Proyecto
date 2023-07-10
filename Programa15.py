def programa15():
    print("Programa 15. \n Calcular la compra de 3 articulos")

    A1 = input("ingrese el precio del primer articulo: ")
    A2 = input("ingrese el precio del segundo articulo: ")
    A3 = input("ingrese el precio del tercer articulo: ")
     
    Articulo1 = float(A1)
    Articulo2 = float(A2)
    Articulo3 = float(A3)

    Articulos = Articulo1 + Articulo2 + Articulo3
    Impuesto = Articulos * 0.07
    TotalCompra = Impuesto + Articulos

    print("imprimir el TotalCompra: ",round(TotalCompra,2))
programa15()
