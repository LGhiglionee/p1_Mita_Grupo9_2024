import random

def crearmatriz_alumnos(cantalum):
    titulos= ['Legajo', 'Nombre', 'Apellido']
    nombres= ['Lucas', 'Maximo', 'Franco', 'Felipe', 'Noah', 'Juan', 'Guillermo', 'Pablo', 'Agustin']
    apellidos=['Ghiglione','Bramuglia','Collura','Remonteo', 'Gomez', 'Huchan', 'Fernandez', 'Gonzalez', 'Perez', 'Garcia']
    matrizalumnos= [titulos]
    for i in range (cantalum):
        legajo= random.randint(0,999999999)
        cad= str(legajo).zfill(9)
        nombre= random.choice(nombres)
        apellido=random.choice(apellidos)
        matrizalumnos.append([cad, nombre, apellido])
    return matrizalumnos

def crearmatriz_materias(cantmaterias):
    turnos = ['Mañana', 'Tarde', 'Noche']
    materias = ['Programacion I', 'Fundamentos de Quimica', 'Sistemas de Representacion', 'Matematica Discreta', 'Algebra', 'Arquitectura de computadores']
    encabezado = ['Codigo', 'Nombre Materia', 'Turno']
    matriz_materias = [encabezado]
    codigos_rep = []
    for i in range(cantmaterias):
        codigo = random.randint(1, 1324)
        while codigo in codigos_rep:
            codigo = random.randint(1, 1324)
        turno = random.choice(turnos)
        materia = random.choice(materias)
        matriz_materias.append([codigo, materia, turno])
        codigos_rep.append(codigo)

    return matriz_materias

def crearmatriz_notas(matrizalumnos, matrizmaterias):
    encabezado = ['Legajo', 'Codigo', 'Parcial 1', 'Parcial 2', 'Final']
    matriznotas = [encabezado]
    for alumno in matrizalumnos[1:]:
        legajo = alumno[0]
        for materia in matrizmaterias[1:]:
            codigo = materia[0]
            parcial1 = random.randint(1, 10)
            parcial2 = random.randint(1, 10)
            if parcial1 >= 8 and parcial2 >= 8:
                final = 'Eximido'
            else:
                final = random.randint(1, 10)
            matriznotas.append([legajo, codigo, parcial1, parcial2, final])
    return matriznotas
