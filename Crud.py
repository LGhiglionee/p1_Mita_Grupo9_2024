def agregar_alumno(matrizalumnos):
    legajo= int(input('Ingrese el legajo: '))
    nombre= input('Ingrese el nombre: ')
    apellido= input('Ingrese el apellido: ')
    matrizalumnos.append([legajo, nombre, apellido])

def leer_alumno(matrizalumnos):
    legajo=int(input('Ingrese el legajo del alumno que desea buscar: '))
    for alumno in matrizalumnos:
        if alumno[0]==legajo:
            print(f'El alumno {alumno} ha sido encontrado.')
            return
    print('No se ha encontrado el alumno con el legajo ingresado')


def actualizar_alumno(matrizalumnos):
    legajo=int(input('Ingrese el legajo del alumno a actualizar: '))
    i= 1
    while i<len(matrizalumnos):
        if matrizalumnos[i][0]==legajo:
            nuevo_nombre=input('Ingrese el nuevo nombre: ')
            nuevo_apellido=input('Ingrese el nuevo apellido: ')
            matrizalumnos[i][1]=nuevo_nombre
            matrizalumnos[i][2]=nuevo_apellido
            print('Datos actualizados.')
            return
        i=i+1
    print('No se ha encontrado el alumno a actualizar')

def eliminar_alumno(matrizalumnos):
    legajo=int(input('Ingrese el legajo del alumno a eliminar: '))
    for alumno in matrizalumnos:
        if alumno[0]==legajo:
            matrizalumnos.remove(alumno)
            print('Alumno eliminado correctamente.')
            return
    print('Alumno no encontrado')
