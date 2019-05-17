#Pide una cadena por teclado, mete los caracteres en una 
#lista sin repetir caracteres.Operador in
lista=[]
cadena=input("Ingrese una palabra: ")

for i in cadena:
	if i not in lista:
		lista.append(i)
print(lista)



