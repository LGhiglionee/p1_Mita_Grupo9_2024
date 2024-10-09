def menuT():
    print('1. Alumnos')
    print('2. Materias')
    print('3. Notas')
    print('4. Mostrar tabla')
    print('5. Salir')
    

def menuA():
    print('1. Agregar alumno')
    print('2. Leer alumno')
    print('3. Actualizar alumno')
    print('4. Eliminar alumno')
    print('5. Asingar materia a alumno')
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
    pass

def tabla(x):
    # max de cada columna
    ancho_columna = [max(len(str(item)) for item in col) for col in zip(*x)]
    

    # muestro el encabezado
    def encabezado():
        encabezado = x[0]
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
        
        print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(encabezado, ancho_columna)) + '|')
        
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
    
    #fila +---+
    def filas():
        for fila in x[1:]:
            print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(fila, ancho_columna)) + '|')
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea

    
    encabezado()
    filas()

def tabladicc(dicc_materia):
    for mat in dicc_materia.keys():
        print(f'{mat}, {dicc_materia[mat][0]}, {dicc_materia[mat][1]}')
