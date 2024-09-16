import random
from Paquetes import *

cantalum = random.randint(0,30 )
def main():
    #usuario root para saltear el paso de crear un usuario.
    usuario = {
        'root': {
            'contrasena' : 'pass',
        }
        }
    while True:
        print('1. No tienes usuario? Registrate')
        print('2. Iniciar Sesion')
        print('3. Salir')
        opcionlog = int(input('Ingrese el numero, 1-3: ' ))
        if opcionlog == 1:
            registro(usuario)
        elif opcionlog == 2:
            if inicio(usuario) == 1:
                opcion = 0
                
                matrizalumnos = crearmatriz_alumnos(cantalum)
                matrizmaterias = crearmatriz_materias()
                matriznotas = crearmatriz_notas(matrizalumnos)    
                combinados = combinado(matrizalumnos, matrizmaterias, matriznotas)
                while opcion != 8:
                    encabezados(combinados)
                    menu()
                    opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                    if opcion == 1:
                        combinados = agregar_alumno(combinados, matrizmaterias)
                    elif opcion == 2:
                        leer_alumno(matrizalumnos)
                    elif opcion == 3:
                        actualizar_alumno(matrizalumnos)
                    elif opcion == 4:
                        eliminar_alumno(matrizalumnos)
                    elif opcion == 5:
                        leer_nota(matriznotas)
                    elif opcion == 6:
                        agregar_nota(matriznotas)
                    elif opcion == 7:
                        actualizar_nota(matriznotas)
                    elif opcion == 8:
                        print('Saliendo...')
                    elif opcion == 9:
                        mostrar(combinado)
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 5.')
                    #Se podria usar un try por si no se pone un numero
        
        elif opcionlog == 3:
            print('Saliendo....')
            break
        else:
            print()
            print('Ingreso un valor que no corresponde, repita el proceso')
            print()
main()