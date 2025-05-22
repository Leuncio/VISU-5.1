# coordenadas.py

# This file contains functions for converting coordinates from meters to CSS percentage values

from .converciones import metros_a_css_porcentaje

semaforo = metros_a_css_porcentaje(8, 8)
semaforo["color"] = "verde"  # Puedes cambiar esto dinámicamente luego

print(semaforo)