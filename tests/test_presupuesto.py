# tests/test_presupuesto.py
import pytest
from src.presupuesto import validar_presupuesto

@pytest.mark.parametrize("pmt, ahorro, serv, susc, ocio", [
    (0, 100, 50, 50, 50),
    (-100, 150, 50, 50, 50),
    (1000, -50, 50, 50, 50)
])
def test_excepciones_valores_invalidos(pmt, ahorro, serv, susc, ocio):
    with pytest.raises(ValueError):
        validar_presupuesto(pmt, ahorro, serv, susc, ocio)

@pytest.mark.parametrize("pmt, ahorro, serv, susc, ocio, estado_esperado, alerta_esperada", [
    (100, 150, 50, 50, 50, "EJERCICIO_DEFICIT", "Déficit detectado en Ahorro"),
    (200, 100, 150, 50, 50, "EJERCICIO_DEFICIT", "Déficit detectado en Servicios"),
    (300, 100, 100, 150, 50, "EJERCICIO_DEFICIT", "Déficit detectado en Suscripciones"),
    (400, 100, 100, 100, 150, "EJERCICIO_DEFICIT", "Déficit detectado en Ocio"),
    (1000, 100, 100, 100, 150, "EJERCICIO", None)
])
def test_suite_completa_prioridades(pmt, ahorro, serv, susc, ocio, estado_esperado, alerta_esperada):
    estado, alertas = validar_presupuesto(pmt, ahorro, serv, susc, ocio)
    assert estado == estado_esperado
    if alerta_esperada:
        assert alerta_esperada in alertas
    else:
        assert len(alertas) == 0