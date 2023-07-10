def programa20():
    print("Programa 20. \n Calcular salario neto")

    SB = input("Ingrese el salario bruto")

    salarioBruto = float(SB)

    totalSS = salarioBruto * 0.08
    totalSE = salarioBruto * 0.02
    totalIM = salarioBruto * 0.15
    totalP = 100

    salarioNeto = (salarioBruto - totalSS - totalSE - totalIM - totalP)
                   
    print("El salario neto a pagar es: ",round(salarioNeto,2))
programa20()