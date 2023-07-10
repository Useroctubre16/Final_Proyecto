def programa12():
    print("Programa 12. \n algoritmo que calcule el interés a pagar por un préstamo \n")
    M = input("Escribir el monto: ")
    T = input("Escribir la taza: ")
    P = input("Escribir el plazo: ")

    monto = float(M)
    tasa = float(T)
    plazo = float(P)

    tasaporcentaje = tasa * 100
    tasamensual = tasa/12
    cuota = monto * (tasamensual / (1-(1 + tasamensual)**(-plazo)))
    interesmensual = monto * tasamensual
    capitalmensual = cuota - interesmensual

    print("imprimir cuota: ",round(cuota,2))
    print("imprimir interes: ",round(interesmensual,2))
    print("imprimir capital: ",round(capitalmensual,2))
programa12()
