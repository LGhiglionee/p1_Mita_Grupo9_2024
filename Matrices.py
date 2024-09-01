import random

def crearmatriz_alumnos(cantalum):
    titulos= ['Legajo', 'Nombre', 'Apellido']
    nombres= ['Lucas', 'Maximo', 'Franco', 'Felipe', 'Noah', 'Juan', 'Guillermo', 'Pablo', 'Agustin']
    apellidos=['Ghiglione','Bramuglia','Collura','Remonteo', 'Gomez', 'Huchan', 'Fernandez', 'Gonzalez', 'Perez', 'Garcia']
    matrizalumnos= [titulos]
    for i in range (cantalum):
        legajo= random.randint(1000000,9999999)
        nombre= random.choice(nombres)
        apellido=random.choice(apellidos)
        matrizalumnos.append([legajo, nombre, apellido])
    return matrizalumnos


