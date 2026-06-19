# tests/test_inversiones.py
import pytest
from src.calculadora import calcular_rendimiento
from src.inversiones import evaluar_estado_inversion, autorizar_inversion

def test_calculo_bajo_riesgo():
    assert calcular_rendimiento(1000, 2, "Bajo") == 1102.5

def test_calculo_alto_riesgo():
    assert calcular_rendimiento(1000, 2, "Alto") == 1254.4

def test_validaciones_calculadora():
    with pytest.raises(ValueError, match="El monto no puede ser negativo"):
        calcular_rendimiento(-100, 2, "Bajo")
        
    with pytest.raises(ValueError, match="El plazo mínimo es de 1 año"):
        calcular_rendimiento(1000, 0.5, "Alto")

def test_evaluar_estado_estable():
    assert evaluar_estado_inversion(10000, 4000, 6, "Bajo") == "INVERSION_ESTABLE"

def test_evaluar_estado_rechazada_por_saldo():
    assert evaluar_estado_inversion(1000, 5000, 6, "Bajo") == "RECHAZADA"

def test_integracion_inversion_exitosa(mocker):
    # OJO AQUÍ: El mock ahora apunta a src.inversiones
    mock_calculadora = mocker.patch('src.inversiones.calcular_rendimiento', return_value=1251.0)
    
    resultado = autorizar_inversion(10000, 4000, 6, "Bajo", 2)
    
    assert resultado["nuevo_estado"] == "INVERSION_ESTABLE"
    assert resultado["folio_aprobacion"] == "BE-1251.0"
    mock_calculadora.assert_called_once_with(4000, 2, "Bajo")