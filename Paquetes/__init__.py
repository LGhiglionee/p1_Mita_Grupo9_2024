from .Aritmetica import *
from .Crud import *
from .Login import *
from .Matrices import *
from .Diseno import *

# __all__ para que no tenga errores de llamada, el init lee primero todo lo que este con guiones bajos primero
__all__ = [
    # Funciones de aritmetica y crud
    'agregar_alumno', 'eliminar_alumno', 'leer_alumno', 'actualizar_alumno',
    'agregar_nota', 'leer_nota', 'actualizar_nota',
    
    # Funciones de login
    'registro', 'inicio',
    
    # Funciones de matrices
    'crearmatriz_alumnos', 'crearmatriz_materias', 'limitar', 'crearmatriz_notas', 'combinado',
    
    # Funciones del diseño
    'menu', 'encabezados', 'mostrar'
]