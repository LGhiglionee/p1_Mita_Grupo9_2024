import random
def agregar_alumno(combinado, matrizmateria):
    legajo = int(input('Ingrese el legajo: '))
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    
    # Seleccionar una materia aleatoria
    materia = random.choice(matrizmateria)
    
    # Crear nuevo alumno con datos de materia y notas iniciales
    nuevo_alumno = {
        'Legajos': legajo,
        'Nombres': nombre,
        'Apellidos': apellido,
        'Turnos': materia['Turnos'],
        'Materias': materia['Materias'],
        'Código': materia['Código'],
        'Parcial 1': '-',
        'Parcial 2': '-',
        'Final': '-'
    }
    
    combinado.append(nuevo_alumno)
    return combinado

def eliminar_alumno(a, b, c):
    legajo=int(input('Ingrese el legajo del alumno a eliminar: '))
    for borro in range(a):
        if str(a[borro][0])==str(legajo):
            a.pop(borro)
            print('Alumno eliminado correctamente.')
            return
    print('Alumno no encontrado') #CHEQUEAR PORQUE NO FUNCIONA
    return


def leer_alumno(x):
    legajo=int(input('Ingrese el legajo del alumno que desea buscar: '))
    for alumno in x:
        if alumno[0]==legajo:
            print(f'El alumno {alumno} ha sido encontrado.')
            return
    print('No se ha encontrado el alumno con el legajo ingresado')


def actualizar_alumno(x):
    legajo=int(input('Ingrese el legajo del alumno a actualizar: '))
    for i in range(1,len(x)):
        if str(x[i][0])== str(legajo):
            nuevo_nombre=input('Ingrese el nuevo nombre: ')
            nuevo_apellido=input('Ingrese el nuevo apellido: ')
            x[i][1]=nuevo_nombre
            x[i][2]=nuevo_apellido
            print('Datos actualizados.')
            return
    print('No se ha encontrado el alumno a actualizar')



def agregar_nota(matriznotas):
    legajo = int(input('Ingrese el número de legajo del alumno a calificar: '))
    codigo = int(input('Ingrese el código de la materia: '))
    parcial1 = int(input('Ingrese la nota del parcial 1: '))

    if parcial1 >= 1 and parcial1 <= 10:
        parcial2_input = input('Ingrese la nota del parcial 2 (o presione Enter para dejar en blanco): ')
        if parcial2_input.strip() == '':
            parcial2 = '-'
        else:
            parcial2 = int(parcial2_input)
            if parcial2 < 1 or parcial2 > 10:
                print('La nota del parcial 2 debe estar entre 1 y 10.')
                return

        if parcial1 >= 8 and parcial2 >= 8:
            final = 'Eximido'
            print('El alumno se ha eximido del examen final.')
        else:
            final = int(input('Ingrese la nota del examen final: '))
            if final < 1 or final > 10:
                print('La nota del examen final debe estar entre 1 y 10.')
                return

        matriznotas.append([legajo, codigo, parcial1, parcial2, final])
        print('Las notas han sido cargadas.')
    else:
        print('La nota del parcial 1 debe estar entre 1 y 10.')

def leer_nota(matriznotas):
    legajo = input('Ingrese el número de legajo del estudiante: ')
    notas_alumno = list(filter(lambda x: x[0] == legajo, matriznotas[1:]))
    if notas_alumno:
        for nota in notas_alumno:
            print(nota)
    else:
        print('No se ha encontrado el alumno con el legajo ingresado')
        return

def actualizar_nota(matriznotas):
    legajo = int(input('Ingrese el legajo del alumno para actualizar su nota: '))
    codigo = int(input('Ingrese el código de la materia: '))
    i = 1
    while i < len(matriznotas):
        if matriznotas[i][0] == legajo and matriznotas[i][1] == codigo:
            parcial1 = int(input('Ingrese la nueva nota del parcial 1: '))
            parcial2 = int(input('Ingrese la nueva nota del parcial 2: '))
            if parcial1 >= 8 and parcial2 >= 8:
                print('El alumno se ha eximido del examen final.')
                matriznotas[i][2] = parcial1
                matriznotas[i][3] = parcial2
                matriznotas[i][4] = 'Promocion'
            else:
                nuevo_final = int(input('Ingrese la nueva nota del final: '))
                matriznotas[i][2] = parcial1
                matriznotas[i][3] = parcial2
                matriznotas[i][4] = nuevo_final
            print('Notas actualizadas')
            return
        i += 1
    print('No se ha encontrado el alumno a actualizar')