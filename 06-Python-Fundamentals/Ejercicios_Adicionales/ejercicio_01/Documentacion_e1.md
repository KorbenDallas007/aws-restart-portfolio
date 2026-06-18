# Ejercicio 1: Captura de Datos de Usuario (Versión Pro)

## Descripción
Este programa solicita información personal al usuario para el registro en el programa AWS Re/Start. A diferencia de una captura simple, esta versión implementa:
1.  **Limpieza de datos**: Uso de métodos de cadena para normalizar nombres (mayúsculas/minúsculas).
2.  **Validación de tipos**: Un bucle que asegura que la edad sea un dato numérico antes de continuar.
3.  **Formateo visual**: Uso de caracteres especiales y alineación de texto para presentar los datos en una tabla estética por consola.

## Conceptos de Python utilizados
- **Métodos de String**: `.strip()` para eliminar espacios y `.title()` para capitalizar nombres correctamente (ej: `alejANDRO` -> `Alejandro`).
- **Control de Errores**: Bucle `while True` con condicional `.isdigit()` para validar entradas del usuario.
- **Interpolación Avanzada**: Uso de f-strings con modificadores de alineación (`:<25`) para crear columnas uniformes.
- **Punto de Entrada**: Estructura `if __name__ == "__main__":`.

## Código del Script (`ejercicio_01.py`)
```python
def solicitar_informacion():
    """
    Función que solicita datos al usuario, los valida y los imprime con formato.
    """
    print("--- Registro de Estudiante AWS Re/Start (Versión Pro) ---")
    
    # Solicitud de datos con limpieza (.strip() quita espacios extras y .title() capitaliza)
    nombre = input("Introduce tu nombre: ").strip().title()
    apellido = input("Introduce tu apellido: ").strip().title()
    
    # Validación de edad (asegura que sea un número)
    while True:
        edad_input = input("Introduce tu edad: ").strip()
        if edad_input.isdigit():
            edad = int(edad_input)
            break
        else:
            print("⚠️ Error: Por favor, introduce un número válido para la edad.")

    ciudad = input("¿En qué ciudad resides?: ").strip().title()
    puesto_objetivo = input("¿Qué rol te gustaría tener en el mundo Cloud?: ").strip()

    # Impresión de datos con formato
    print("\n" + "╔" + "═"*38 + "╗")
    print("║      PERFIL DEL ESTUDIANTE AWS       ║")
    print("╠" + "═"*38 + "╣")
    print(f"║ Nombre:    {nombre + ' ' + apellido:<25} ║")
    print(f"║ Edad:      {edad:<25} ║")
    print(f"║ Ubicación: {ciudad:<25} ║")
    print(f"║ Objetivo:  {puesto_objetivo:<25} ║")
    print("╚" + "═"*38 + "╝")

if __name__ == "__main__":
    solicitar_informacion()
```

## Output (Resultado Real en Consola)
```text
PS D:\Documentos\Projects_GitHub\Python\ejercicio_01> python ejercicio_01.py
--- Registro de Estudiante AWS Re/Start (Versión Pro) ---
Introduce tu nombre: alejANDRO
Introduce tu apellido: bARREnechea
Introduce tu edad: _a 49
⚠️ Error: Por favor, introduce un número válido para la edad.
Introduce tu edad: 49
¿En qué ciudad resides?: Buin
¿Qué rol te gustaría tener en el mundo Cloud?: SA

╔══════════════════════════════════════╗
║      PERFIL DEL ESTUDIANTE AWS       ║
╠══════════════════════════════════════╣
║ Nombre:    Alejandro Barrenechea     ║
║ Edad:      49                        ║
║ Ubicación: Buin                      ║
║ Objetivo:  SA                        ║
╚══════════════════════════════════════╝
```