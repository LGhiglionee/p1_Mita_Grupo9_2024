import random

def agregar_alumno(dicc_alumnos, matriz_combinada, dicc_materias):
    flag = 1
    while flag == 1:
        cad = input('Ingrese el legajo: ')
        if not cad.isdigit():
            print('El legajo debe ser un número.')
        else:
            legajo = str(cad.zfill(9))  # llena de 0 el legajo
            flag = 0
    
    nombre = input('Ingrese el nombre: ').title()
    apellido = input('Ingrese el apellido: ').title()
    dicc_alumnos[legajo] = [nombre, apellido] #agrega alumno a dicc alumnos

    entrada = input('Desea asignar una nueva materia a este alumno? [y/n] ').lower()
    
    while entrada not in ['y', 'n', 'yes', 'no']:
        entrada = input('Recuerde ingresar las opciones que ve en pantalla [y/n]: ').lower()

    if entrada == 'y' or 'yes':
        aux = 1
        while aux == 1:
            for codigo in sorted(dicc_materias.keys()):
                print(f'Codigo: {codigo}, Materia: {dicc_materias[codigo][1]}, Turno: {dicc_materias[codigo][0]}') #muestra materias disponibles

            codigoI = int(input('Ingrese código de la nueva materia: '))
            if codigoI in dicc_materias.keys(): #chequea si existe tal codigo
                nuevo_ingreso = [
                    legajo,
                    codigoI,  # pone el codigo de la mat
                    '-',  # parcial 1
                    '-',  # parcial 2
                    '-'   # final
                ]
                matriz_combinada.append(nuevo_ingreso)  # pone el nuevo alumno en la matriz combinada
                aux = 0
                print(f'Materia {dicc_materias[codigoI][1]} asignada correctamente.')
            else:
                print('No se encontró el código, intente nuevamente.')
        
    elif entrada == 'n' or 'no': #si pone que no, no asigna materia
        nuevo_ingreso = [
            legajo,
            '',  # sin materia
            '-',  # parcial 1
            '-',  # parcial 2
            '-'   # final
        ]
        matriz_combinada.append(nuevo_ingreso)

    print(f'Nuevo alumno con legajo {legajo} fue agregado.')
    return dicc_alumnos, matriz_combinada


def eliminar_alumno(dicc_alumnos, matriz_combinada):
    legajo = int(input('Ingrese el legajo del alumno a eliminar: '))
    if legajo in dicc_alumnos :
        dicc_alumnos.pop(legajo)
        print(f'Alumno con legajo {legajo} eliminado.')

        filas_a_eliminar = []
        for fila in matriz_combinada[1:]:  # Slice para que no tome los encabezados
            if fila[0] == legajo:
                filas_a_eliminar.append(fila) #junta todas las filas que tenga ese legajo
        for fila in filas_a_eliminar:
            matriz_combinada.remove(fila) #borra
            print('filas elimindas correctamente de la matriz.')
    else:
        print('El legajo ingresado no existe.')
    
    return dicc_alumnos , matriz_combinada


def leer_alumno(dicc_alumnos):
    encontrado = 0
    legajo = int(input('Ingrese el legajo del alumno que desea buscar: '))
    for alumno in dicc_alumnos.keys():
        if alumno == legajo:
            print('El alumno ha sido encontrado')
            print('Datos del alumnos: ', end=' ')
            print(f'Legajo: {legajo}, Nombre: {dicc_alumnos[legajo][0]}, Apellido: {dicc_alumnos[legajo][1]}')
            encontrado= 1
    if encontrado == 0:
        print('No se encontro el alumno')
    return


def actualizar_alumno(dicc_alumnos, matriz_combinada):

    legajo = int(input('Ingrese el legajo del alumno a actualizar: '))
    for alumno in dicc_alumnos.keys():
        if alumno == legajo:
            nuevo_nombre = input('Ingrese el nuevo nombre: ').title()
            nuevo_apellido = input('Ingrese el nuevo apellido: ').title()
            if nuevo_apellido and nuevo_nombre:
                dicc_alumnos[legajo] = [nuevo_nombre, nuevo_apellido]
            flag = 1
            #actualizar también en combinados
            while flag == 1:
                for fila in matriz_combinada [1:]:
                    if fila[0] == legajo:
                        fila[1] = nuevo_nombre
                        fila[2] = nuevo_apellido
                        flag = 0
            print('Datos actualizados.')
            return dicc_alumnos, matriz_combinada
    print('No se ha encontrado el alumno a actualizar')
    return dicc_alumnos, matriz_combinada

