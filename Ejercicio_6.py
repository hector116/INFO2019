tupla=(2,3,18,20,6,2,8,4,3,5,7,7,8,9,10,2)

numero=int(input("Ingrese un nro: "))
if numero in tupla:
    print("Se repite "+str(tupla.count(numero)))
else:
    print("El numero que ingreso no se encuentra en la lista")    
