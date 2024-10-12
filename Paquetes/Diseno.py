def menuT():
    print('1. Alumnos')
    print('2. Materias')
    print('3. Notas')
    print('4. Mostrar tabla')
    print('5. Artimetrica Alumnos')
    print('6. Salir')
    
def menuA():
    print('1. Agregar alumno')
    print('2. Leer alumno')
    print('3. Actualizar alumno')
    print('4. Eliminar alumno')
    print('5. Asignar materia a alumno')
    print('6. Salir')
    
def menuM():  
    print('1. Agregar nueva materia')
    print('2. Eliminar materia')
    print('3. Mostrar materias')
    print('4. Salir')
    
def menuN():
    print('1. Ver notas')
    print('2. Agregar nota')
    print('3. Actualizar nota')
    print('4. Salir')

def menuP():
    print('1. Promedio de alumno por materia')
    print('2. Promedio de alumno en todas las materias inscriptas')
    print('3. Salir')
    
def tabla(x):
    # max de cada columna
    ancho_columna = [max(len(str(item)) for item in col) for col in zip(*x)]
    
    
    # muestro el encabezado
    encabezado = x[0]
    print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
        
    print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(encabezado, ancho_columna)) + '|')
        
    print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
    
    #fila +---+

    for fila in x[1:]:
        print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(fila, ancho_columna)) + '|')
    print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea

def tablaMateria(dicc_materia):
    dicc1 = dicc_materia.copy()
    matriz = []
    matriz.append(['Codigo', 'Nombre'])
    for codigo, nombre in dicc1.items():
        matriz.append([codigo,nombre]) 
        
    # max de cada columna
    ancho_columna = [max(len(str(item)) for item in col) for col in zip(*matriz)]
    
    # muestro el encabezado
    
    encabezado = matriz[0]
    print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
        
    print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(encabezado, ancho_columna)) + '|')
        
    print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
    
    #fila +---+
    for fila in matriz[1:]:
        print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(fila, ancho_columna)) + '|')
    print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
    


    