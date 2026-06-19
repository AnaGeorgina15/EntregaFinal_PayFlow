from datetime import datetime

COMISION = 15.0

# 1a. Función A (Capa Superior - Validación)
def validar_disponibilidad(saldo, monto):
    # Solo dice "SÍ" (True) o "NO" (False)
    if saldo >= (monto + COMISION):
        return True
    return False

# 1b. Función B (Capa Inferior - Cálculo)
def aplicar_descuento(saldo, monto):
    # Realiza la operación matemática pura
    return saldo - monto - COMISION

# 1c. Función C (Capa Media - Formateo)
def generar_comprobante(concepto):
    # Genera el texto del folio o comprobante
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"PAGO-{concepto.upper()}{timestamp}"

# 2. Orquestador del proceso de negocio (MVP)
def procesar_pago(id_usuario, concepto, monto, saldo_disponible):
    conceptos_validos = ["Renta", "Internet", "Luz"]
    
    # Validar concepto (Evitar que afecte el saldo si es inválido)
    if concepto not in conceptos_validos:
        return {
            "status": "Rechazada", 
            "mensaje": "Concepto inválido", 
            "saldo_restante": saldo_disponible, 
            "folio": None
        }
        
    # Validar disponibilidad (Función A)
    if not validar_disponibilidad(saldo_disponible, monto):
        return {
            "status": "Rechazada", 
            "mensaje": "Fondos Insuficientes", 
            "saldo_restante": saldo_disponible, 
            "folio": None
        }
        
    # Ejecutar descuento (Función B)
    nuevo_saldo = aplicar_descuento(saldo_disponible, monto)
    
    # Emitir comprobante (Función C)
    folio = generar_comprobante(concepto)
    
    # Retornar objeto E2E inmutable
    return {
        "status": "Éxito", 
        "mensaje": "Pago realizado", 
        "saldo_restante": nuevo_saldo, 
        "folio": folio
    }