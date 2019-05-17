#Ejercicio n°4
lista=[]
num=int(input("Ingrese un numero: "))
while num!=0:
    lista.append(num)
    num=int(input("Ingrese un numero: "))

lista2=sorted(lista)  
print(lista2)    
