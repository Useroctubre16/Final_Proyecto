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
programa25()

