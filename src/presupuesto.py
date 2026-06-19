# presupuesto.py
def validar_presupuesto(pmt, ahorro_meta, serv_hist, susc_fijas, ocio_hist):
    # 1. VALIDACIÓN DE EXCEPCIONES (PMT 0 o valores negativos)
    if pmt <= 0 or ahorro_meta < 0 or serv_hist < 0 or susc_fijas < 0 or ocio_hist < 0:
        raise ValueError("Valores inválidos: No se admiten negativos ni PMT en cero")

    alertas_lista = []
    
    # Prioridad 1: Ahorro
    if pmt < ahorro_meta:
        alertas_lista.append("Déficit detectado en Ahorro")
        return "EJERCICIO_DEFICIT", alertas_lista
        
    saldo_restante = pmt - ahorro_meta
    
    # Prioridad 2: Servicios
    if saldo_restante < serv_hist:
        alertas_lista.append("Déficit detectado en Servicios")
        return "EJERCICIO_DEFICIT", alertas_lista
        
    saldo_restante -= serv_hist
    
    # Prioridad 3: Suscripciones Fijas Digitales
    if saldo_restante < susc_fijas:
        alertas_lista.append("Déficit detectado en Suscripciones")
        return "EJERCICIO_DEFICIT", alertas_lista
        
    saldo_restante -= susc_fijas
    
    # Prioridad 4: Ocio
    if saldo_restante < ocio_hist:
        alertas_lista.append("Déficit detectado en Ocio")
        return "EJERCICIO_DEFICIT", alertas_lista
        
    # Flujo Feliz
    return "EJERCICIO", []

