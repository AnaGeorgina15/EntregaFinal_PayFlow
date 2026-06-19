from src.calculadora import calcular_rendimiento

def evaluar_estado_inversion(saldo_actual, monto_inversion, antiguedad_meses, perfil_riesgo):
    if antiguedad_meses < 3 and perfil_riesgo == "Alto":
        return "RECHAZADA"
        
    if monto_inversion > saldo_actual:
        return "RECHAZADA"
        
    porcentaje = (monto_inversion / saldo_actual) * 100
    
    if porcentaje > 50:
        return "INVERSION_RIESGOSA"
    else:
        return "INVERSION_ESTABLE"

def autorizar_inversion(saldo_actual, monto_inversion, antiguedad_meses, perfil_riesgo, tiempo_anios):
    estado = evaluar_estado_inversion(saldo_actual, monto_inversion, antiguedad_meses, perfil_riesgo)
    
    if estado == "RECHAZADA":
        return {
            "monto_final": None,
            "nuevo_estado": "DISPONIBLE",
            "folio_aprobacion": None
        }
        
    monto_final = calcular_rendimiento(monto_inversion, tiempo_anios, perfil_riesgo)
    
    letra_perfil = "B" if perfil_riesgo == "Bajo" else "A"
    letra_estado = "E" if estado == "INVERSION_ESTABLE" else "R"
    folio = f"{letra_perfil}{letra_estado}-{monto_final}"
    
    return {
        "monto_final": monto_final,
        "nuevo_estado": estado,
        "folio_aprobacion": folio
    }