def Promedio(matriz_combinada, dicc_alumnos, dicc_materias): #Lo que tengo pensado
                 #aca es agregar un alumno e informar cual es el promedio de alumno por 
                 # materia que este anotado
    try:
        legajo = int(input('Ingrese el legajo del alumno que deseas saber su promedio: '))
        codigo_materia = int(input('Ingrese el código de la materia que desee saber su promedio: '))
        
        for fila in matriz_combinada:
            if fila[0] == legajo and fila[1] == codigo_materia:
                parcial1 = fila[2]
                parcial2 = fila[3]
                final = fila[4]
                
                if parcial1 == '-' or parcial2 == '-':
                    raise ValueError("Faltan notas de parciales")             
                
                if final == 'Promoción':
                    promedio = (parcial1 + parcial2) / 2
                elif final == 'Recursa':
                    promedio = (parcial1 + parcial2) / 2
                elif final != '-':
                    promediopar = (parcial1 + parcial2)/2
                    promedio = (promediopar + final)/2
                else:
                    promedio = (parcial1 + parcial2) / 2
                
                print(f'El promedio del alumno {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]} '
                      f'en la materia {dicc_materias[codigo_materia]} es {promedio}')
                
                if final == 'Promoción':
                    print("El alumno ha promocionado la materia.")
                elif final == 'Recursa':
                    print("El alumno debe recursar la materia.")
                elif final != '-':
                    print(f"Nota del examen final: {final}")
                else:
                    print("El alumno aún no ha rendido el examen final.")
                
                return
        
        print("No se encontró el alumno o la materia especificada.")
    
    except ValueError as parciales:
        print(f'Hubo un problema, {parciales}')
    except TypeError:
        print('Hubo un problema. Hay alguna/s instancia/s que no tiene nota cargada correctamente.')

def Promedio_todas_Materias(matriz_combinada, dicc_alumnos):
    promedio_materias= []
    try:
        legajo= int(input('Ingrese el legajo del alumno: '))
        promedio = 0
        if legajo not in dicc_alumnos:
            raise ValueError('El legajo ingresado no pertenece a ningun alumno')
        for fila in matriz_combinada:
            if legajo == fila[0]:
                parcial1 = fila[2]
                parcial2 = fila[3]
                final = fila[4]

                assert parcial1 != '-', 'Falta la nota del primer parcial'
                assert parcial2 != '-', 'Falta la nota del segundo parcial'
                if final == 'Promoción':
                    promedio = (parcial1 + parcial2) / 2
                elif final == 'Recursa':
                    promedio = (parcial1 + parcial2) / 2
                elif final != '-':
                    promediopar = (parcial1 + parcial2)/2
                    promedio = (promediopar + final)/2
                else:
                    promedio = (parcial1 + parcial2) / 2
                promedio_materias.append(promedio)

        promedio_total= sum(promedio_materias)/len(promedio_materias)
        print(f'El promedio del alumno {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]} es {promedio_total}')
    except TypeError:
        print('Ha habido un problema. Hay alguna/s instancia/s que no tiene nota cargada')
    except AssertionError as msj:
        print(f'Ha ocurrido un error. {msj}')
    except ValueError as nopertenece:
        print(f'{nopertenece}')
