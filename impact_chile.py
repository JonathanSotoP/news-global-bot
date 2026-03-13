def analyze_impact(text):
    text = text.lower()
    impacts = []

    if "oil" in text or "energy" in text:
        impacts.append("posible alza de combustibles en Chile")

    if "china" in text or "commodities" in text:
        impacts.append("impacto potencial en el precio del cobre")

    if "interest rate" in text or "inflation" in text:
        impacts.append("posible presión en el dólar y tasas en Chile")

    if "war" in text or "conflict" in text:
        impacts.append("volatilidad en mercados globales que puede afectar la economía chilena")

    if len(impacts) == 0:
        impacts.append("posible impacto indirecto en comercio internacional")

    return impacts[:3]