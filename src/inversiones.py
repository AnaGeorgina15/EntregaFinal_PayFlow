# inversiones.py
# Importamos la función matemática de la capa inferior
from calculadora import calcular_rendimiento

def evaluar_estado_inversion(saldo_actual, monto_inversion, antiguedad_meses, perfil_riesgo):
    # Regla 6: Bloquea perfiles de alto riesgo si la cuenta tiene menos de 3 meses
    if antiguedad_meses < 3 and perfil_riesgo == "Alto":
        return "RECHAZADA"
        
    # Regla implícita: Rechaza si el usuario intenta invertir más dinero del que posee
    if monto_inversion > saldo_actual:
        return "RECHAZADA"
        
    # Regla 5: Obtiene qué proporción del saldo actual representa esta inversión
    porcentaje = (monto_inversion / saldo_actual) * 100
    
    # Evalúa si la proporción de la inversión supera la mitad del saldo (50%)
    if porcentaje > 50:
        # Transita al estado de riesgo por comprometer más del 50%
        return "INVERSION_RIESGOSA"
    else:
        # Transita al estado estable por comprometer un porcentaje seguro
        return "INVERSION_ESTABLE"

def autorizar_inversion(saldo_actual, monto_inversion, antiguedad_meses, perfil_riesgo, tiempo_anios):
    # Capa Media: Inicia evaluando las reglas de negocio con la Capa Superior
    estado = evaluar_estado_inversion(saldo_actual, monto_inversion, antiguedad_meses, perfil_riesgo)
    
    # Regla 7: Detiene el flujo y no genera folio si la inversión fue rechazada
    if estado == "RECHAZADA":
        return {
            "monto_final": None,
            "nuevo_estado": "DISPONIBLE", # Regla 4: Mantiene el estado inicial
            "folio_aprobacion": None
        }
        
    # Capa Media: Si es autorizada, delega el cálculo matemático a la Capa Inferior
    monto_final = calcular_rendimiento(monto_inversion, tiempo_anios, perfil_riesgo)
    
    # Regla 9: Asigna el prefijo 'B' o 'A' dependiendo del nivel de riesgo
    letra_perfil = "B" if perfil_riesgo == "Bajo" else "A"
    # Asigna el sufijo 'E' o 'R' dependiendo del estado de inversión obtenido
    letra_estado = "E" if estado == "INVERSION_ESTABLE" else "R"
    # Genera el folio concatenando letras del perfil, estado y el resultado del cálculo
    folio = f"{letra_perfil}{letra_estado}-{monto_final}"
    
    # Regla 8: Retorna el diccionario con la estructura final exigida por el sistema
    return {
        "monto_final": monto_final,
        "nuevo_estado": estado,
        "folio_aprobacion": folio
    }

    