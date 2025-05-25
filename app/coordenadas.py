# coordenadas.py

# This file contains functions for converting coordinates from meters to CSS percentage values
from .converciones import metros_a_css_porcentaje, numero_para_lista_binaria

NUMERO_BINARIO = numero_para_lista_binaria

semaforo = metros_a_css_porcentaje(8, 8)
semaforo["color"] = numero_para_lista_binaria(6) # Puedes cambiar esto dinámicamente luego

print(semaforo)

avg = metros_a_css_porcentaje(5, 5)
semaforo["color"] = "rojo"