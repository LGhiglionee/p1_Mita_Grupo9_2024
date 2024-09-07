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
#funciona
def crearmatriz_materias():
    turnos = ['Mañana', 'Tarde', 'Noche']
    materias = ['Programacion I', 'Fundamentos de Quimica', 'Sistemas de Representacion', 'Matematica Discreta', 'Algebra', 'Arquitectura de computadores']
    encabezado = ['Codigo', 'Nombre Materia', 'Turno']
    
    matriz_materias = [encabezado]
    codigos_rep = []
    for i in range(18):# 18 = len(turnos) * len(materias) => total de materias x turnos 3x6
        codigo = random.randint(1, 1324)
        while codigo in codigos_rep:
            codigo = random.randint(1, 1324)
        turno = random.choice(turnos)
        materia = random.choice(materias)
        matriz_materias.append([codigo, materia, turno])
        codigos_rep.append(codigo)

    return matriz_materias
#funciona

def crearmatriz_notas(matrizalumnos, matrizmaterias):
    matriznotas = [['Legajo', 'Codigo', 'Parcial 1', 'Parcial 2', 'Final']]
    
    for alumno in matrizalumnos[1:]:
        legajo = alumno[0]
        
        for materia in matrizmaterias[1:]:
            codigo = materia[0]  #extra el codigo ubicado en la primera columna => [0]

            parcial1 = random.randint(1, 10)
            parcial2 = random.randint(1, 10)
            
            if parcial1 >= 8 and parcial2 >= 8:
                final = 'Promociono'
            else:
                final = random.randint(1, 10)
            
            
        matriznotas.append([legajo, codigo, parcial1, parcial2, final])#!!!!!!!!!!!!!!!!!!!!!!!!
    'dsp de unas horas vi que depende donde ubiques matriznotas.append, o funciona el legajo o funciona el codigo de la materia'

    return matriznotas
#hay algo raro aca, arregle lo de los legajos multiplicados pero ahora no funca el codigo => codigo = materia[0]