import random

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
    return diccalumnos

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

    return dicc_materias
#ahí lo cambie según el profesor    
        



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
            matriz_combinada.append([legajo, codigo, '-', '-', '-']) #hace la linea de la matriz

    return matriz_combinada
