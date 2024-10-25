from random import *
from .Login import *
import json

def ActualizarArchivoAlumno (dicc_alumnos, archivo):
    with open('ArchivoAlumnos.json', 'w', encoding= 'UTF-8') as archivo :
        json.dump(dicc_alumnos, archivo, ensure_ascii= False)

def ActualizarArchivoMaterias (dicc_materias, archivo):
    with open('ArchivoMaterias.json', 'w', encoding = 'UTF-8') as archivo:
        json.dump(dicc_materias, archivo, ensure_ascii= False)
        
def EscribirArchivo(matriz_combinada):
    try:
        with open('ArchivoMatriz.txt', 'w', encoding= 'UTF-8') as arch:
            lineas = [f'{fila[0]};{fila[1]};{fila[2]};{fila[3]};{fila[4]}\n' for fila in matriz_combinada]
            arch.writelines(lineas)
        
        print('Carga de datos finalizada')
    except OSError:
        print('No se pudo crear el archivo')
    except ValueError:
        print('No se pudo convertir el tipo de dato del legajo')
    finally:
        return arch
    

def agregar_alumno(dicc_alumnos, matriz_combinada, dicc_materias, archivo):
    flag = 1
    while flag == 1:
        legajo = input('Ingrese el legajo: ')
        if not legajo.isdigit():
            print('El legajo debe ser un número.')
        else:
            flag = 0
    nombre = input('Ingrese el nombre: ').title()
    apellido = input('Ingrese el apellido: ').title()

    aux= 0
    while aux == 0:
        fecha_nacimiento = input('Ingrese tu fecha de nacimiento en formato (DD/MM/YYYY): ')
        if validar_fecha_nacimiento(fecha_nacimiento) == False:
            print('Fecha de nacimiento invalida. Porfavor revise como la introdujo')
        else:
            aux = 1

    aux2=0
    while aux2 == 0:
        mail= input('Ingrese tu mail: ')
        if validar_mail(mail) == False:
            print('Mail invalido, Porfavor revise.')
        else:
            aux2 = 1

    dicc_alumnos[legajo] = [nombre, apellido, mail, fecha_nacimiento] #agrega alumno a dicc alumnos

    entrada = input('Desea asignar una nueva materia a este alumno? [y/n] ').lower()
    
    while entrada not in ['y', 'n', 'yes', 'no']:
        entrada = input('Recuerde ingresar las opciones que ve en pantalla [y/n]: ').lower()
        
    if entrada in ['y', 'yes']:
        aux = 1
        while aux == 1:
            for codigo, materia in dicc_materias.items():
                print(f'Codigo: {codigo}, Materia: {materia}') #muestra materias disponibles

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
                print(f'Materia {materia} asignada correctamente.')
                EscribirArchivo(matriz_combinada)
                return dicc_alumnos, matriz_combinada
            else:
                print('No se encontró el código, intente nuevamente.')
        
    else: #si pone que no, no asigna materia
        nuevo_ingreso = [
            legajo,
            '',  # sin materia
            '-',  # parcial 1
            '-',  # parcial 2
            '-'   # final
        ]
        matriz_combinada.append(nuevo_ingreso)

    print(f'Nuevo alumno con legajo {legajo} fue agregado.')
    
    EscribirArchivo(matriz_combinada)
    ActualizarArchivoAlumno(dicc_alumnos, 'ArchivoAlumnos.json')

    return dicc_alumnos, matriz_combinada


def eliminar_alumno(dicc_alumnos, matriz_combinada):
    legajo = int(input('Ingrese el legajo del alumno a eliminar: '))
    if legajo in dicc_alumnos :
        dicc_alumnos.pop(legajo)
        print(f'Alumno con legajo {legajo} eliminado.')

        filas_a_eliminar = []
        for fila in matriz_combinada[1:]:  # slice para que no tome los encabezados
            if fila[0] == legajo:
                filas_a_eliminar.append(fila) #junta todas las filas que tenga ese legajo // agregar un re.match ==> patrón = fila ==> ('alumno')
        for fila in filas_a_eliminar:
            matriz_combinada.remove(fila) #borra
            print('filas elimindas correctamente de la matriz.')
    else:
        print('El legajo ingresado no existe.')

    ActualizarArchivoAlumno(dicc_alumnos, 'ArchivoAlumnos.json')
    EscribirArchivo(matriz_combinada)
    
    return dicc_alumnos , matriz_combinada


def leer_alumno(dicc_alumnos):
    encontrado = 0
    legajo = int(input('Ingrese el legajo del alumno que desea buscar: '))
    for alumno in dicc_alumnos.keys():
        if alumno == legajo:
            print('El alumno ha sido encontrado')
            print('Datos del alumnos: ', end=' ')
            print(f'Legajo: {legajo}, Nombre: {dicc_alumnos[legajo][0]}, Apellido: {dicc_alumnos[legajo][1]}, Mail: {dicc_alumnos[legajo][2]}, Fecha de nacimiento: {dicc_alumnos[legajo][3]}')
            encontrado= 1
    if encontrado == 0:
        print('No se encontro el alumno')
    return


