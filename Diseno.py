def menu():
    print('1. Agregar alumno')
    print('2. Leer alumno')
    print('3. Actualizar alumno')
    print('4. Eliminar alumno')
    print('5. Ver notas')
    print('6. Agregar nota')
    print('7. Actualizar nota')
    print('8. Salir')

def mostrarmatrizalumnos_ordenada(matrizalumnos):
    for fila in matrizalumnos:
        cad = ' | '.join(f'{elemento:<25}' for elemento in fila)
        print(cad)

def mostrarmatriznotas_ordenada(matriznotas):
    for fila in matriznotas:
        cad = ' | '.join(f'{elemento:<8}' for elemento in fila)
        print(cad)

def mostrarmatrizmaterias_ordenada(matrizmaterias):
    for fila in matrizmaterias:
        cad = ' | '.join(f'{elemento:<25}' for elemento in fila)
        print(cad)