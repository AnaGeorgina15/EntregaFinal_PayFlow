# test_validador.py
import pytest
from validador_spei import validar_transferencia

# Refactorización: Suite parametrizada que cubre los 6 casos de la Tabla de Decisión
@pytest.mark.parametrize("monto, hora, cuenta, token, estado_esperado", [
    (10000, 23, "Misma", False, "APROBADA"),                 # C1: Misma cuenta (Sin restricciones)
    (2000, 14, "Crédito", False, "APROBADA"),                # C2: Crédito en horario válido (09 a 18)
    (2000, 20, "Crédito", False, "RECHAZADA_POR_POLÍTICA"),  # C3: Crédito fuera de horario
    (4500, 10, "Débito", False, "APROBADA"),                 # C4: Débito monto permitido (<= 5000)
    (6000, 15, "Débito", False, "RECHAZADA_POR_POLÍTICA"),   # C5: Débito monto alto SIN token
    (8000, 11, "Débito", True, "APROBADA")                   # C6: Débito monto alto CON token
])
def test_suite_completa_transferencias(monto, hora, cuenta, token, estado_esperado):
    estado = validar_transferencia(monto, hora, cuenta, token)
    assert estado == estado_esperado