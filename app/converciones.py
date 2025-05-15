# converciones.py

# This file contains functions for converting coordinates from meters to CSS percentage values

from .coordenadas_mapa import metros_a_css_porcentaje

semaforo = metros_a_css_porcentaje(8, 3)
semaforo["color"] = "verde"  # Puedes cambiar esto dinámicamente luego

print(semaforo)