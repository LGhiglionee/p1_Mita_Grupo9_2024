import random
from Paquetes import *
def main():
    #usuario root para saltear el paso de crear un usuario.
    usuario = {
        'root': {
            'contrasena' : 'pass',
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
                tabla(combinados)
                while opcion != 8:
                    menu()
                    opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                    if opcion == 1:
                        combinados = agregar_alumno(combinados, matrizmaterias)
                    elif opcion == 2:
                        leer_alumno(dicc_alumnos)
                    elif opcion == 3:
                        actualizar_alumno(dicc_alumnos)
                    elif opcion == 4:
                        eliminar_alumno(dicc_alumnos)
                    elif opcion == 5:
                        leer_nota(dicc_notas)
                    elif opcion == 6:
                        agregar_nota(dicc_notas)
                    elif opcion == 7:
                        actualizar_nota(dicc_notas)
                    elif opcion == 8:
                        print('Saliendo...')
                    elif opcion == 9:
                        pass #arreglar mostrar
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 5.')
        
        elif opcionlog == 3:
            print('Saliendo....')
            break
        
        else:
            print()
            print('Ingreso un valor que no corresponde, repita el proceso')
            print()
main()