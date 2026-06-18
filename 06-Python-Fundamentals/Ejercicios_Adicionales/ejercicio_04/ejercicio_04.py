from decimal import Decimal, getcontext, InvalidOperation

# Configuramos la precisión del contexto global a 110 dígitos 
# (100 decimales + margen para la parte entera)
getcontext().prec = 110

def calculadora_alta_precision():
    """
    Realiza operaciones matemáticas con una precisión de 100 decimales
    utilizando el módulo decimal de Python.
    """
    print("--- Calculadora de Alta Precisión (100 decimales) ---")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    
    opcion = input("\nElige el número de la operación (1-4): ").strip()
    
    if opcion not in ['1', '2', '3', '4']:
        print("⚠️ Error: Opción no válida.")
        return

    # Ingreso de valores con validación para Decimal
    try:
        val1 = input("Ingresa el primer valor: ").strip()
        val2 = input("Ingresa el segundo valor: ").strip()
        
        # Convertimos a tipo Decimal para mantener la precisión
        num1 = Decimal(val1)
        num2 = Decimal(val2)
    except InvalidOperation:
        print("⚠️ Error: Los valores ingresados no son números válidos.")
        return

    # Procesamiento del cálculo
    resultado = None
    operacion_nombre = ""
    simbolo = ""

    if opcion == '1':
        resultado = num1 + num2
        operacion_nombre = "Suma"
        simbolo = "+"
    elif opcion == '2':
        resultado = num1 - num2
        operacion_nombre = "Resta"
        simbolo = "-"
    elif opcion == '3':
        resultado = num1 * num2
        operacion_nombre = "Multiplicación"
        simbolo = "*"
    elif opcion == '4':
        if num2 == 0:
            print("⚠️ Error crítico: No es posible dividir por cero.")
            return
        resultado = num1 / num2
        operacion_nombre = "División"
        simbolo = "/"

    # Formateo del resultado para forzar 100 decimales (.100f)
    resultado_formateado = format(resultado, '.100f')

    # Presentación del resultado
    print("\n" + "="*115)
    print(f" OPERACIÓN: {operacion_nombre} ({simbolo})")
    print("-" * 115)
    print(f" RESULTADO:")
    print(f" {resultado_formateado}")
    print("=" * 115)

if __name__ == "__main__":
    calculadora_alta_precision()