import random

def agregar_alumno(dicc_alumnos, combinados, matrizmateria):
    """Agrega un nuevo alumno al sistema con legajo, nombre y materia aleatoria."""
    while True:
        cad = input('Ingrese el legajo: ')
        if not cad.isdigit():
            print('El legajo debe ser un número.')
            continue
        legajo = str(cad.zfill(9)) #Llena de 0 el legajo
        break

    materia = random.choice(matrizmateria)
    nombre = input('Ingrese el nombre: ').title()
    apellido = input('Ingrese el apellido: ').title()

    nuevo_alumno = {
        'Legajos': legajo,
        'Nombres': nombre,
        'Apellidos': apellido,
    }

    nueva_ingreso = [
        legajo,
        nombre,
        apellido,
        materia[0],  # código materia
        materia[1],  # nombre materia
        materia[2],  # turno
        '-',  # parcial 01
        '-',  # parcial 02
        '-'   # final
    ]

    dicc_alumnos.append(nuevo_alumno)
    combinados.append(nueva_ingreso)

    print(f'Nuevo alumno con legajo {legajo} fue agregado.')
    return dicc_alumnos, combinados

def eliminar_alumno(dicc_alumnos, combinados):
    """Elimina un alumno del sistema por su número de legajo."""
    legajo=int(input('Ingrese el legajo del alumno a eliminar: '))
    for alumno in dicc_alumnos:
        if alumno['Legajos'] == legajo:
            dicc_alumnos.remove(alumno) 
            print('Alumno eliminado correctamente.')
            break
    else:
        print('Alumno no encontrado')
        return dicc_alumnos, combinados
    combinados = [fila for fila in combinados if fila[0]!= legajo] #borra al legajo puesto, y se queda con los otros
    print('Alumno eliminado correctamente del diccionario')
    return dicc_alumnos, combinados


def leer_alumno(dicc_alumnos):
    """Muestra la información de un alumno por su número de legajo."""
    legajo = input('Ingrese el legajo del alumno que desea buscar: ')
    for alumno in dicc_alumnos: 
        if str(alumno['Legajos']) == legajo: #se fija el que tenga el mismo legajo
            print(f"Legajo: {alumno['Legajos']}")
            print(f"Nombre: {alumno['Nombres']}")
            print(f"Apellido: {alumno['Apellidos']}")
            return
    print('No se ha encontrado el alumno con el legajo ingresado')


def actualizar_alumno(dicc_alumnos, combinados):
    """Actualiza el nombre y apellido de un alumno existente."""
    legajo = input('Ingrese el legajo del alumno a actualizar: ')
    for alumno in dicc_alumnos:
        if str(alumno['Legajos']) == legajo:
            nuevo_nombre = input('Ingrese el nuevo nombre: ').title()
            nuevo_apellido = input('Ingrese el nuevo apellido: ').title()
            if nuevo_nombre:
                alumno['Nombres'] = nuevo_nombre
            if nuevo_apellido:
                alumno['Apellidos'] = nuevo_apellido
            
            #actualizar también en combinados
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

def agregar_nota(combinados):
    """Agrega o actualiza las notas de un alumno para una materia específica."""
    
    legajo = input('Ingrese el número de legajo del alumno a calificar: ')
    
    for alumno in combinados[1:]:  #emmpieza  desde el índice 1 para saltar el encabezado
        if str(alumno[0]) == legajo: 
            print(f"Alumno: {alumno[1]} {alumno[2]}")
            print(f"Materia: {alumno[4]}")
            
            parcial1 = input('Ingrese la nota del parcial 1 (1-10 o "-" para no cambiar): ')
            if parcial1 != '-':
                if parcial1.isdigit() and 1 <= int(parcial1) <= 10:
                    alumno[6] = int(parcial1)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return combinados

            parcial2 = input('Ingrese la nota del parcial 2 (1-10 o "-" para no cambiar): ')
            if parcial2 != '-':
                if parcial2.isdigit() and 1 <= int(parcial2) <= 10:
                    alumno[7] = int(parcial2)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return combinados

            # convierte a enteros para la comparación, si no son '-'
            parcialuno= int(alumno[6]) if alumno[6] != '-' else 0
            parcialdos = int(alumno[7]) if alumno[7] != '-' else 0

            if parcialuno >= 8 and parcialdos >= 8:
                alumno[8] = 'Promoción'
            elif parcialuno < 4 and parcialdos < 4:
                alumno[8] = 'Recursa'
            else:
                final = input('Ingrese la nota del examen final (1-10 o "-" para no cambiar): ')
                if final != '-':
                    if final.isdigit() and 1 <= int(final) <= 10:
                        alumno[8] = int(final)
                    else:
                        print('Nota inválida. Debe ser un número entre 1 y 10.')
                        return combinados

            print('Las notas han sido cargadas correctamente')
            return combinados
    
    print('No se ha encontrado el alumno con el legajo ingresado')
    return combinados

