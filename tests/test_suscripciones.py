# test_suscripciones.py
import pytest
from procesador_pagos import procesar_transaccion

# TC-01: Regla 4 - Jerarquía de Fondos (Priorización de Ahorro)
def test_alerta_deficit_ahorro():
    resultado = procesar_transaccion(pmt=100, ahorro_meta=150, monto_gasto=0)
    assert resultado["alerta"] == "Déficit de Ahorro"
    assert resultado["estado_salud"] == "Crítico"

# TC-02: Regla 1 - Pago Exitoso (Estado Ideal)
def test_pago_exitoso_saludable():
    # PMT=1000, Ahorro=200, Gasto=100 (No es ocio)
    resultado = procesar_transaccion(pmt=1000, ahorro_meta=200, monto_gasto=100, es_ocio=False)
    assert resultado["estado_suscripcion"] == "Pagada"
    assert resultado["estado_salud"] == "Saludable"

# TC-03: Regla 2 - Protección de Suscripciones (Riesgo por Ocio)
def test_advertencia_riesgo_ocio():
    # El gasto es de ocio y deja poco saldo para la suscripción fija de mañana
    resultado = procesar_transaccion(pmt=500, ahorro_meta=100, monto_gasto=380, es_ocio=True, compromete_fija=True)
    assert resultado["alerta"] == "Advertencia de Riesgo"
    assert resultado["estado_salud"] == "En Riesgo"

# TC-04: Regla 3 - Saldo Insuficiente (Suscripción Vencida)
def test_suscripcion_vencida_sin_saldo():
    # El gasto (500) supera el saldo disponible (PMT 400 - Ahorro 100 = 300)
    resultado = procesar_transaccion(pmt=400, ahorro_meta=100, monto_gasto=500)
    assert resultado["estado_suscripcion"] == "Vencida"
    assert resultado["estado_salud"] == "Crítico"