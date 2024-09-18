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
                while opcion != 12:
                    menu()
                    opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                    if opcion == 1:
                        dicc_alumnos, combinados = agregar_alumno(dicc_alumnos,combinados, matrizmaterias)
                    elif opcion == 2:
                        leer_alumno(dicc_alumnos)
                    elif opcion == 3:
                        dicc_alumnos, combinados = actualizar_alumno(dicc_alumnos, combinados)
                    elif opcion == 4:
                        dicc_alumnos, combinados =eliminar_alumno(dicc_alumnos, combinados)
                    elif opcion == 5:
                        leer_nota(combinados)
                    elif opcion == 6:
                        combinados = agregar_nota(combinados)
                    elif opcion == 7:
                        combinados=actualizar_nota(combinados)
                    elif opcion == 8:
                         tabla(combinados)
                    elif opcion == 9:
                        tablamatriz(matrizmaterias)
                    elif opcion == 10:
                        matrizmaterias = agregar_materia(matrizmaterias)
                    elif opcion == 11:
                        matrizmaterias = eliminar_materia(matrizmaterias)
                    elif opcion == 12:
                        print('Saliendo...')
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 9.')
        elif opcionlog == 3:
            print('Saliendo....')
            break
        else:
            print()
            print('Ingreso un valor que no corresponde, repita el proceso')
            print()
main()