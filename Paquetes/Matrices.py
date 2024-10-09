import re, collections, random

def creardicc_alumnos(x):
    diccalumnos = {}
    while x >= 1:
        legajo = random.randint(111111111, 999999999)
        nombre = random.choice(['Lucas', 'Maximo', 'Franco', 'Felipe', 'Noah', 'Juan', 'Guillermo', 'Pablo', 'Agustin'])
        apellido = random.choice(['Ghiglione', 'Bramuglia', 'Collura', 'Remonteo', 'Gomez', 'Huchan', 'Fernandez', 'Gonzalez', 'Perez', 'Garcia'])
        diccalumnos[legajo] = [nombre, apellido]
        x -= 1
    return diccalumnos
    '''diccalumnos.sort(key = lambda x: (int(x[legajo])))# el x para que se ordene de manera ascendente
    diccalumnos.reverse()# y esto lo pasa a descendente'''
#funciona

def creardicc_materias():
    turnos = ('Mañana', 'Tarde', 'Noche')
    materias_con_codigos = {
        3180: 'Programación I',
        91218: 'Fundamentos de Química',
        31784: 'Sistemas de Representación',          #Le puse codigo manualmente, mas facil
        31283: 'Matemática Discreta',
        553123: 'Álgebra',
        11163: 'Arquitectura de Computadores'
    }
    dicc_materias = {}
    cont = collections.defaultdict(lambda: collections.defaultdict(int))

    for turno in turnos:
        for codigo, materia in materias_con_codigos.items():
            if cont[turno][materia] < 3:  # Limitar a 3 asignaciones por turno y materia
                cont[turno][materia] += 1
                dicc_materias[codigo] = [turno, materia]

    return dicc_materias
#ahí lo cambie según el profesor    
        



def combinado(diccalumnos, dicc_final):

    min_materias, max_materias = 0 , 5
    matriz_combinada = []
    matriz_combinada.append(['Legajo', 'Código Materia', 'Parcial 1', 'Parcial 2', 'Final'])
    for legajo in diccalumnos.keys():
        num_materias = random.randint(min_materias, max_materias)  # pone un numero aleatorio para no todos los alumnos esten en todas las materias
        materias_asignadas = []
        materias_disponibles = list(dicc_final.keys()) #crea una lista con todos los codigos
        while len(materias_asignadas) < num_materias and materias_disponibles:
            codigo = random.choice(materias_disponibles)
            materias_asignadas.append(codigo)  # pone materia a alumno
            materias_disponibles.remove(codigo)  # la saca de la otra lsta, para que no hayan repetidas
        for codigo in materias_asignadas:
            matriz_combinada.append([legajo, codigo, '-', '-', '-']) #hace la linea de la matriz

    return matriz_combinada
