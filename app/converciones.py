# converciones.py
# This file contains functions for converting coordinates from meters to CSS percentage values

from .coordenadas_mapa import metros_a_css_porcentaje

punto_rojo = metros_a_css_porcentaje(2,1)
print(punto_rojo)