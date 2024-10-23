import random
import json

def creardicc_alumnos(archivo, modo):
    diccalumnos = {}
    try:
        with open(archivo, modo, encoding= 'UTF-8') as ArchivoAlumnos:
            diccalumnos = json.load(ArchivoAlumnos)
    except FileNotFoundError:
        print('No se encontro el archivo.')
    except:
        print('Ocurrio un error.')
    finally:
        return diccalumnos, ArchivoAlumnos



def creardicc_materias(archivo, modo):
    dicc_materias = {}
    try:
        with open(archivo, modo, encoding= 'UTF-8') as ArchivoMateria:
            dicc_materias= json.load(ArchivoMateria)   
    except FileNotFoundError:
        print('No se encontro el archivo.')
    except:
        print('Ocurrio un error.')
    finally:
        return dicc_materias, ArchivoMateria
 
        
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
