from Crud import agregar_alumno, eliminar_alumno, leer_alumno, actualizar_alumno
from Matrices import crearmatriz_alumnos, random 
from Diseno import mostrarmatriz_ordenada

cantalum = random.randint(0,30)

def main ():
    print('1. Agregar alumno')
    print('2. Leer alumno')
    print('3. Actualizar alumno')
    print('4. Eliminar alumno')
    print('5. Salir')

opcion= 0
matrizalumnos= crearmatriz_alumnos(cantalum)

while opcion !=5:
    mostrarmatriz_ordenada(matrizalumnos)
    main()
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
        print('Saliendo...')
    else:
        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 5.')
    #Se podria usar un try por si no se pone un numero
