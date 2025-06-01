# converciones.py

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
    x = min(max(x, 0), ANCHO_MAPA_M)
    y = min(max(y, 0), ALTO_MAPA_M)

    left_pct = (x / ANCHO_MAPA_M) * 100
    top_pct = ((ALTO_MAPA_M - y) / ALTO_MAPA_M) * 100  # Inversión del eje Y

    return {
        "left": f"{left_pct:.2f}%",
        "top": f"{top_pct:.2f}%"
    }


def numero_para_lista_binaria(num_elementos):
    """
    Genera una lista binaria con la misma cantidad de bits que el número de elementos.
    """
    binario = bin(num_elementos)[2:].zfill(num_elementos)  # Convierte el número total de semáforos en binario
    return [int(bit) for bit in binario[-num_elementos:]]  # Usa solo los bits necesarios


def obtener_elementos(tipo, x, y, angulo, num_elementos):
    """
    Obtiene las coordenadas de los elementos en formato CSS,
    asignando un bit aleatorio a cada uno. Permite definir X, Y y el ángulo para AGVs.
    """
    elementos = []
    binario = numero_para_lista_binaria(num_elementos)

    for i in range(num_elementos):
        elemento = metros_a_css_porcentaje(x[i], y[i])  # Conversión a CSS
        elemento["color"] = binario[i]  # Asigna color aleatorio
        elemento["id"] = f"{tipo}-{i}"

        # Si el elemento es un AGV, agregar el ángulo definido
        if tipo == "agv":
            elemento["angulo"] = angulo[i]

        elementos.append(elemento)

    return elementos
