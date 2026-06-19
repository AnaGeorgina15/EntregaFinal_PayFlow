from datetime import datetime

COMISION = 15.0

def validar_disponibilidad(saldo, monto):
    if saldo >= (monto + COMISION):
        return True
    return False

def aplicar_descuento(saldo, monto):
    return saldo - monto - COMISION

def generar_comprobante(concepto):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"PAGO-{concepto.upper()}{timestamp}"

def procesar_pago(id_usuario, concepto, monto, saldo_disponible):
    conceptos_validos = ["Renta", "Internet", "Luz"]
    
    if concepto not in conceptos_validos:
        return {
            "status": "Rechazada", 
            "mensaje": "Concepto inválido", 
            "saldo_restante": saldo_disponible, 
            "folio": None
        }
        
    if not validar_disponibilidad(saldo_disponible, monto):
        return {
            "status": "Rechazada", 
            "mensaje": "Fondos Insuficientes", 
            "saldo_restante": saldo_disponible, 
            "folio": None
        }
    nuevo_saldo = aplicar_descuento(saldo_disponible, monto)
    folio = generar_comprobante(concepto)
    
    return {
        "status": "Éxito", 
        "mensaje": "Pago realizado", 
        "saldo_restante": nuevo_saldo, 
        "folio": folio
    }

    