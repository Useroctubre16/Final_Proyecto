def programa13():
    print("Programa 13. \n algoritmo para calcular el salario neto de sus empleados \n")
    SB = input("leer el salario bruto: ")

    salariobruto = float(SB)

    SeguroSocial = salariobruto * 0.0514
    SegiuroEducativo = salariobruto * 0.02
    CuotaPrestamo = 50

    Salarioneto = (salariobruto - SeguroSocial - SegiuroEducativo - CuotaPrestamo)

    print("imprimir Salarioneto: ",round(Salarioneto,2))
programa13()