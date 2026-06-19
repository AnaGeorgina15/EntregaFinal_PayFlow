# test_inversiones.py
import pytest
from calculadora import calcular_rendimiento
from inversiones import evaluar_estado_inversion, autorizar_inversion

# --- Pruebas de la Capa Inferior ---
def test_calculo_bajo_riesgo():
    resultado = calcular_rendimiento(1000, 2, "Bajo")
    assert resultado == 1102.5

def test_calculo_alto_riesgo():
    resultado = calcular_rendimiento(1000, 2, "Alto")
    assert resultado == 1254.4

def test_validaciones_calculadora():
    with pytest.raises(ValueError, match="El monto no puede ser negativo"):
        calcular_rendimiento(-100, 2, "Bajo")
        
    with pytest.raises(ValueError, match="El plazo mínimo es de 1 año"):
        calcular_rendimiento(1000, 0.5, "Alto")

# --- Pruebas de la Capa Superior ---
def test_evaluar_estado_estable():
    estado = evaluar_estado_inversion(10000, 4000, 6, "Bajo")
    assert estado == "INVERSION_ESTABLE"

# --- Prueba de la Capa Media (Sandwich Testing) ---
def test_integracion_inversion_exitosa(mocker):
    # Parcheamos la capa inferior para controlar el resultado matemático
    mock_calculadora = mocker.patch(
        'inversiones.calcular_rendimiento',
        return_value=1251.0
    )
    
    # Ejecutamos la integración global
    resultado = autorizar_inversion(10000, 4000, 6, "Bajo", 2)
    
    # Verificamos estructura y el Mock
    assert resultado["nuevo_estado"] == "INVERSION_ESTABLE"
    assert resultado["folio_aprobacion"] == "BE-1251.0"
    mock_calculadora.assert_called_once_with(4000, 2, "Bajo")


def test_evaluar_estado_rechazada_por_saldo():
    # Resolución de Bug 2 (Tarjeta 2): Prueba para cubrir el rechazo por saldo insuficiente
    # Saldo: 1000, Intento de inversión: 5000 (Supera el saldo)
    estado = evaluar_estado_inversion(1000, 5000, 6, "Bajo")
    
    # El sistema debe protegerse y rechazar la operación
    assert estado == "RECHAZADA"