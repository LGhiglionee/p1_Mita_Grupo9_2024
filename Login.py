def registro(usuario):#registro de usuarios

    user = input('ingrese su nuevo usuario: ')
    contra = input('ingrese su nueva contra: ')

    usuario[user] = {'contrasena' : contra}
        
    print(usuario)
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