def agregar_nota(matriz_combinada, dicc_alumnos):
    
    legajo = int(input('Ingrese el número de legajo del alumno a calificar: '))
    
    for alumno in matriz_combinada[1:]:  # empieza desde el índice 1 para saltar el encabezado
        if int(alumno[0]) == legajo: 
            print(f"Alumno: {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]}")
            
            # Nota del Parcial 1
            parcial1 = input('Ingrese la nota del parcial 1 (1-10 o "-" para no cambiar): ')
            if parcial1 != '-':
                if parcial1.isdigit() and 1 <= int(parcial1) <= 10:
                    alumno[2] = int(parcial1)  # actualiza nota de parcial 1
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return matriz_combinada

            # Nota del Parcial 2
            parcial2 = input('Ingrese la nota del parcial 2 (1-10 o "-" para no cambiar): ')
            if parcial2 != '-':
                if parcial2.isdigit() and 1 <= int(parcial2) <= 10:
                    alumno[3] = int(parcial2)  # actualiza nota de parcial 2
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return matriz_combinada

            parcialuno = alumno[2] if alumno[2] != '-' else 0
            parcialdos = alumno[3] if alumno[3] != '-' else 0

            if parcialuno >= 8 and parcialdos >= 8: #se fija si promociona o recursa
                alumno[4] = 'Promoción'
            elif parcialuno < 4 and parcialdos < 4:
                alumno[4] = 'Recursa'
            else:
                final = input('Ingrese la nota del examen final (1-10 o "-" para no cambiar): ')
                if final != '-':
                    if final.isdigit() and 1 <= int(final) <= 10:
                        alumno[4] = int(final)
                    else:
                        print('Nota inválida. Debe ser un número entre 1 y 10.')
                        return matriz_combinada

            print('Las notas han sido cargadas correctamente')
            return matriz_combinada
    
    print('No se ha encontrado el alumno con el legajo ingresado')
    return matriz_combinada


def leer_nota(matriz_combinada, dicc_alumnos):
    legajo = int(input('Ingrese el número de legajo del estudiante: '))
    for fila in matriz_combinada [1:]:
        if int(fila[0]) == legajo: #busca el legajo, e imprime toda su informacion
            print(f"Legajo: ", fila[0])
            print(f"Nombre y apellido: {dicc_alumnos[legajo][0]},' ',{dicc_alumnos[legajo][1]}")
            print(f'Codigo Materia: ', fila[1])
            print(f"Parcial 1: ", fila[2])
            print(f"Parcial 2: ", fila[3])
            print(f"Final: ", fila[4])
            return
    print('No se ha encontrado el alumno con el legajo ingresado')


def actualizar_nota(matriz_combinada, dicc_alumnos):
    legajo = int(input("Ingrese el legajo del alumno: "))
    for fila in matriz_combinada[1:]:
        if int(fila[0]) == legajo:
            print(f"Nombre y apellido: {dicc_alumnos[legajo][0]},' ',{dicc_alumnos[legajo][1]}")
            print(f"Materia: ", fila[1])
            print(f"Notas actuales: Parcial 1: ",fila[2], "Parcial 2: " , fila[3] , "Final: " ,fila[4])

            parcial1 = input("Ingrese la nueva nota del parcial 1 (1-10 o '-' para no cambiar): ")
            if parcial1 != '-':
                if parcial1.isdigit() and 1 <= int(parcial1) <= 10:
                    fila[2] = int(parcial1)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return matriz_combinada

            parcial2 = input("Ingrese la nueva nota del parcial 2 (1-10 o '-' para no cambiar): ")
            if parcial2 != '-':
                if parcial2.isdigit() and 1 <= int(parcial2) <= 10:
                    fila[3] = int(parcial2)
                else:
                    print('Nota errónea. Debe ser un número entre 1 y 10.')
                    return matriz_combinada

            if fila[2] != '-' and fila[3] != '-':
                if int(fila[2]) >= 8 and int(fila[3]) >= 8:
                    fila[4] = 'Promoción'
                elif int(fila[2]) < 4 and int(fila[3]) < 4:
                    fila[4] = 'Recursa'
                else:
                    final = input('Ingrese la nueva nota del examen final (1-10 o "-" para no cambiar): ')
                    if final != '-':
                        if final.isdigit() and 1 <= int(final) <= 10:
                            fila[4] = int(final)
                        else:
                            print('Nota inválida. Debe ser un número entre 1 y 10.')
                            return matriz_combinada

            print("Notas actualizadas con éxito")
            return matriz_combinada

    print("El legajo no existe")
    return matriz_combinada

def agregar_nueva_materia(dicc_materias):
    flag = 0
    nuevo_codigo = int(input('Ingrese el codigo de la nueva materia: '))
    for mat in dicc_materias.keys():
        if mat == nuevo_codigo:
            print('El codigo ya existe')
            flag = 1
    if flag == 0:
        nuevo_nombre = input('Ingrese el nombre de la materia: ').strip().capitalize()
        turno= input('Ingrese el turno que se da la materia: ').strip().capitalize()
        dicc_materias[nuevo_codigo] = [nuevo_nombre, turno]



def eliminar_materia(dicc_materias, matriz_combinada):
    codigo = int(input('Ingrese el codigo de la materia a eliminar: '))
    if codigo in dicc_materias :
        dicc_materias.pop(codigo)
        print(f'La materia con codigo {codigo} ha sido eliminada.')

        filas_a_eliminar = []
        for fila in matriz_combinada[1:]:  # Slice para que no tome los encabezados
            if fila[1] == codigo:
                filas_a_eliminar.append(fila) #junta todas las filas que tenga ese legajo
        for fila in filas_a_eliminar:
            matriz_combinada.remove(fila) #borra
        print('filas elimindas correctamente de la matriz.')
    else:
        print('El codigo ingresado no existe.')
    
    return dicc_materias , matriz_combinada