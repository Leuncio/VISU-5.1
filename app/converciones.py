# converciones.py

NUMERO_PARA_BINARIO = 6

# Escala: 1 pixel = 0.05 metros
ESCALA_METROS_POR_PIXEL = 0.05

# Dimensiones reales del mapa en metros (basadas en el tamaño de la imagen en píxeles)
ANCHO_MAPA_M = 979 * ESCALA_METROS_POR_PIXEL  # 48.95 metros
ALTO_MAPA_M = 599 * ESCALA_METROS_POR_PIXEL  # 29.95 metros

def metros_a_css_porcentaje(x, y):
    """
    Convierte coordenadas (x, y) en metros a porcentaje CSS,
    basada en el tamaño del mapa y el sistema de coordenadas invertido del CSS.
    """
    # Asegurar que las coordenadas estén dentro de los límites del mapa
    x = min(max(x, 0), ANCHO_MAPA_M)
    y = min(max(y, 0), ALTO_MAPA_M)

    left_pct = (x / ANCHO_MAPA_M) * 100
    top_pct = ((ALTO_MAPA_M - y) / ALTO_MAPA_M) * 100  # Inversión del eje Y

    return {
        "left": f"{left_pct:.2f}%",
        "top": f"{top_pct:.2f}%"
    }

def numero_para_lista_binaria(bits=5):
    """
    Convierte un número entero a una lista de bits con longitud fija.
    """
    binario = bin(NUMERO_PARA_BINARIO)[2:]  # Convierte a binario y elimina el prefijo '0b'
    binario = binario.zfill(bits)  # Rellena con ceros a la izquierda para ajustar el tamaño
    return [int(bit) for bit in binario]

# Prueba de conversión binaria
convertido = numero_para_lista_binaria()
print(f'El número convertido a binario es {convertido}')


def obtener_elementos(tipo, x, y, angulo, num_elementos):
    """
    Obtiene las coordenadas de los elementos en formato CSS,
    asignando un único bit a cada uno. Permite definir X, Y y el ángulo para AGVs.
    """
    elementos = []
    binario = numero_para_lista_binaria(num_elementos)

    for i in range(num_elementos):
        elemento = metros_a_css_porcentaje(x[i], y[i])  # Usa listas para definir posiciones individuales
        elemento["color"] = binario[i % len(binario)]  # Atribuye un único bit
        elemento["id"] = f"{tipo}-{i}"

        # Si el elemento es un AGV, agregar el ángulo definido
        if tipo == "agv":
            elemento["angulo"] = angulo[i]  # Se pasa el ángulo desde la lista

        elementos.append(elemento)

    return elementos
