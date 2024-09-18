import random
def agregar_alumno(dicc_alumnos, combinados, matrizmateria):
    while True:
        cad = input('Ingrese el legajo: ')
        if not cad.isdigit(): #Verifica que lo ingresado sea un numero
            print('El legajo debe ser un numero.')
            continue
        legajo= str(cad).zfill(9)
        legajo= int(legajo)
        if any(alumno['Legajos']== legajo for alumno in dicc_alumnos):
            print('Este legajo ya existe')
            continue
        break

    # Seleccionar una materia aleatoria
    materia = random.choice(matrizmateria)

    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    #Creacion de nuevo alumno en diccionario alumnos
    nuevo_alumno= {
        'Legajos': legajo,
        'Nombres': nombre,
        'Apellidos' : apellido,
    }
        
    # Crear nuevo alumno con datos de materia y notas iniciales en combinados
    nueva_entrada = {
        legajo,
        nombre,
        apellido,
        materia[0],  # Código de materia
        materia[1],  # Nombre de la materia
        materia[2],  # Turno
        '-',  # Parcial 1
        '-',  # Parcial 2
        '-'   # Final
    }
    dicc_alumnos.append(nuevo_alumno)
    combinados.append(nueva_entrada)

    print(f'Nuevo alumno con legajo {legajo} fue agregado.')
    return dicc_alumnos, combinados

def eliminar_alumno(dicc_alumnos, combinados):
    legajo=int(input('Ingrese el legajo del alumno a eliminar: '))
    for alumno in dicc_alumnos:
        if alumno['Legajos'] == legajo:
            dicc_alumnos.remove(alumno)
            print('Alumno eliminado correctamente.')
            break
    else:
        print('Alumno no encontrado')
        return dicc_alumnos, combinados
    combinados = [fila for fila in combinados if fila[0]!= legajo]
    print('Alumno eliminado correctamente del diccionario')
    return dicc_alumnos, combinados


def leer_alumno(dicc_alumnos):
    legajo = input('Ingrese el legajo del alumno que desea buscar: ')
    for alumno in dicc_alumnos:
        if str(alumno['Legajos']) == legajo:
            print(f"Legajo: {alumno['Legajos']}")
            print(f"Nombre: {alumno['Nombres']}")
            print(f"Apellido: {alumno['Apellidos']}")
            return
    print('No se ha encontrado el alumno con el legajo ingresado')


def actualizar_alumno(dicc_alumnos, combinados):
    legajo = input('Ingrese el legajo del alumno a actualizar: ')
    for alumno in dicc_alumnos:
        if str(alumno['Legajos']) == legajo:
            nuevo_nombre = input('Ingrese el nuevo nombre: ')
            nuevo_apellido = input('Ingrese el nuevo apellido: ')
            if nuevo_nombre:
                alumno['Nombres'] = nuevo_nombre
            if nuevo_apellido:
                alumno['Apellidos'] = nuevo_apellido
            
            # Actualizar también en combinados
            for fila in combinados:
                if str(fila[0]) == legajo:
                    if nuevo_nombre:
                        fila[1] = nuevo_nombre
                    if nuevo_apellido:
                        fila[2] = nuevo_apellido
                    break
            
            print('Datos actualizados.')
            return dicc_alumnos, combinados
    print('No se ha encontrado el alumno a actualizar')
    return dicc_alumnos, combinados

def agregar_nota(dicc_notas):
    legajo = input('Ingrese el número de legajo del alumno a calificar: ')
    
    # Buscar el alumno en dicc_notas
    for notas in dicc_notas:
        if str(notas['Legajo']) == legajo:
            
            # Ingreso y validación de la nota del parcial 1
            parcial1 = input('Ingrese la nota del parcial 1 (1-10 o "-" para no cambiar): ')
            if parcial1 != '-':
                if parcial1.isdigit() and 1 <= int(parcial1) <= 10:
                    notas['Parcial 1'] = int(parcial1)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return dicc_notas

            # Ingreso y validación de la nota del parcial 2
            parcial2 = input('Ingrese la nota del parcial 2 (1-10 o "-" para no cambiar): ')
            if parcial2 != '-':
                if parcial2.isdigit() and 1 <= int(parcial2) <= 10:
                    notas['Parcial 2'] = int(parcial2)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return dicc_notas

            # Validar si el alumno promociona o necesita nota de final
            if notas['Parcial 1'] >= 8 and notas['Parcial 2'] >= 8:
                notas['Final'] = 'Promoción'
            elif notas['Parcial 1'] <4 and notas['Parcial 2']<4:
                notas['Final'] = 'Recursa'
            else:
                final = input('Ingrese la nota del examen final (1-10 o "-" para no cambiar): ')
                if final != '-':
                    if final.isdigit() and 1 <= int(final) <= 10:
                        notas['Final'] = int(final)
                    else:
                        print('Nota inválida. Debe ser un número entre 1 y 10.')
                        return dicc_notas

            print('Las notas han sido cargadas correctamente.')
            return dicc_notas
    
    # Si no encuentra el legajo, da un mensaje de error
    print('No se ha encontrado el alumno con el legajo ingresado')
    return dicc_notas


def leer_nota(combinados):
    legajo = input('Ingrese el número de legajo del estudiante: ')
    for fila in combinados:
        if str(fila[0]) == legajo:
            print(f"Legajo: {fila[0]}")
            print(f"Nombre: {fila[1]} {fila[2]}")
            print(f"Materia: {fila[4]}")
            print(f"Parcial 1: {fila[6]}")
            print(f"Parcial 2: {fila[7]}")
            print(f"Final: {fila[8]}")
            return
    print('No se ha encontrado el alumno con el legajo ingresado')

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