import random
from Paquetes import *
def main():
    #usuario root para saltear el paso de crear un usuario.
    usuario = {
        'root': {
            'contrasena' : 'pass',
            'mail' : 'root@gmail.com'
                }
        }
    numAlumnos = random.randint(1,30)
    dicc_alumnos = creardicc_alumnos(numAlumnos)
    dicc_materias = creardicc_materias()
    matriz_combinada = combinado(dicc_alumnos, dicc_materias)
    opcionlog = 0
    while opcionlog != 3:
        try:
            print('1. No tienes usuario? Registrate')
            print('2. Iniciar Sesion')
            print('3. Salir')
                
            opcionlog = int(input('Ingrese el numero, 1-3: ' ))
                
            if opcionlog == 1:
                registro(usuario)
            elif opcionlog == 2:
                if inicio(usuario) == 1:
                    print()
                    opcion = 0
                    while opcion != 6:
                        try:
                            menuT()
                            print()
                            opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                            if opcion == 1:
                                menuA()
                                print()
                                aux = 0
                                aux = int(input('Ingrese la acción que desee, indicando su número: '))
                                if aux != 6:
                                    if aux == 1:
                                        dicc_alumnos, matriz_combinada = agregar_alumno(dicc_alumnos, matriz_combinada, dicc_materias)
                                    elif aux == 2:
                                        leer_alumno(dicc_alumnos)
                                    elif aux == 3:
                                        dicc_alumnos= actualizar_alumno(dicc_alumnos)
                                    elif aux == 4:
                                        dicc_alumnos, matriz_combinada = eliminar_alumno(dicc_alumnos, matriz_combinada)
                                    elif aux== 5:
                                        matriz_combinada = asignarmateria(matriz_combinada, dicc_alumnos, dicc_materias)
                                    elif aux == 6:
                                        print('Saliendo...')
                                    else:
                                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 5')
                            elif opcion == 2:
                                menuM()
                                print()
                                aux = 0
                                aux = int(input('Ingrese la acción que desee, indicando su número: '))
                                if aux != 4:
                                    if aux == 1:
                                        dicc_materias = agregar_nueva_materia(dicc_materias)
                                    elif aux == 2:
                                        dicc_materias, matriz_combinada = eliminar_materia(dicc_materias, matriz_combinada)
                                    elif aux == 3:
                                        tablaMateria(dicc_materias)
                                    elif aux == 4:
                                        print('Saliendo...')
                                    else:
                                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 4')
                            elif opcion == 3:
                                menuN()
                                print()
                                aux = 0
                                aux = int(input('Ingrese la acción que desee, indicando su número: '))
                                if aux != 4:
                                    if aux == 1:
                                        leer_nota(matriz_combinada, dicc_alumnos)
                                    elif aux == 2:
                                        matriz_combinada = agregar_nota(matriz_combinada, dicc_alumnos)
                                    elif aux == 3:
                                        matriz_combinada = actualizar_nota(matriz_combinada, dicc_alumnos)
                                    elif aux == 4:
                                        print('Saliendo...')
                                    else:
                                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 4')
                                            
                            elif opcion == 4:
                                aux = input('¿Desea ordenar de manera ascendente los alumnos? [y/n]: ').lower()
                                if aux in ['y', 'yes']:
                                    matriz_ordenada = [matriz_combinada[0]] + sorted(matriz_combinada[1:], key=lambda x: x[0])
                                    tabla(matriz_ordenada)
                                else:
                                    tabla(matriz_combinada)
                            elif opcion == 5:
                                menuP()
                                print()
                                aux= int(input('Ingrese la accion que desee: '))
                                if aux != 3:
                                    if aux == 1:
                                        Promedio(matriz_combinada, dicc_alumnos, dicc_materias)
                                    elif aux == 2:
                                        Promedio_todas_Materias(matriz_combinada, dicc_alumnos)
                                    elif aux == 3:
                                        print('saliendo...')
                                    else:
                                        print('Ingrese un numero valido')
                            elif opcion == 6:
                                print('Saliendo...')
                            else:
                                print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 4.')
                        except ValueError:
                                print('Porfavor debe ingresar un numero, no un caracter.')
                                print('Volviendo al menu...')
                elif opcionlog == 3:
                    print('Saliendo....')
                else:
                    print()
                    print('Ingreso un valor que no corresponde, repita el proceso')
                    print()
        except ValueError:
            print('Porfavor, debe ingresar un numero y del rango pedido (1-3), no un caracter')
            print()

main()