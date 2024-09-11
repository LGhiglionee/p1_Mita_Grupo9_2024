from Matrices import *

def menu():
    print('1. Agregar alumno')
    print('2. Leer alumno')
    print('3. Actualizar alumno')
    print('4. Eliminar alumno')
    print('5. Ver notas')
    print('6. Agregar nota')
    print('7. Actualizar nota')
    print('8. Salir')
    return
def encabezados(x):# x == cualquier matriz, en un futuro si se unifica va ser más cómodo
    claves = x[0].keys()
    encabezado = " | ".join(f"{clave:<19}" for clave in claves)
    print(encabezado)
    for fila in x:
        cadena = " | ".join(f"{str(fila.get(clave)):<19}" for clave in claves)
        print(cadena)