def Promedio(matriz_combinada, dicc_alumnos, dicc_materias): #Lo que tengo pensado
                 #aca es agregar un alumno e informar cual es el promedio de alumno por 
                 # materia que este anotado
    try:
        legajo= int(input('Ingrese el legajo del alumno que deseas saber su promedio: '))
        codigo_materia = int(input('Ingrese el codigo de la materia que desee saber si promedio: '))
        promedio= 0
        for fila in matriz_combinada:
            leg = fila[0]
            cod = fila[1]
            if legajo == leg and codigo_materia == cod:
                notas= fila[2:]
                promedio = sum(notas)/len(notas)
                print(f'El promedio del alumno {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]} en la materia {dicc_materias[codigo_materia]} es {promedio}')
    except TypeError:
        print('Ha habido un problema. Hay alguna/s instancia/s que no tiene nota cargada')

def Promedio_todas_Materias(matriz_combinada, dicc_alumnos):
    promedio_materias= []
    try:
        legajo= int(input('Ingrese el legajo del alumno: '))
        promedio = 0
        for fila in matriz_combinada:
            leg = fila[0]
            if legajo == leg:
                notas = fila[2:]
                promedio= sum(notas)/len(notas)
                promedio_materias.append(promedio)
        promedio_total= sum(promedio_materias)/len(promedio_materias)
        print(f'El promedio del alumno {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]} es {promedio_total}')
    except TypeError:
        print('Ha habido un problema. Hay alguna/s instancia/s que no tiene nota cargada')
