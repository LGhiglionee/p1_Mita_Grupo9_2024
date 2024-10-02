import re, collections, random

def creardicc_alumnos(x):
    diccalumnos = []
    while x>=1:
        legajo = random.randint(111111111,999999999)
        
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

def creardicc_materias():
    turnos = ('Mañana', 'Tarde', 'Noche')
    materias = ('Programación I', 'Fundamentos de Quimica', 'Sistemas de Representación', 'Matematica Discreta', 'Algebra', 'Arquitectura de computadores')
    dicc_final = []
    CodigosNoUsados = set(range(111, 999))
    cont = collections.defaultdict(lambda: collections.defaultdict(int))# crea dicc ==> {'':{'':0}}
    
    while CodigosNoUsados:# tuve que hacer un bucle en base a los elementod de codigos no usados, no me cierra
        for turno in turnos:
            materias_disponibles = list(materias)
            
            for _ in range(len(materias)*3):  # materias * turnos
                limite = [m for m in materias if cont[turno][m] < 3]
                
                if not materias_disponibles or not CodigosNoUsados:
                    return dicc_final
                
                codigo = random.choice(list(CodigosNoUsados))
                CodigosNoUsados.remove(codigo)
                
                materia = random.choice(materias_disponibles)
                
                if cont[turno][materia] < 3:
                    cont[turno][materia] += 1
                    dicc_final.append  ({
                        'Codigo': codigo,
                        'Turno': turno,
                        'Materia': materia
                    })
                    
    
    return dicc_final
#ahí lo cambie según el profesor    
        


def creardicc_notas(x):#matriz cambiar nombre
    diccio_notas = [] #matriz cambiar nombre
    for l in x[1:]:
        
        for i in range(len(x)):
            
            parcial1 = random.randint(1,10)
            parcial2 = random.randint(1,10)
            
            if parcial1 >= 8 and parcial2 >= 8:
                final = 'Promocion'
            elif parcial1 <4 and parcial2 <4:
                final = 'Recursa'
            else:
                final = random.randint(1,10)
            diccio_notas.append(
                {
                    'Parcial 1' : parcial1,
                    'Parcial 2' : parcial2,
                    'Final' : final
                }
            )
    return diccio_notas

def combinado(diccalumnos, matrizmateria, matriznotas):
    matriz_combinada = []

    matriz_combinada.append(['Legajo', 'Código Materia', 'Materia', 'Turno', 'Parcial 1', 'Parcial 2', 'Final'])

    for alumno, materia, nota in zip(diccalumnos, matrizmateria, matriznotas):
        matriz_combinada.append (fila = [
            alumno['Legajos'],
            materia['Codigo'], #codigo de materia
            nota['Parcial 1'],
            nota['Parcial 2'],
            nota['Final']
        ])
        
    
    return matriz_combinada
