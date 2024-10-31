import os

flagA = True
flagB = True
flagC = True

lista = []

diccAlumnos = {
  "846885591": [
    "Felipe",
    "Huchan",
    "fhuchan@gmail.com",
    "07/03/1960"
  ],
  "356082115": [
    "Felipe",
    "Collura",
    "fcollura@gmail.com",
    "12/11/1991"
  ],
  "214217020": [
    "Lucas",
    "Ghiglione",
    "lghiglione@gmail.com",
    "15/03/1994"
  ],
  "929496297": [
    "Juan",
    "Collura",
    "jcollura@gmail.com",
    "28/03/1980"
  ],
  "390888732": [
    "Felipe",
    "Collura",
    "fcollura@gmail.com",
    "11/07/2004"
  ],
  "554048772": [
    "Juan",
    "Fernandez",
    "jfernandez@gmail.com",
    "24/07/1985"
  ],
  "157004875": [
    "Guillermo",
    "Garcia",
    "ggarcia@gmail.com",
    "07/03/1982"
  ],
  "341403145": [
    "Noah",
    "Remonteo",
    "nremonteo@gmail.com",
    "15/02/2001"
  ],
  "205240919": [
    "Juan",
    "Fernandez",
    "jfernandez@gmail.com",
    "18/01/1991"
  ],
  "436254842": [
    "Franco",
    "Fernandez",
    "ffernandez@gmail.com",
    "21/01/1964"
  ],
  "383845824": [
    "Noah",
    "Collura",
    "ncollura@gmail.com",
    "07/05/1997"
  ],
  "508429473": [
    "Pablo",
    "Huchan",
    "phuchan@gmail.com",
    "10/06/1989"
  ],
  "529843431": [
    "Felipe",
    "Garcia",
    "fgarcia@gmail.com",
    "20/09/2007"
  ],
  "480875604": [
    "Pablo",
    "Perez",
    "pperez@gmail.com",
    "20/03/1997"
  ],
  "227312127": [
    "Juan",
    "Fernandez",
    "jfernandez@gmail.com",
    "22/10/1967"
  ],
  "624598406": [
    "Franco",
    "Perez",
    "fperez@gmail.com",
    "24/09/1975"
  ],
  "984469199": [
    "Agustin",
    "Fernandez",
    "afernandez@gmail.com",
    "15/05/1965"
  ],
  "537846253": [
    "Noah",
    "Ghiglione",
    "nghiglione@gmail.com",
    "12/11/1969"
  ],
  "721213945": [
    "Agustin",
    "Remonteo",
    "aremonteo@gmail.com",
    "12/09/1962"
  ],
  "947069102": [
    "Pablo",
    "Remonteo",
    "premonteo@gmail.com",
    "31/01/1976"
  ],
  "128314212": [
    "Juan",
    "Huchan",
    "jhuchan@gmail.com",
    "17/10/1960"
  ],
  "654235710": [
    "Maximo",
    "Perez",
    "mperez@gmail.com",
    "18/09/1976"
  ],
  "333085722": [
    "Agustin",
    "Remonteo",
    "aremonteo@gmail.com",
    "20/09/1988"
  ],
  "261477818": [
    "Maximo",
    "Ghiglione",
    "mghiglione@gmail.com",
    "08/04/1974"
  ],
  "870107737": [
    "Lucas",
    "Gonzalez",
    "lgonzalez@gmail.com",
    "18/03/1981"
  ]
}

carpeta = os.listdir(r'C:\Users\nhuch\Desktop\Proyecto\p1_Mita_Grupo9_2024')



if 'ArchivoMatriz.txt' not in lista:
    flagA = False
    print('Falta ArchivoMatriz')
elif 'ArchivoAlumnos.json' not in lista:
    flagB = False
    print('Falta ArchivoAlumnos')
elif 'ArchivoMaterias.json' not in lista:
    flagC = False
    print('FaltaArchivoMaterias')

        
if flagB == True and flagC == True and flagA == True:
    print('Todos los archivos estan presentes')

if flagA != True or flagB != True or flagC != True:
    confirmacion = input(f'Desea formar los archivos faltantes? [y/n] \n').lower().split()
  
if flagB == False:
    with open('ArchivoEjemplo.txt', 'w', encoding='UTF-8') as archivo:
        #archivo.write(str(diccAlumnos)) X
        print('ok')
#meter un dump porque es un diccionario