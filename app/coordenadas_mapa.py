ANCHO_MAPA_M = 20
ALTO_MAPA_M = 15

def metros_a_css_porcentaje(x, y):
    left_pct = (x / ANCHO_MAPA_M) * 100
    # Flip the top calculation by subtracting from the map height
    top_pct = ((ALTO_MAPA_M - y) / ALTO_MAPA_M) * 100
    return {
        "left": f"{left_pct:.2f}%",
        "top": f"{top_pct:.2f}%"
    }