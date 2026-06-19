import pytest
from payflow_pago import procesar_pago

def test_pago_exitoso():
    # 3a: Saldo de 5000 paga Renta de 3500 + 15 comisión. Esperado: 1485
    resultado = procesar_pago("USR01", "Renta", 3500.0, 5000.0)
    
    assert resultado["status"] == "Éxito"
    assert resultado["saldo_restante"] == 1485.0
    assert resultado["folio"].startswith("PAGO-RENTA")

def test_pago_saldo_insuficiente():
    # 3b: Saldo de 1010 intenta pagar Internet por 1000 + 15 comisión. Esperado: Rechazo
    resultado = procesar_pago("USR02", "Internet", 1000.0, 1010.0)
    
    assert resultado["status"] == "Rechazada"
    assert resultado["mensaje"] == "Fondos Insuficientes"
    assert resultado["saldo_restante"] == 1010.0
    assert resultado["folio"] is None

def test_pago_concepto_invalido():
    # 3c: Concepto fuera de Renta, Internet o Luz. Esperado: Rechazo
    resultado = procesar_pago("USR03", "Agua", 500.0, 5000.0)
    
    assert resultado["status"] == "Rechazada"
    assert resultado["mensaje"] == "Concepto inválido"
    assert resultado["saldo_restante"] == 5000.0
    assert resultado["folio"] is None