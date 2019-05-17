
meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre",
        "noviembre","diciembre")
num=int(input("Ingrese un numero: "))
print("  ")

if num<=len(meses) and num>=0:
    print("Mes: ",meses[num-1])
else:
    print("ERROR")    