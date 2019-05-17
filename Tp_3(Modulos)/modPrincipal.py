from modUser import *
from modPass import *



while True:
    user=input(">>USUARIO: ")

    if vadidaUsuario(user)==True and vadidaUsuario2(user)==True:
    
        break
    else:

        print("Vueleva ingrese el usuario")


while True:
    passw=input(">>Introduce la contraseña: ")

    if longPass(passw)==True\
         and mayusculas(passw)==True\
         and minusculas(passw)==True\
         and numeros(passw)==True\
         and caracter(passw)==True\
         and espacio(passw)==True:

        break
    else:
        print("Vuelva ingresar su contraseña")

print(">>Bienvenido:",user)





