
def procesar_transaccion(pmt, ahorro_meta, monto_gasto, es_ocio=False, compromete_fija=False):
    if pmt < ahorro_meta:
        return {
            "alerta": "Déficit de Ahorro",
            "estado_salud": "Crítico",
            "estado_suscripcion": "Suspendida"
        }
    
    saldo_disponible = pmt - ahorro_meta
    
    if monto_gasto > saldo_disponible:
        return {
            "alerta": "Saldo Insuficiente",
            "estado_salud": "Crítico",
            "estado_suscripcion": "Vencida"
        }
    
    if es_ocio and compromete_fija:
        return {
            "alerta": "Advertencia de Riesgo",
            "estado_salud": "En Riesgo",
            "estado_suscripcion": "Pendiente"
        }
    
    return {
        "alerta": None,
        "estado_salud": "Saludable",
        "estado_suscripcion": "Pagada"
    }