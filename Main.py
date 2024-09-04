from Crud import agregar_alumno, eliminar_alumno, leer_alumno, actualizar_alumno, leer_nota, agregar_nota, actualizar_nota
from Matrices import crearmatriz_alumnos, random , crearmatriz_materias , crearmatriz_notas
from Diseno import mostrarmatrizalumnos_ordenada, menu, mostrarmatriznotas_ordenada, mostrarmatrizmaterias_ordenada
from Login import inicio, registrar_usuario

cantalum = random.randint(0,30)
cantmat=60

def main():
    usuario= {}
    while True:
        print('1. No tienes usuario? Registrate')
        print('2. Iniciar Sesion')
        print('3. Salir')
        opcionlog=int(input('Ingrese el numero, 1-3: ' ))
        if opcionlog == 1:
            registrar_usuario(usuario)
        elif opcionlog == 2:
            if inicio(usuario)==1:
                opcion= 0
                matrizalumnos= crearmatriz_alumnos(cantalum)
                matrizmaterias= crearmatriz_materias(cantmat)
                matriznotas= crearmatriz_notas(matrizalumnos, matrizmaterias)    
                while opcion !=8:
                    mostrarmatrizalumnos_ordenada(matrizalumnos)
                    print()
                    mostrarmatrizmaterias_ordenada(matrizmaterias)
                    print()
                    mostrarmatriznotas_ordenada(matriznotas)
                    menu()
                    opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                    if opcion == 1:
                        agregar_alumno(matrizalumnos)
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
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 5.')
                    #Se podria usar un try por si no se pone un numero

        elif opcionlog == 3:
            print('Saliendo....')
            break

main()