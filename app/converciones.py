# converciones.py

# Escala: 1 pixel = 0.05 metros
ESCALA_METROS_POR_PIXEL = 0.05

# Dimensões reais do mapa em metros (baseadas no tamanho da imagem em pixels)
ANCHO_MAPA_M = 979 * ESCALA_METROS_POR_PIXEL  # 48.95
ALTO_MAPA_M = 599 * ESCALA_METROS_POR_PIXEL  # 29.95

def metros_a_css_porcentaje(x, y):
    """
    Converte coordenadas (x, y) em metros para porcentagem CSS
    baseada no tamanho do mapa e no sistema de coordenadas invertido do CSS.
    """
    left_pct = (x / ANCHO_MAPA_M) * 100
    top_pct = ((ALTO_MAPA_M - y) / ALTO_MAPA_M) * 100  # inverte o eixo Y
    return {
        "left": f"{left_pct:.2f}%",
        "top": f"{top_pct:.2f}%"
    }