def actualizar_alumno(dicc_alumnos):

    legajo = int(input('Ingrese el legajo del alumno a actualizar: '))
    for alumno in dicc_alumnos.keys():
        if alumno == legajo:
            nuevo_nombre = input('Ingrese el nuevo nombre: ').title().strip()
            nuevo_apellido = input('Ingrese el nuevo apellido: ').title().strip()
            aux= 0
            while aux == 0:
                fecha_nacimiento = input('Ingrese tu fecha de nacimiento en formato (DD/MM/YYYY): ')
                if validar_fecha_nacimiento(fecha_nacimiento) == False:
                    print('Fecha de nacimiento invalida. Porfavor revise como la introdujo')
                else:
                    aux = 1

            aux2=0
            while aux2 == 0:
                mail= input('Ingrese tu mail: ')
                if validar_mail(mail) == False:
                    print('Mail invalido, Porfavor revise.')
                else:
                    aux2 = 1

            if nuevo_apellido and nuevo_nombre:
                dicc_alumnos[legajo] = [nuevo_nombre, nuevo_apellido, mail, fecha_nacimiento]
                print('Datos Actualizados.')

                ActualizarArchivoAlumno(dicc_alumnos, 'ArchivoAlumnos.json')

                return dicc_alumnos
            
    print('No se ha encontrado el alumno a actualizar')


def agregar_nota(matriz_combinada, dicc_alumnos):
    
    legajo = int(input('Ingrese el número de legajo del alumno a calificar: '))
    codigo_materia = int(input('Ingrese el codigo de la materia: '))
    for alumno in matriz_combinada[1:]:  # empieza desde el índice 1 para saltar el encabezado
        if int(alumno[0]) == legajo and alumno[1] == codigo_materia: 
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
            EscribirArchivo(matriz_combinada)
            return matriz_combinada
    
    print('No se ha encontrado el alumno con el legajo ingresado y/o el codigo de materia no coincide')
    return matriz_combinada


def leer_nota(matriz_combinada, dicc_alumnos):
    legajo = int(input('Ingrese el número de legajo del estudiante: '))
    codigo_materia = int(input('Ingrese el codigo de la materia que desea ver las notas: '))
    for fila in matriz_combinada [1:]:
        if int(fila[0]) == legajo and fila[1] == codigo_materia: #busca el legajo, e imprime toda su informacion
            print(f"Legajo: ", fila[0])
            print(f"Nombre y apellido: {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]}")
            print(f'Codigo Materia: ', fila[1])
            print(f"Parcial 1: ", fila[2])
            print(f"Parcial 2: ", fila[3])
            print(f"Final: ", fila[4])
            return
    print('No se ha encontrado el alumno con el legajo ingresado y/o el codigo de la materia no coincide')


def actualizar_nota(matriz_combinada, dicc_alumnos):
    legajo = int(input("Ingrese el legajo del alumno: "))
    codigo_materia = int(input('Ingrese el codigo de la materia que desea ver las notas: '))
    for fila in matriz_combinada[1:]:
        
        if fila[0] == legajo and fila[1] == codigo_materia:
            print(f"Nombre y apellido: {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]}")
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
                if fila[2] >= 8 and fila[3] >= 8:
                    fila[4] = 'Promoción'
                elif fila[2] < 4 and fila[3] < 4:
                    fila[4] = 'Recursa'
                elif fila[2] < 4 or fila[3] < 4:
                    fila[4]= 'Debe recuperatorio'
                else:
                    final = input('Ingrese la nueva nota del examen final (1-10 o "-" para no cambiar): ')
                    if final != '-':
                        if final.isdigit() and 1 <= int(final) <= 10:
                            fila[4] = int(final)
                        else:
                            print('Nota inválida. Debe ser un número entre 1 y 10.')
                            return matriz_combinada

            print("Notas actualizadas con éxito")
            EscribirArchivo(matriz_combinada)
            return matriz_combinada

    print("El legajo no existe y/o el codigo de la materia no coincide")
    return matriz_combinada

def agregar_nueva_materia(dicc_materias, Archivo):
    flag = 0
    nuevo_codigo = int(input('Ingrese el codigo de la nueva materia: '))
    for mat in dicc_materias.keys():
        if mat == nuevo_codigo:
            print('El codigo ya existe')
            flag = 1
    if flag == 0:
        nuevo_nombre = input('Ingrese el nombre de la materia: ').strip().capitalize()
        dicc_materias[nuevo_codigo] = nuevo_nombre

    ActualizarArchivoMaterias (dicc_materias, 'ArchivoMaterias.json')

    print('Materia añadida correctamente.')
    return dicc_materias



def eliminar_materia(dicc_materias, matriz_combinada, archivo):
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

    ActualizarArchivoMaterias (dicc_materias, 'ArchivoMaterias.json')

    return dicc_materias , matriz_combinada



def asignarmateria(matriz_combinada, dicc_alumnos, dicc_materias):
    legajo = int(input('Ingrese el legajo del alumno al que le quieras asignar una materia: '))
    if legajo not in dicc_alumnos:
            print('No se encontro al alumno')
            return
    codigo_materia= int(input(f'Ingrese el codigo de la materia que le quieras asignarle a {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]}: '))
    if codigo_materia in dicc_materias:
        matriz_combinada.append([legajo, codigo_materia, '-', '-','-'])
        print(f'La materia {dicc_materias[codigo_materia]} fue asignada correctamente al alumno.')
        return matriz_combinada