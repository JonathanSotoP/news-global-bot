def analyze_impact(text):

    text = text.lower()

    impacts = []

    if "oil" in text or "energy" in text:
        impacts.append("Podría provocar aumentos en el precio de los combustibles en Chile, lo que impactaría transporte, inflación y costos logísticos.")

    if "china" in text or "trade" in text:
        impacts.append("Podría afectar el comercio internacional y las exportaciones chilenas, especialmente cobre, litio y otros recursos naturales.")

    if "inflation" in text or "interest rate" in text:
        impacts.append("Podría generar presión sobre el dólar en Chile y afectar tasas de interés, inflación y el costo del crédito.")

    if "war" in text or "conflict" in text:
        impacts.append("Los conflictos geopolíticos suelen generar volatilidad en los mercados globales, lo que puede impactar el tipo de cambio y la estabilidad económica en Chile.")

    if "economy" in text or "recession" in text:
        impacts.append("Una desaceleración económica global podría reducir la demanda de materias primas, afectando el crecimiento económico de Chile.")

    if len(impacts) == 0:
        impacts.append("El impacto directo en Chile es incierto, pero cambios en la economía global pueden afectar mercados financieros y comercio internacional.")

    return impacts
