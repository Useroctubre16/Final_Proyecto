def programa16():
    print("Programa 16. \n algoritmo para saber la nota final \n")
    Eva1 = input("Escribir la primera Evaluacion: ")
    Eva2 = input("Escribir la segunda Evaluacion: ")
    Eva3 = input("Escribir la tercera Evaluacion: ")
    Eva4 = input("Escribir la cuarta Evaluacion: ")
    Eva5 = input("Escribir la quinta Evaluacion: ")

    Evaluacion1 = float(Eva1)
    Evaluacion2 = float(Eva2)
    Evaluacion3 = float(Eva3)
    Evaluacion4 = float(Eva4)
    Evaluacion5 = float(Eva5)

    N1 = Evaluacion1 / 0.020
    N2 = Evaluacion2 / 0.015
    N3 = Evaluacion3 / 0.025
    N4 = Evaluacion4 / 0.010
    N5 = Evaluacion5 / 0.030  

    EvaFinal = (N1 + N2 + N3 +N4 +N5) / 100

    print("imprimir la EvaFinal: ",round(EvaFinal,2))
programa16()
