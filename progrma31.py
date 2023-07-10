def programa31():
    print("programa 31. \n")
    value = 1
    while value < 8:    
        num = float(input("ingrese el numero: "))
        if num == 10:
          print("el programa debe acabar")   
          break
        print(value)
        value = value + 1
    print("\n Fin del programa") 
programa31()