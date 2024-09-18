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
    while True:
        numAlumnos = random.randint(0,30)
        print('1. No tienes usuario? Registrate')
        print('2. Iniciar Sesion')
        print('3. Salir')
        
        opcionlog = int(input('Ingrese el numero, 1-3: ' ))
        if opcionlog == 1:
            registro(usuario)
        elif opcionlog == 2:
            if inicio(usuario) == 1:
                opcion = 0
                dicc_alumnos = diccio_alumnos(numAlumnos)
                matrizmaterias = crearmatriz_materias(numAlumnos)
                dicc_notas = creardicc_notas(dicc_alumnos)    
                combinados = combinado(dicc_alumnos, matrizmaterias, dicc_notas)
                while opcion != 5:
                    menuT()
                    print()
                    opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                    if opcion == 1:
                        menuA()
                        print()
                        aux = 0
                        aux = int(input('Ingrese la acción que desee, indicando su número: '))
                        if aux != 5:
                            if aux == 1:
                                dicc_alumnos, combinados = agregar_alumno(dicc_alumnos, combinados, matrizmaterias)
                            elif aux == 2:
                                leer_alumno(dicc_alumnos)
                            elif aux == 3:
                                dicc_alumnos, combinados = actualizar_alumno(dicc_alumnos, combinados)
                            elif aux == 4:
                                dicc_alumnos, combinados = eliminar_alumno(dicc_alumnos, combinados)
                            elif aux == 5:
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
                                    matrizmaterias = agregar_materia(matrizmaterias)
                                elif aux == 2:
                                    matrizmaterias = eliminar_materia(matrizmaterias)
                                elif aux == 3:
                                    tablamatriz(matrizmaterias)
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
                                leer_nota(combinados)
                            elif aux == 2:
                                combinados = agregar_nota(combinados)
                            elif aux == 3:
                                combinados = actualizar_nota(combinados)
                            elif aux == 4:
                                print('Saliendo...')
                            else:
                                print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 4')
                            
                    elif opcion == 4:
                        combinados = combinado(dicc_alumnos, matrizmaterias, dicc_notas)
                        tabla(combinados)
                    elif opcion == 5:
                        print('Saliendo...')
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 4.')
                    
        elif opcionlog == 3:
            print('Saliendo....')
            break
        else:
            print()
            print('Ingreso un valor que no corresponde, repita el proceso')
            print()
main()