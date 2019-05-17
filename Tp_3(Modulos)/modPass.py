def longPass(contraseña):

    if len(contraseña)>=8:
        return True
    else:
        print("La contraseña debe tener al menos 8 caracteres..!")    

def minusculas(contraseña):
    minuscula=False

    for i in contraseña:
        if i.islower()==True:
            minuscula=True

    if minuscula==True:
        return True
    else:
        print("La contraseña debe tener al menos una minuscula..!")        

def mayusculas(contraseña):
    mayuscula=False
    
    for i in contraseña:
        if i.isupper()==True:
            mayuscula=True

    if mayuscula==True:
        return True
    else:
        print("La contraseña debe tener al menos una mayuscula..!")            

def numeros(contraseña):
    numero=False

    for i in contraseña:
        if i.isdigit()==True:
            numero=True
    
    if numero==True:
        return True
    else:
        print("La contraseña debe tener al menos un número..!")

def caracter(contraseña):
    caracter=False

    for i in contraseña:
        if i.isalnum()==False:
            caracter=True
    
    if caracter==False:
        print("La contraseña debe tener al menos un caracter especial..!")
    else:
        return True

def espacio(contraseña):
    espacio=False

    for i in contraseña:
        if i.isspace()==True:
            espacio = True
    
    if espacio==True:
        print("La contraseña no puede tener espacios en blanco..!")
    else:
        return True    
