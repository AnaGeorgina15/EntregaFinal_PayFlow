def validar_transferencia(monto, hora_transferencia, tipo_cuenta, token_activo=False):
    if tipo_cuenta == "Misma":
        return "APROBADA"
        
    if tipo_cuenta == "Crédito":
        if 9 <= hora_transferencia <= 18:
            return "APROBADA"
        else:
            return "RECHAZADA_POR_POLÍTICA"
            
    if tipo_cuenta == "Débito":
        if monto <= 5000:
            return "APROBADA"
        elif monto > 5000 and token_activo:
            return "APROBADA"
        else:
            return "RECHAZADA_POR_POLÍTICA"
            
    return "RECHAZADA_POR_POLÍTICA"