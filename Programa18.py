def programa18():
    print("Programa 18. Interes compuesto\n")

    ci = float(input("ingrese la capital inicial: "))
    i = float(input("ingrese la tasa de interes: "))
    n = float(input("Ingrese el periiodo de ahorro: "))
    cf = ci * (1 + i) ** n
    print(f"La capital final es de, {round(cf,2)}")
programa18()
