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
    opcionlog = 0
    while opcionlog != 3:
        print('1. No tienes usuario? Registrate')
        print('2. Iniciar Sesion')
        print('3. Salir')
        
        opcionlog = int(input('Ingrese el numero, 1-3: ' ))
        
        if opcionlog == 1:
            registro(usuario)
        elif opcionlog == 2:
            if inicio(usuario) == 1:
                numAlumnos = random.randint(1,30)
                dicc_alumnos = creardicc_alumnos(numAlumnos)
                dicc_materias = creardicc_materias()
                matriz_combinada = combinado(dicc_alumnos, dicc_materias)
                opcion = 0
                while opcion != 5:
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
                                dicc_alumnos, matriz_combinada = actualizar_alumno(dicc_alumnos, matriz_combinada)
                            elif aux == 4:
                                dicc_alumnos, matriz_combinada = eliminar_alumno(dicc_alumnos, matriz_combinada)
                            elif aux == 5:
                                matriz_combinada, dicc_materias= asignar_materias(dicc_alumnos, dicc_materias, matriz_combinada)
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
                                    tabladicc(dicc_materias)
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
                        matriz_combinada = combinado(dicc_alumnos, dicc_materias)
                        tabla(matriz_combinada)
                    elif opcion == 5:
                        print('Saliendo...')
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 4.')
                    
        elif opcionlog == 3:
            print('Saliendo....')
        else:
            print()
            print('Ingreso un valor que no corresponde, repita el proceso')
            print()
main()