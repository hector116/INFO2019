diccionario={}

while True:	
	nom=input("Usuario: ")
	num=int(input("Teléfono: "))
	if nom in diccionario:
		print("EL USUARIO YA EXISTE".format(nom))
	else:
		diccionario[nom]=num
	n = input("¡ENTER PARA CONTINUAR, (N) PARA DETENER! ")
	if n=="N":
		break
	elif n=="n":
		break
print(diccionario)