import time
from src.payflow_pago import procesar_pago
from src.inversiones import autorizar_inversion
from src.presupuesto import validar_presupuesto
from src.validador_spei import validar_transferencia

def mostrar_menu():
    print("\n" + "="*50)
    print(" 🚀 BIENVENIDO AL SISTEMA PAYFLOW MVP 🚀 ")
    print("="*50)
    print("1. Configurar Presupuesto Mensual (CU-01)")
    print("2. Pagar Servicio Fijo E2E (Renta/Internet/Luz)")
    print("3. Simular Inversión y Generar Folio")
    print("4. Validar Transferencia SPEI")
    print("5. Salir del Sistema")
    print("="*50)

def modulo_presupuesto():
    print("\n--- [1] Configuración de Presupuesto ---")
    try:
        pmt = float(input("Ingresa el Presupuesto Mensual Total (PMT): $"))
        ahorro = float(input("Meta de Ahorro: $"))
        servicios = float(input("Gastos en Servicios: $"))
        suscripciones = float(input("Gastos en Suscripciones: $"))
        ocio = float(input("Gastos en Ocio: $"))
        
        estado, alertas = validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
        print("\n[Resultado de Configuración]")
        print(f"Estado del Sistema: {estado}")
        if alertas:
            print(f"Alertas disparadas: {', '.join(alertas)}")
        else:
            print("Distribución Saludable. Sin alertas.")
    except ValueError as e:
        print(f"\n[Error] {e}")

def modulo_pago_servicio():
    print("\n--- [2] Módulo de Pago de Servicios Fijos ---")
    usuario = input("ID de Usuario: ")
    concepto = input("Concepto (Renta/Internet/Luz): ")
    try:
        monto = float(input("Monto del recibo: $"))
        saldo = float(input("Saldo actual de la cuenta: $"))
        
        print("\nProcesando pago (Aplicando comisión de $15.00)...")
        time.sleep(1)
        
        resultado = procesar_pago(usuario, concepto, monto, saldo)
        print("\n[Resultado de Transacción E2E]")
        print(f"Estado: {resultado['status']} | Mensaje: {resultado['mensaje']}")
        print(f"Saldo Restante: ${resultado['saldo_restante']}")
        if resultado['folio']:
            print(f"Folio Generado: {resultado['folio']}")
    except ValueError:
        print("\n[Error] Ingresa cantidades numéricas válidas.")

def modulo_inversiones():
    print("\n--- [3] Módulo de Inversiones ---")
    try:
        saldo = float(input("Saldo actual de la cuenta: $"))
        monto = float(input("Monto a invertir: $"))
        antiguedad = int(input("Antigüedad de la cuenta (meses): "))
        perfil = input("Perfil de riesgo (Bajo/Alto): ").capitalize()
        tiempo = int(input("Plazo de inversión (años): "))
        
        print("\nCalculando interés compuesto y evaluando riesgo...")
        time.sleep(1)
        
        resultado = autorizar_inversion(saldo, monto, antiguedad, perfil, tiempo)
        print("\n[Resolución de Inversión]")
        if resultado['nuevo_estado'] == "RECHAZADA":
            print("Estado: RECHAZADA (No cumple con las políticas de fondos o antigüedad)")
        else:
            print(f"Estado Autorizado: {resultado['nuevo_estado']}")
            print(f"Monto Final Proyectado: ${resultado['monto_final']}")
            print(f"Folio de Aprobación: {resultado['folio_aprobacion']}")
    except ValueError:
        print("\n[Error] Ingresa datos válidos.")

def modulo_spei():
    print("\n--- [4] Validador de Transferencias SPEI ---")
    try:
        monto = float(input("Monto a transferir: $"))
        hora = int(input("Hora de la transferencia (Formato 24h, ej. 14): "))
        cuenta = input("Tipo de cuenta destino (Misma/Crédito/Débito): ").capitalize()
        token = input("¿Token activo? (S/N): ").upper() == 'S'
        
        estado = validar_transferencia(monto, hora, cuenta, token)
        print(f"\n[Resolución SPEI]: La transferencia fue {estado}")
    except ValueError:
        print("\n[Error] Ingresa datos válidos.")

def iniciar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '1':
            modulo_presupuesto()
        elif opcion == '2':
            modulo_pago_servicio()
        elif opcion == '3':
            modulo_inversiones()
        elif opcion == '4':
            modulo_spei()
        elif opcion == '5':
            print("\nCerrando PayFlow... ¡Gracias por usar nuestro sistema financiero!")
            break
        else:
            print("\n[!] Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    iniciar_sistema()