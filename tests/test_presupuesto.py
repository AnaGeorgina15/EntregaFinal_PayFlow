# test_presupuesto.py
import pytest
from presupuesto import validar_presupuesto

# A. PRUEBA DE EXCEPCIONES PARAMETRIZADA
@pytest.mark.parametrize("pmt, ahorro, serv, susc, ocio", [
    (0, 100, 50, 50, 50),     # Caso: PMT igual a cero
    (-100, 150, 50, 50, 50),  # Caso: PMT negativo
    (1000, -50, 50, 50, 50)   # Caso: Otro valor negativo
])
def test_excepciones_valores_invalidos(pmt, ahorro, serv, susc, ocio):
    with pytest.raises(ValueError):
        validar_presupuesto(pmt, ahorro, serv, susc, ocio)


# B. SUITE COMPLETA DE PRIORIDADES PARAMETRIZADA (Los 5 Tests en 1)
@pytest.mark.parametrize("pmt, ahorro, serv, susc, ocio, estado_esperado, alerta_esperada", [
    (100, 150, 50, 50, 50, "EJERCICIO_DEFICIT", "Déficit detectado en Ahorro"),         # Test 1
    (200, 100, 150, 50, 50, "EJERCICIO_DEFICIT", "Déficit detectado en Servicios"),     # Test 2
    (300, 100, 100, 150, 50, "EJERCICIO_DEFICIT", "Déficit detectado en Suscripciones"),# Test 3
    (400, 100, 100, 100, 150, "EJERCICIO_DEFICIT", "Déficit detectado en Ocio"),        # Test 4
    (1000, 100, 100, 100, 150, "EJERCICIO", None)                                       # Test 5 (Feliz)
])
def test_suite_completa_prioridades(pmt, ahorro, serv, susc, ocio, estado_esperado, alerta_esperada):
    estado, alertas = validar_presupuesto(pmt, ahorro, serv, susc, ocio)
    
    assert estado == estado_esperado
    if alerta_esperada:
        assert alerta_esperada in alertas
    else:
        assert len(alertas) == 0