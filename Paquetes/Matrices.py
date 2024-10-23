import random
import json

def creardicc_alumnos(x):
    diccalumnos = {}
    while x >= 1:
        legajo = random.randint(111111111, 999999999)
        nombre = random.choice(['Lucas', 'Maximo', 'Franco', 'Felipe', 'Noah', 'Juan', 'Guillermo', 'Pablo', 'Agustin'])
        apellido = random.choice(['Ghiglione', 'Bramuglia', 'Collura', 'Remonteo', 'Gomez', 'Huchan', 'Fernandez', 'Gonzalez', 'Perez', 'Garcia'])
        mail = ''.join([nombre[0].lower(), apellido.lower(), '@gmail.com'])
        dia= random.randint(1,31) #elije un dia posible
        mes= random.randint(1,12) #meses posibles
        anio= random.randint(1960, 2007)
        fecha_nacimiento = '{:02d}/{:02d}/{}'.format(dia,mes,anio)
        diccalumnos[legajo] = [nombre, apellido, mail, fecha_nacimiento]
        x -= 1
    try:
        with open('ArchivoAlummos.json', 'w', encoding= 'UTF-8') as archivo:
            json.dump(diccalumnos, archivo, indent = 2)   
    except:
        print('No se puede abrir el archivo')

    return diccalumnos, archivo

#funciona

def creardicc_materias():
    dicc_materias = {
        3180: 'Programación I',
        91218: 'Fundamentos de Química',
        31784: 'Sistemas de Representación',          #le puse codigo manualmente, mas facil
        31283: 'Matemática Discreta',
        553123: 'Álgebra',
        11163: 'Arquitectura de Computadores'
    }
    try:
        with open('ArchivoAlummos.json', 'w', encoding= 'UTF-8') as archivo:
            json.dump(dicc_materias, archivo, indent = 2)   
    except:
        print('No se puede abrir el archivo')
    
    return dicc_materias, archivo
 
        
def EscribirArchivo(matriz_combinada):
    try:
        with open('ArchivoMatriz.txt', 'w', encoding= 'UTF-8') as arch:
            lineas = [f'{fila[0]};{fila[1]};{fila[2]};{fila[3]};{fila[4]};\n' for fila in matriz_combinada]
            arch.writelines(lineas)
        
        print('Carga de datos finalizada')
    except OSError:
        print('No se pudo crear el archivo')
    except ValueError:
        print('No se pudo convertir el tipo de dato del legajo')
    finally:
        return arch



def combinado(diccalumnos, dicc_materias):

    min_materias, max_materias = 0 , 5
    matriz_combinada = []
    matriz_combinada.append(['Legajo', 'Código Materia', 'Parcial 1', 'Parcial 2', 'Final'])
    for legajo in diccalumnos.keys():
        num_materias = random.randint(min_materias, max_materias)  # pone un numero aleatorio para no todos los alumnos esten en todas las materias
        materias_asignadas = []
        materias_disponibles = list(dicc_materias.keys()) #crea una lista con todos los codigos
        while len(materias_asignadas) < num_materias and materias_disponibles:
            codigo = random.choice(materias_disponibles)
            materias_asignadas.append(codigo)  # pone materia a alumno
            materias_disponibles.remove(codigo)  # la saca de la otra lsta, para que no hayan repetidas
        for codigo in materias_asignadas:
            parcial1 = random.randint(1,10)
            parcial2 = random.randint(1,10)
            if parcial1 >= 8 and parcial2 >=8:
                final= 'Promocion'
            elif parcial1 <4 and parcial2<4:
                final= 'Recursa'
            elif parcial1 < 4 or parcial2 < 4:
                final= 'Debe recuperatorio'
            else:
                final= random.randint(1,10)
            matriz_combinada.append([legajo, codigo, parcial1, parcial2, final]) #hace la linea de la matriz
    arch= EscribirArchivo(matriz_combinada)

    return matriz_combinada, arch
