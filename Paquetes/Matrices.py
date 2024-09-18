import random

def diccio_alumnos(x):
    diccalumnos = []
    while x>=1:
        legajo = random.randint(0,999999999)
        cad = str(legajo).zfill(9)
        nombre = random.choice(['Lucas', 'Maximo', 'Franco', 'Felipe', 'Noah', 'Juan', 'Guillermo', 'Pablo', 'Agustin'])
        apellido = random.choice(['Ghiglione','Bramuglia','Collura','Remonteo', 'Gomez', 'Huchan', 'Fernandez', 'Gonzalez', 'Perez', 'Garcia'])
        diccalumnos.append (
        {
            'Legajos' : legajo,
            'Nombres' : nombre,
            'Apellidos' : apellido
        }
        )
        x -= 1
        diccalumnos.sort(key = lambda x: (int(x["Legajos"])))# el x para que se ordene de manera ascendente
        diccalumnos.reverse()# y esto lo pasa a descendente
    
    return diccalumnos
#funciona

def crearmatriz_materias(x):
    turnos = ['Mañana', 'Tarde', 'Noche']
    materias = ['Programacion I', 'Fundamentos de Quimica', 'Sistemas de Representacion', 'Matematica Discreta', 'Algebra', 'Arquitectura de computadores']

    matriz_materias = []
    codigos_rep = []
    for i in range(x):
        for i in range(18):# 18 = len(turnos) * len(materias) => total de materias x turnos 3x6
            codigo = random.randint(1, 1324)
            while codigo in codigos_rep:
                codigo = random.randint(1, 1324)
            codigos_rep.append(codigo)
        turno = random.choice(turnos)
        materia = random.choice(materias)
        matriz_materias.append([codigo, materia, turno])
        codigos_rep.append(codigo)
    return matriz_materias

#funciona, pero hay q ver como unificar
def limitar(opcion, x): #opcion == lista , x == numero para limitar
    if len(opcion) > x:
        return opcion[:x]
    else:
        return(opcion) 
    # no estaria funcionando, revisar!

def creardicc_notas(x):
    matriznotas = [['Parcial 1', 'Parcial 2', 'Final']]
    matriznotas = []
    for alumno in x[1:]:
        legajo = str(alumno['Legajos'])
        for i in range(len(legajo)):
            parcial1 = random.randint(1,10)
            parcial2 = random.randint(1,10)
            if parcial1 >= 8 and parcial2 >= 8:
                final = 'Promocion'
            elif parcial1 <4 and parcial2 <4:
                final = 'Recursa'
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

def combinado(diccalumnos, matrizmateria, matriznotas):
    matriz_combinada = []
    
    # Agregar encabezados como primera fila (opcional)
    matriz_combinada.append(['Legajo', 'Nombre', 'Apellido', 'Código Materia', 'Materia', 'Turno', 'Parcial 1', 'Parcial 2', 'Final'])

    # Recorrer las tres listas simultáneamente
    for alumno, materia, nota in zip(diccalumnos, matrizmateria, matriznotas):
        fila = [
            alumno['Legajos'],
            alumno['Nombres'],
            alumno['Apellidos'],
            materia[0],  #codigo de materia
            materia[1],  # nombre de la materia
            materia[2],  #turno
            nota['Parcial 1'],
            nota['Parcial 2'],
            nota['Final']
        ]
        matriz_combinada.append(fila)
        
    
    return matriz_combinada
