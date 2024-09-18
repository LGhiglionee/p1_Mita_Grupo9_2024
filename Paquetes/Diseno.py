from .Matrices import *

def menu():
    print('1. Agregar alumno')
    print('2. Leer alumno')
    print('3. Actualizar alumno')
    print('4. Eliminar alumno')
    print('5. Ver notas')
    print('6. Agregar nota')
    print('7. Actualizar nota')
    print('8. Mostrar tabla')
    print('9. Mostrar materias')
    print('10. Agregar materia')
    print('11. Eliminar materia')
    print('12. Salir')
    return

def tabla(x):
    # Encuentra el ancho máximo de cada columna
    ancho_columna = [max(len(str(item)) for item in col) for col in zip(*x)]
    

    # Imprime el encabezado
    def encabezado():
        encabezado = x[0]
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
        
        print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(encabezado, ancho_columna)) + '|')
        
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
    
    # Imprime el contenido
    def filas():
        for fila in x[1:]:
            print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(fila, ancho_columna)) + '|')
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea

    # Ejecuta las funciones de impresión
    encabezado()
    filas()

def tablamatriz(x):
    # Encuentra el ancho máximo de cada columna
    ancho_columna = [max(len(str(item)) for item in col) for col in zip(*x)]
    

    # Imprime el encabezado
    def encabezado():
        encabezado = ['Codigo', 'Materia', 'Turno']
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
        
        print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(encabezado, ancho_columna)) + '|')
        
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea
    
    # Imprime el contenido
    def filas():
        for fila in x[1:]:
            print('|' + '|'.join(f' {str(item).ljust(ancho)} ' for item, ancho in zip(fila, ancho_columna)) + '|')
        print('-'.join(['-' * (ancho + 2) for ancho in ancho_columna]))# la linea

    # Ejecuta las funciones de impresión
    encabezado()
    filas()


