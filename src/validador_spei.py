# validador_spei.py
def validar_transferencia(monto, hora_transferencia, tipo_cuenta, token_activo=False):
    # Regla 3: Si es la misma cuenta, pasa directo.
    if tipo_cuenta == "Misma":
        return "APROBADA"
        
    # Regla 1: Transferencias a Crédito (Horario de 09:00 a 18:00 hrs)
    if tipo_cuenta == "Crédito":
        if 9 <= hora_transferencia <= 18:
            return "APROBADA"
        else:
            return "RECHAZADA_POR_POLÍTICA"
            
    # Regla 2: Transferencias a Débito (Monto y Token)
    if tipo_cuenta == "Débito":
        if monto <= 5000:
            return "APROBADA"
        elif monto > 5000 and token_activo:
            return "APROBADA"
        else:
            return "RECHAZADA_POR_POLÍTICA"
            
    # Estado final por defecto si entra un tipo de cuenta desconocido (Regla 4)
    return "RECHAZADA_POR_POLÍTICA"