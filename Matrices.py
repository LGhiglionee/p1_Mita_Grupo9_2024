import random

def crearmatriz_alumnos(cantalum):
    matrizalumnos = []
    while cantalum>=1:
        legajo = random.randint(0,999999999)
        cad = str(legajo).zfill(9)
        nombre = random.choice(['Lucas', 'Maximo', 'Franco', 'Felipe', 'Noah', 'Juan', 'Guillermo', 'Pablo', 'Agustin'])
        apellido = random.choice(['Ghiglione','Bramuglia','Collura','Remonteo', 'Gomez', 'Huchan', 'Fernandez', 'Gonzalez', 'Perez', 'Garcia'])
        matrizalumnos.append (
        {
            'Legajos' : legajo,
            'Nombres' : nombre,
            'Apellidos' : apellido
        }
        )
        cantalum -= 1
    return matrizalumnos
#funciona
def crearmatriz_materias():
    codigos_rep = [] 
    encabezado = ['Codigo', 'Nombre Materia', 'Turno']
    matriz_materias = []
    
    for i in range(18):# 18 = len(turnos) * len(materias) => total de materias x turnos 3x6
        
        codigo = random.randint(1, 1324)
        while codigo in codigos_rep:
            codigo = random.randint(1, 1324)
        turno = random.choice(['Mañana', 'Tarde', 'Noche'])
        materia = random.choice(['Programacion I', 'Fundamentos de Quimica', 'Sistemas de Representacion', 'Matematica Discreta', 'Algebra', 'Arquitectura de computadores'])
        codigos_rep.append(codigo)
        matriz_materias.append(
                {
                    'Turnos' : turno,
                    'Materias' : materia,
                    'Código' : codigo
                }
            )
    return matriz_materias
#funciona
def limitar(opcion, x): #opcion == lista , x == numero para limitar
    if len(opcion) > x:
        return opcion[:x]
    else:
        return(opcion) 
    # no estaria funcionando, revisar!

def crearmatriz_notas(matrizalumnos):
    matriznotas = [['Parcial 1', 'Parcial 2', 'Final']]
    matriznotas = []
    for alumno in matrizalumnos[1:]:
        legajo = str(alumno['Legajos'])
    for i in range(len(legajo)):
        parcial1 = random.randint(1,10)
        parcial2 = random.randint(1,10)
        if parcial1 >= 8 and parcial2 >= 8:
            final = 'Promo'
        else:
            final = random.randint(1,10)
        matriznotas.append(
            {
                'Parcial 1' : parcial1,
                'Parcial 2' : parcial2,
                'Final' : final
            }
        )
    return matriznotas

def combineta(matrizalumnos, matrizmateria, matriznotas):
    matriz_combinada = []
    for alumno, materia, nota in zip(matrizalumnos, matrizmateria, matriznotas):
        combinado = {
            'Legajos' : alumno['Legajos'],
            'Nombres' : alumno['Nombres'],
            'Apellidos' : alumno['Apellidos'],
            'Turnos' : materia['Turnos'],
            'Materias' : materia['Materias'],
            'Código' : materia['Código'],
            'Parcial 1' : nota['Parcial 1'],
            'Parcial 2' : nota['Parcial 2'],
            'Final' : nota['Final']
                        
        }
        matriz_combinada.append(combinado)
    return matriz_combinada
    
#hay algo raro aca, arregle lo de los legajos multiplicados pero ahora no funca el codigo => codigo = materia[0]