def leer_nota(combinados):
    legajo = input('Ingrese el número de legajo del estudiante: ').strip()
    for fila in combinados:
        if str(fila[0]) == legajo: #busca el legajo, e imprime toda su informacion
            print(f"Legajo: {fila[0]}")
            print(f"Nombre: {fila[1]} {fila[2]}")
            print(f"Materia: {fila[4]}")
            print(f"Parcial 1: {fila[6]}")
            print(f"Parcial 2: {fila[7]}")
            print(f"Final: {fila[8]}")
            return
    print('No se ha encontrado el alumno con el legajo ingresado')


def actualizar_nota(combinados):
    legajo = input("Ingrese el legajo del alumno: ")
    for fila in combinados[1:]:
        if str(fila[0]) == legajo:
            print(f"Alumno: {fila[1]} {fila[2]}")
            print(f"Materia: {fila[4]}")
            print(f"Notas actuales: Parcial 1: {fila[6]}, Parcial 2: {fila[7]}, Final: {fila[8]}")

            parcial1 = input("Ingrese la nueva nota del parcial 1 (1-10 o '-' para no cambiar): ")
            if parcial1 != '-':
                if parcial1.isdigit() and 1 <= int(parcial1) <= 10:
                    fila[6] = int(parcial1)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return combinados

            parcial2 = input("Ingrese la nueva nota del parcial 2 (1-10 o '-' para no cambiar): ")
            if parcial2 != '-':
                if parcial2.isdigit() and 1 <= int(parcial2) <= 10:
                    fila[7] = int(parcial2)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return combinados

            if fila[6] != '-' and fila[7] != '-':
                if int(fila[6]) >= 8 and int(fila[7]) >= 8:
                    fila[8] = 'Promoción'
                elif int(fila[6]) < 4 and int(fila[7]) < 4:
                    fila[8] = 'Recursa'
                else:
                    final = input('Ingrese la nueva nota del examen final (1-10 o "-" para no cambiar): ')
                    if final != '-':
                        if final.isdigit() and 1 <= int(final) <= 10:
                            fila[8] = int(final)
                        else:
                            print('Nota inválida. Debe ser un número entre 1 y 10.')
                            return combinados

            print("Notas actualizadas con éxito")
            return combinados

    print("El legajo no existe")
    return combinados

def agregar_materia(matrizmaterias):
    codigo= int(input('Ingrese el codigo de la materia: '))
    nombre = input('Ingrese el nombre de la materia: ').capitalize().strip()
    turno = input('Ingrese el turno en el que se dicta: ').capitalize().strip()
    nuevasmat = [codigo,nombre,turno]

    matrizmaterias.append(nuevasmat)
    return matrizmaterias

def eliminar_materia(matrizmaterias):
    codigo = int(input('Ingrese el codigo de la materia a eliminar: '))
    for materia in matrizmaterias:
        if materia[0] == codigo:

            matrizmaterias.remove(materia)
            
            print(f'La materia con codigo {codigo} ha sido eliminada')
            return matrizmaterias
    print('No se encontro ninguna materia con dicho codigo')