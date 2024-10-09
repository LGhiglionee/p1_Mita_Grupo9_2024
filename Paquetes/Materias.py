def asignar_materias(dicc_alumnos, matriz_combinada, dicc_materias):
    legajo = int(input("Ingrese el legajo del alumno al que desea asignar materias: "))
    
    if legajo not in dicc_alumnos:
        print("El legajo ingresado no corresponde a ningún alumno registrado.")
        return matriz_combinada, dicc_materias

    print(f"Asignando materias al alumno: {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]}")
    
    materias_asignadas = []
    while True:
        print("\nMaterias disponibles:")
        for codigo in dicc_materias.keys():
            print(f'Codigo: {codigo}, Materia: {dicc_materias[codigo][0][1]}, Turno: {dicc_materias[codigo][0][0]}')
        
        codigo_materia = input("Ingrese el código de la materia a asignar (o 'q' para terminar): ")
        
        if codigo_materia.lower() == 'q':
            break
        codigo_materia = int(codigo_materia)
        if codigo_materia in dicc_materias:
            if any(fila[0] == legajo and fila[1] == codigo_materia for fila in matriz_combinada): #se fija si ya se asigno la materia
                print("Esta materia ya está asignada al alumno.")
            else:
                nueva_fila = [legajo, codigo_materia, '-', '-', '-']
                matriz_combinada.append(nueva_fila)
                materias_asignadas.append(dicc_materias[codigo_materia][0][1])
                print(f"Materia '{dicc_materias[codigo_materia][0][1]}' asignada correctamente.")
        else:
            print("Código de materia inválido.")
    
    if materias_asignadas:
        print(f"\nMaterias asignadas a {dicc_alumnos[legajo][0]} {dicc_alumnos[legajo][1]}:")
        for materia in materias_asignadas:
            print(f"- {materia}")
    else:
        print("No se asignaron nuevas materias.")

    return matriz_combinada, dicc_materias
    

