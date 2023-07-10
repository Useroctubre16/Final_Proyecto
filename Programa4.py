def programa4():   
    def area_de_un_tiangulo():
        print("Programa que calcula el area de un tiangulo \n")
        Base = input("Escriba el valor de la Base: ")
        Altura = input("Escriba el valor de la Altura: ")

        B = float(Base)
        A = float(Altura)

        Area = (B * A)/2
        DR = round(Area, 2)

        print("Imprimir: ",DR)
    area_de_un_tiangulo()
programa4()