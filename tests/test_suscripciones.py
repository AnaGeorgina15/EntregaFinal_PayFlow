# tests/test_suscripciones.py
import pytest
from src.procesador_pagos import procesar_transaccion

def test_alerta_deficit_ahorro():
    resultado = procesar_transaccion(pmt=100, ahorro_meta=150, monto_gasto=0)
    assert resultado["alerta"] == "Déficit de Ahorro"
    assert resultado["estado_salud"] == "Crítico"

def test_pago_exitoso_saludable():
    resultado = procesar_transaccion(pmt=1000, ahorro_meta=200, monto_gasto=100, es_ocio=False)
    assert resultado["estado_suscripcion"] == "Pagada"
    assert resultado["estado_salud"] == "Saludable"

def test_advertencia_riesgo_ocio():
    resultado = procesar_transaccion(pmt=500, ahorro_meta=100, monto_gasto=380, es_ocio=True, compromete_fija=True)
    assert resultado["alerta"] == "Advertencia de Riesgo"
    assert resultado["estado_salud"] == "En Riesgo"

def test_suscripcion_vencida_sin_saldo():
    resultado = procesar_transaccion(pmt=400, ahorro_meta=100, monto_gasto=500)
    assert resultado["estado_suscripcion"] == "Vencida"
    assert resultado["estado_salud"] == "Crítico"