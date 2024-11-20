def Promedio(matriz_combinada, dicc_alumnos, dicc_materias): 
    '''
    Pre: ---
    Pos: Devuelve promedio del alumno de la materia puesta
    '''
    try:
        legajo = int(input('Ingrese el legajo del alumno que deseas saber su promedio: '))
        codigo_materia = int(input('Ingrese el código de la materia que desee saber su promedio: '))
        
        for fila in matriz_combinada:
            if fila[0] == legajo and fila[1] == codigo_materia:
                parcial1 = fila[2]
                parcial2 = fila[3]
                final = fila[4]
                calculo = lambda parcial1, parcial2: (parcial1 + parcial2) / 2
                calculo_par = lambda parcial1, parcial2: (parcial1 + parcial2) / 2
                
                if parcial1 == '-' or parcial2 == '-':
                    raise ValueError
                if final == 'Promocion':
                    promedio = calculo(parcial1, parcial2)
                elif final == 'Recursa':
                    promedio = calculo(parcial1, parcial2)
                elif final == 'Debe recuperatorio':
                    promedio= calculo(parcial1, parcial2)
                elif final == '-':
                    promedio = calculo(parcial1, parcial2)
                else:
                    promedio_par = calculo_par(parcial1, parcial2)
                    promedio = calculo(promedio_par, final)
                print(f'El promedio del alumno {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]} '
                      f'en la materia {dicc_materias[codigo_materia]} es {promedio}')
                
                if final == 'Promoción':
                    print("El alumno ha promocionado la materia.")
                elif final == 'Recursa':
                    print("El alumno debe recursar la materia.")
                elif final == "Debe recuperatorio":
                    print("El alumno debe un recuperatorio")
                elif final != '-':
                    print(f"Nota del examen final: {final}")
                else:
                    print("El alumno aún no ha rendido el examen final.")

                return
        
        print("No se encontró el alumno o la materia especificada.")
    
    except ValueError:
        print(f'Hubo un problema, faltan notas de parciales')
    except TypeError:
        print('Hubo un problema. Hay instancias que no tiene nota cargada correctamente.')

def validarlegajo(dicc_alumnos):
    aux= 0
    while aux == 0:
        legajo = int(input('Ingrese el legajo del alumno que deseas saber su promedio: '))
        if legajo in dicc_alumnos:
            return legajo
        else:
            print('No se encontro al alumno')

def Promedio_recursivo (matriz_combinada, promediomat, legajo, i=0):
    '''
    Pre: Recibe una lista vacia, legajo, etc
    Pos: Devuelve lista con cada uno de los promedios POR materia
    '''
    suma, cantnotas = 0,0

    if i == len(matriz_combinada): #cuando llega a la cantidad de notas para
        return promediomat
    
    if matriz_combinada[i][0] == legajo: # i0 es legjo
        if matriz_combinada[i][2] != '-' and matriz_combinada[i][3] != '-': # i2 es parcial 1 y i3 es parcial 2 (ubis)
            promediopar = (matriz_combinada[i][2] + matriz_combinada[i][3])/2 #suma = (matrix_combinada[i][2]+ matriz_combinada[i][3])
            suma += promediopar #asigna en una variable a el resultado de la suma de los dos parciales
            cantnotas += 1

            if matriz_combinada[i][4] not in ['-', 'Debe recuperatorio', 'Promocion', 'Recursa']: #i4 es final
                suma += matriz_combinada[i][4] #si es un entero, a la variable suma le suma el final
                cantnotas += 1

        if cantnotas > 0: 
            promediomat.append(suma/cantnotas) #si hay notas, hace suma divido la cantidad y almacena en una lista promediomat
    
    return Promedio_recursivo(matriz_combinada, promediomat, legajo, i + 1)

def Promediogen(promediomateria):
    '''
    Pre: Recibe lista de el promedio recursivo
    Pos: Hace la suma, divide por la longitud y devuelve promedio
    '''
    try:
        suma=0
        for i in promediomateria:
            suma += i
        promedio = suma/len(promediomateria)
        return promedio
    except ZeroDivisionError:
        print('Hubo un problema. No hay promedios')
        return 0

def ContarAprobados (matrizcombinada, dicc_materias):
    '''
    Pre: ---
    Pos: Devuelve dos conjuntos, uno con los legajos de los que aprobaron, y otro de desaprobados
    '''
    try:
        codigomat = int(input('Ingrese el codigo de la materia: '))
        aprobados = set()
        desaprobados = set()
        if codigomat in dicc_materias:
            for i in matrizcombinada [1:]: #evita encabezado
                final = i[4]
                if i[1] == codigomat: #codigo materia
                    if final == int:
                        if final >= 4:
                            aprobados.add(i[0]) #legajo
                    elif final == 'Promocion':
                        aprobados.add(i[0])
                    else:
                        desaprobados.add(i[0])
            total = aprobados | desaprobados #union (suma de ambos)
            print(f'La cantidad de alumnos que cursaron la materia: {len(total)}')
            print(f'Cantidad de aprobados: {len(aprobados)}')
            print(f'Cantidad de desaprobados: {len(desaprobados)}')
            print()
    except ValueError:
        print('El codigo de la materia debe ser un numero')