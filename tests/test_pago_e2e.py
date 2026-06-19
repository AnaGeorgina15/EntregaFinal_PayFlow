# tests/test_pago_e2e.py
import pytest
from src.payflow_pago import procesar_pago

def test_pago_exitoso():
    resultado = procesar_pago("USR01", "Renta", 3500.0, 5000.0)
    assert resultado["status"] == "Éxito"
    assert resultado["saldo_restante"] == 1485.0
    assert resultado["folio"].startswith("PAGO-RENTA")

def test_pago_saldo_insuficiente():
    resultado = procesar_pago("USR02", "Internet", 1000.0, 1010.0)
    assert resultado["status"] == "Rechazada"
    assert resultado["mensaje"] == "Fondos Insuficientes"
    assert resultado["folio"] is None

def test_pago_concepto_invalido():
    resultado = procesar_pago("USR03", "Agua", 500.0, 5000.0)
    assert resultado["status"] == "Rechazada"
    assert resultado["mensaje"] == "Concepto inválido"