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
programa37()
