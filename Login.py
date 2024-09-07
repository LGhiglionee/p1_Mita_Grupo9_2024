def registro(usuario):#registro de usuarios

    nombre_usuario = input('ingrese su nuevo usuario: ')
    contrasena = input('ingrese su nueva contra: ')

    usuario[nombre_usuario] = {'contrasena' : contrasena}
    
    if nombre_usuario in usuario:# verifica en caso de repeticion de usuarios
        if usuario[nombre_usuario]['contrasena'] == contrasena:
            print('su usuario ya cuenta con un registro')
            
    return usuario


def inicio (usuario):#verificacion de usuario
    nombre_usuario= input('Ingrese tu nombre de usuario: ')
    contrasena= input('Ingrese tu contraseña: ')
    
    if nombre_usuario in usuario:#verifica su el nombre del input esta en el dicc
        if usuario[nombre_usuario]['contrasena'] == contrasena:# ahora con el nombre busca la contra
            print('Login exitoso')
            print()
            return 1
        else:
            return print('Contraseña incorrecta')
    else:
        return print('Usuario incorrecto')