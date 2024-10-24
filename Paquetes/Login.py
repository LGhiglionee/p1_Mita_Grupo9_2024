import re

def validar_mail(mail):
    # patron para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron, mail):
        return True
    else:
        return False

def validar_fecha_nacimiento(fecha_nacimiento):
    patron= r'^\d{2}/\d{2}/\d{4}$'
    if re.match(patron, fecha_nacimiento):
        return True
    else:
        return False

def registro(usuario):#registro de usuarios
    flag = 0
    while flag == 0:
        nombre_usuario = input('Ingrese su nuevo usuario: ').strip().lower()
        contrasena = input('Ingrese su nueva contrasena: ').strip()
        mail= input('Ingrese su correo electronico: ').strip().lower()
        if validar_mail(mail) == False:
            print('Correo invalido')
            flag=0
        
        if nombre_usuario in usuario:# verifica en caso de repeticion de usuarios
            if usuario[nombre_usuario]['contrasena'] == contrasena:
                print('su usuario ya cuenta con un registro')
                print()
                confirm = input('Desea cancelar su registro? [y/n]: ').lower()
                print()
                if confirm in ['y', 'yes']:
                    flag = 1
        else:
            usuario[nombre_usuario] = {'contrasena' : contrasena, 'mail' : mail}
            flag = 1    
    return usuario

def inicio (usuario):#verificacion de usuario
    ingreso = input('Ingrese su nombre de usuario o correo electrónico: ').strip().lower()
    contrasena = input('Ingrese su contraseña: ').strip()
    if "@" in ingreso and "." in ingreso: # si el ingreso contiene un "@" y un "."
        if validar_mail(ingreso) == False: #verifica que siga el patron de mail
            print('El correo electrónico ingresado no es válido.')
            return 0
    for key, valor in usuario.items():  # buscar el usuario por nombre de usuario o correo electrónico
        if key == ingreso or ('mail' in valor and valor['mail'] == ingreso):  # verifica si existe
            if valor['contrasena'] == contrasena:
                print('Login exitoso')
                return 1
            else:
                print('Contraseña incorrecta')
                return 0
    print('Usuario o correo incorrecto')
    return 0