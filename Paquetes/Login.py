import re

def validar_mail(mail):
    # Patrón para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, mail) is not None

def registro(usuario):#registro de usuarios
    flag = 0
    while flag == 0:
        nombre_usuario = input('ingrese su nuevo usuario: ').strip().lower()
        contrasena = input('ingrese su nueva contra: ').strip()
        mail= input('Ingrese su correo electronico: ').strip().lower()

        if validar_mail(mail) == None:
            print('Correo invalido')
            
        
        if nombre_usuario in usuario:# verifica en caso de repeticion de usuarios
            if usuario[nombre_usuario]['contrasena'] == contrasena:
                print('su usuario ya cuenta con un registro')
                print()
                confirm = input('Desea cancelar su registro? [y/n]: ')
                print()
                if confirm.lower in ['y', 'yes']:
                    flag = 1
        else:
            usuario[nombre_usuario] = {'contrasena' : contrasena, 'mail' : mail}
            flag = 1    
    return usuario

def inicio (usuario):#verificacion de usuario
    ingreso = input('Ingrese su nombre de usuario o correo electrónico: ').strip().lower()
    contrasena = input('Ingrese su contraseña: ').strip()
    if "@" in ingreso and "." in ingreso: # si el ingreso contiene un "@" y un "."
        if not validar_mail(ingreso): #verifica que siga el patron de mail
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