# tests/test_validador.py
import pytest
from src.validador_spei import validar_transferencia

@pytest.mark.parametrize("monto, hora, cuenta, token, estado_esperado", [
    (10000, 23, "Misma", False, "APROBADA"),
    (2000, 14, "Crédito", False, "APROBADA"),
    (2000, 20, "Crédito", False, "RECHAZADA_POR_POLÍTICA"),
    (4500, 10, "Débito", False, "APROBADA"),
    (6000, 15, "Débito", False, "RECHAZADA_POR_POLÍTICA"),
    (8000, 11, "Débito", True, "APROBADA")
])
def test_suite_completa_transferencias(monto, hora, cuenta, token, estado_esperado):
    assert validar_transferencia(monto, hora, cuenta, token) == estado_esperado