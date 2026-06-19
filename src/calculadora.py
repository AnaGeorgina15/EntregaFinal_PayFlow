# calculadora.py

def calcular_rendimiento(capital, tiempo_anios, perfil_riesgo):
    # Validación de montos negativos y plazos cortos
    if capital < 0:
        raise ValueError("El monto no puede ser negativo")
    if tiempo_anios < 1:
        raise ValueError("El plazo mínimo es de 1 año")

    # Asignación de tasa anual según el perfil
    if perfil_riesgo == "Bajo":
        tasa = 0.05
    elif perfil_riesgo == "Alto":
        tasa = 0.12
    else:
        raise ValueError("Perfil no válido")

    # Cálculo de la fórmula de interés compuesto
    monto_final = capital * ((1 + tasa) ** tiempo_anios)
    
    # Redondeo financiero a dos decimales
    return round(monto_final, 2)
    