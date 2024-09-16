from .Aritmetica import *
from .Crud import *
from .Login import *
from .Matrices import *
from .Diseno import *

# __all__ para que no tenga errores de llamada, el init lee primero todo lo que este con guiones bajos primero
__all__ = [
    #funciones de aritmetica y crud
    'agregar_alumno', 'eliminar_alumno', 'leer_alumno', 'actualizar_alumno',
    'agregar_nota', 'leer_nota', 'actualizar_nota',
    
    #funciones de login
    'registro', 'inicio',
    
    #funciones de matrices
    'diccio_alumnos', 'crearmatriz_materias', 'limitar', 'creardicc_notas', 'combinado',
    
    #funciones del diseño
    'menu', 'tabla'
]