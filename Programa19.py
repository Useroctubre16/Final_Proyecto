def programa19():
    print("Programa 19. \n Calcular la compra de 5 articulos")

    A1 = input("ingrese el precio del primer articulo: ")
    A2 = input("ingrese el precio del segundo articulo: ")
    A3 = input("ingrese el precio del tercer articulo: ")
    A4 = input("ingrese el precio del cuarto articulo: ")
    A5 = input("ingrese el precio del quinto articulo: ")
     
    Articulo1 = float(A1)
    Articulo2 = float(A2)
    Articulo3 = float(A3)
    Articulo4 = float(A4)
    Articulo5 = float(A5)

    Articulossinimpuesto = Articulo1 + Articulo2 + Articulo3 + Articulo4 + Articulo5
    ArticulosconImpuesto = Articulossinimpuesto * 0.07
    promedio = (Articulossinimpuesto)/5

    print("imprimir Articulos sin impuesto: ",round(Articulossinimpuesto,2))
    print("imprimir Articulos con impuesto: ",round(ArticulosconImpuesto,2))
    print("imprimir promedio: ",round(promedio,2))
programa19()