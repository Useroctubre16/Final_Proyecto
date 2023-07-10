def programa10():    
    print("Programa 10. \n Programa de converción \n")
    metros = input("Escribir los metros: ")

    DR = float(metros)

    pies = DR * 3.28
    pulgadas = DR / 39.37

    print("El resultado de pies es: ",round(pies,1))
    print("El resultado de pulgadas es: ",round(pulgadas,1))
programa10()