import json

def creardicc_alumnos(archivo, modo):
    '''
    Pre: Recibe archivo json alumnos
    Pos: Devuelve dicc alumnos
    '''
    diccalumnos = {}
    try:
        with open(archivo, modo, encoding= 'UTF-8') as ArchivoAlumnos:
            diccalumnos_string = json.load(ArchivoAlumnos)
            for legajo , info in diccalumnos_string.items():
                leg = int(legajo)
                diccalumnos[leg] = info
    except FileNotFoundError:
        print('No se encontro el archivo.')
    except ValueError:
        print('Ocurrio un error al convertir el codigo a entero')
    except Exception as msj:
        print(f'Ocurrio un error, {msj}.')
    finally:
        return diccalumnos


def creardicc_materias(archivo, modo):
    '''
    Pre: Recibe archivo json materias
    Pos: Devuelve dicc materias
    '''
    dicc_materias = {}
    try:
        with open(archivo, modo, encoding= 'UTF-8') as ArchivoMateria:
            dicc_materias_string= json.load(ArchivoMateria)
            for codigo , info in dicc_materias_string.items():
                cod = int(codigo)
                dicc_materias[cod] = info
    except FileNotFoundError:
        print('No se encontro el archivo.')
    except ValueError:
        print('Ocurrio un error al convertir el codigo a entero')
    except Exception:
        print('Ocurrio un error.')
    return dicc_materias
 
def crearmatriz (archivo, modo):
    '''
    Pre: Recibe archivo txt
    Pos: Devuelve matriz hecha
    '''
    try:
        matriz_combinada= []
        with open(archivo, modo, encoding='UTF-8') as arch:
            encabezado= arch.readline().strip().split(';')
            matriz_combinada.append(encabezado)
            linea = arch.readline().strip()
            while linea:
                legajo, codigo, parcial1 , parcial2 , final = linea.split(';')
                legajo = int(legajo)  #Paso todo a entero
                codigo= int(codigo) if codigo!='-' else '-'
                parcial1 = int(parcial1) if parcial1 != '-' else '-'
                parcial2 = int(parcial2) if parcial2 != '-' else '-'
                if final not in ['-', 'Debe recuperatorio', 'Recursa', 'Promocion']:
                    final = int(final)
                else:
                    final = final              
                matriz_combinada.append([legajo, codigo, parcial1, parcial2, final])
                linea = arch.readline().strip()
        return matriz_combinada
    except FileNotFoundError:
        print('No se encontro el archivo')
    except ValueError:
        print('Hay un error con la conversion a entero')
    except Exception:
        print('Ocurrio un error')
        
