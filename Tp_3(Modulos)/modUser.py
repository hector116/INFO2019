def vadidaUsuario(user):
    
    if len(user)>=6 and len(user)<=12:
        return True 
    else:
        print("Nobre de usuario incorrecto..!")
    if len(user)<6:
           print("El nombre de usuario debe tener 6 o mas caracteres..!")
    else:
        if len(user)>12:
           print("El nombre de usuario no puede tener mas de 12 caracteres..! ")


def vadidaUsuario2(user):

    if (user.isalnum())==True:
        return True
    else:
        print("El nombre de usuario solo puede contener numeros y letras..!")
        
   


