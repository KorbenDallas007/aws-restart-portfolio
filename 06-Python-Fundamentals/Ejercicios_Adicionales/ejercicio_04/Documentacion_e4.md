# Ejercicio 4: Calculadora de Alta Precisión (100 decimales)

## Descripción
Este programa implementa una calculadora aritmética avanzada que permite realizar operaciones de suma, resta, multiplicación y división. A diferencia de las calculadoras convencionales, este script utiliza el motor de precisión arbitraria de Python para garantizar que todos los resultados se entreguen con **exactamente 100 decimales**, permitiendo cálculos científicos y financieros de alta fidelidad.

## Conceptos de Python utilizados
- **Módulo `decimal`**: Se utiliza `Decimal` en lugar de `float` para evitar errores de redondeo binario.
- **Configuración de Contexto**: Uso de `getcontext().prec = 110` para establecer un límite de dígitos significativos que soporte la operación y sus decimales.
- **Formateo de Cadenas (`format`)**: El especificador `.100f` obliga al intérprete a imprimir cien posiciones después del punto decimal, rellenando con ceros si es necesario.
- **Gestión de Signos y Flotantes**: El programa procesa correctamente números negativos y notaciones decimales extensas.
- **Validación de Entradas**: Implementación de filtros para evitar opciones de menú inexistentes y manejo de excepciones en la conversión de datos.

## Código del Script (`ejercicio_04.py`)
```python
from decimal import Decimal, getcontext, InvalidOperation

# Configuramos la precisión del contexto global a 110 dígitos 
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
        print(f"⚠️ Error: Opción no válida.")
        return

    # Ingreso de valores con validación para Decimal
    try:
        val1 = input("Ingresa el primer valor: ").strip()
        val2 = input("Ingresa el segundo valor: ").strip()
        
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

    # Formateo del resultado para forzar 100 decimales
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
```

## Instrucciones de ejecución
1. Ejecuta el script: `python ejercicio_04.py`
2. Selecciona una operación (1-4).
3. Ingresa números (positivos, negativos o con decimales).

## Output (Registro Completo de Ejecuciones)
```text
PS D:\Documentos\Projects_GitHub\Python\ejercicio_04> python .\ejercicio_04.py
--- Calculadora de Alta Precisión (100 decimales) ---
Operaciones disponibles:
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)
Elige el número de la operación (1-4): 1
Ingresa el primer valor: 3333333.6434554
Ingresa el segundo valor: -5333333.755

===================================================================================================================
 OPERACIÓN: Suma (+)
-------------------------------------------------------------------------------------------------------------------
 RESULTADO:
 -2000000.1115446000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
===================================================================================================================

PS D:\Documentos\Projects_GitHub\Python\ejercicio_04> python .\ejercicio_04.py
--- Calculadora de Alta Precisión (100 decimales) ---
Operaciones disponibles:
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)
Elige el número de la operación (1-4): 2
Ingresa el primer valor: -653234567.8965
Ingresa el segundo valor: -64456785.788654

===================================================================================================================
 OPERACIÓN: Resta (-)
-------------------------------------------------------------------------------------------------------------------
 RESULTADO:
 -588777782.1078460000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
===================================================================================================================

PS D:\Documentos\Projects_GitHub\Python\ejercicio_04> python .\ejercicio_04.py
Operaciones disponibles:
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)

Elige el número de la operación (1-4): 3
Ingresa el primer valor: -76543.76544
Ingresa el segundo valor: -9087654.87654

===================================================================================================================
 OPERACIÓN: Multiplicación (*)
-------------------------------------------------------------------------------------------------------------------
 RESULTADO:
 695603323269.5499187776000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
===================================================================================================================

PS D:\Documentos\Projects_GitHub\Python\ejercicio_04> python .\ejercicio_04.py
Operaciones disponibles:
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)

Elige el número de la operación (1-4): 4
Ingresa el primer valor: 0
Ingresa el segundo valor: -5855555555555.99944444

===================================================================================================================
 OPERACIÓN: División (/)
-------------------------------------------------------------------------------------------------------------------
 RESULTADO:
 -0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
===================================================================================================================

PS D:\Documentos\Projects_GitHub\Python\ejercicio_04> python .\ejercicio_04.py
--- Calculadora de Alta Precisión (100 decimales) ---
Operaciones disponibles:
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)

Elige el número de la operación (1-4): 4
Ingresa el primer valor: -9655855555.6545555
Ingresa el segundo valor: -99999999999999999.9999999999999

===================================================================================================================
 OPERACIÓN: División (/)
-------------------------------------------------------------------------------------------------------------------
 RESULTADO:
 0.0000000965585555565455550000000000000965585555565455550000000000000965585555565455550000000000000966
===================================================================================================================
```