def agregar_materia(matrizmaterias):
    codigo= int(input('Ingrese el codigo de la materia: '))
    nombre = input('Ingrese el nombre de la materia: ').capitalize().strip()
    turno = input('Ingrese el turno en el que se dicta: ')
    nuevasmat = [codigo,nombre,turno]

    matrizmaterias.append(nuevasmat)
    return matrizmaterias

def eliminar_materia(matrizmaterias):
    codigo= int(input('Ingrese el codigo de la materia a eliminar'))
    for materia in matrizmaterias:
        if materia[0] == codigo:
            matrizmaterias.remove (materia)
            print(f'La materia con codigo {codigo} ha sido eliminada')
            return
    print('No se encontro ninguna materia con dicho codigo')