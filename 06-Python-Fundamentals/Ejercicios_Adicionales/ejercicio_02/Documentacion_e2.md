# Ejercicio 2: Conteo de Caracteres y Análisis de Texto Multilínea

## Descripción
Este programa permite capturar y analizar bloques de texto extensos, incluyendo múltiples párrafos y saltos de línea. A diferencia de una captura simple, esta herramienta utiliza la entrada estándar del sistema para procesar el texto completo, devolviendo métricas precisas sobre la cantidad de caracteres (con y sin espacios), el total de palabras y el número de líneas procesadas.

## Conceptos de Python utilizados
- **`import sys`**: Módulo que permite interactuar con el intérprete. Se utiliza `sys.stdin.read()` para capturar texto hasta encontrar un carácter de fin de archivo (EOF), permitiendo múltiples líneas.
- **`len()`**: Función para obtener la longitud de la cadena de texto.
- **`split()`**: Método que divide el texto en una lista de palabras basándose en cualquier espacio en blanco (incluyendo tabulaciones y saltos de línea).
- **`count('\n')`**: Método para contar los saltos de línea y determinar el total de líneas del texto.
- **F-Strings con Alineación**: Uso de modificadores como `:<10` para tabular los resultados numéricos y presentar una interfaz limpia en consola.

## Código del Script (`ejercicio_02.py`)
```python
import sys

def analizar_multilinea():
    """
    Solicita un texto de una o más líneas al usuario y realiza un análisis estadístico.
    """
    print("--- Analizador de Texto Multilinea ---")
    print("Escribe o pega tu texto. Para finalizar y ver los resultados:")
    print("- En Windows: Presiona Enter, luego Ctrl+Z y Enter.")
    print("- En Linux/Mac: Presiona Enter y luego Ctrl+D.")
    print("-" * 40)

    # Leemos todo el contenido de la entrada estándar
    entrada = sys.stdin.read()
    
    # Limpiamos espacios innecesarios en los extremos
    texto = entrada.strip()

    if not texto:
        print("\n⚠️ Error: No has ingresado ningún contenido para analizar.")
        return

    # Procesamiento de métricas
    total_caracteres_con_espacios = len(texto)
    total_caracteres_sin_espacios = len("".join(texto.split()))
    total_palabras = len(texto.split())
    total_lineas = texto.count('\n') + 1 if texto else 0

    # Presentación de resultados
    print("\n" + "╔" + "═"*42 + "╗")
    print("║          RESULTADO DEL ANÁLISIS          ║")
    print("╠" + "═"*42 + "╣")
    print(f"║ Caracteres (con espacios):    {total_caracteres_con_espacios:<10} ║")
    print(f"║ Caracteres (sin espacios):    {total_caracteres_sin_espacios:<10} ║")
    print(f"║ Total de palabras:            {total_palabras:<10} ║")
    print(f"║ Total de líneas:              {total_lineas:<10} ║")
    print("╚" + "═"*42 + "╝")

if __name__ == "__main__":
    analizar_multilinea()
```

## Output (Resultado Real en Consola)
```text
PS D:\Documentos\Projects_GitHub\Python\ejercicio_02> python ejercicio_02.py
--- Analizador de Texto Multilinea ---
Escribe o pega tu texto. Para finalizar y ver los resultados:
- En Windows: Presiona Enter, luego Ctrl+Z y Enter.
- En Linux/Mac: Presiona Enter y luego Ctrl+D.
----------------------------------------
The Economist lo advierte en su edición pasada: la crisis energética global está empujando la inflación nuevamente hacia niveles que los bancos centrales ya creían superados.
El análisis es fuerte: cuando los costos energéticos suben con fuerza, las empresas enfrentan un doble golpe. Primero disminuyen los márgenes. Luego, los clientes ajustan su gasto. Y el flujo de caja que parecía estable deja de serlo.
Lo que describe la revista para las grandes economías del mundo, las pymes chilenas lo sufren a su propia escala y con menos margen de error.
En Gestión Integral Consultores acompañamos a emprendedores y gerentes a tener claridad financiera precisamente en momentos como este: conocer los costos reales del negocio, revisar la estructura tributaria y proyectar el flujo de caja con anticipación no es un lujo, es la diferencia entre reaccionar tarde o tomar decisiones a tiempo.
La incertidumbre global no se controla. La gestión de tu empresa, sí.

www.giconsultores.cl

#GestiónFinanciera #PymesChile #Inflación #PlanificaciónEmpresarial #GIConsultores
^Z

╔══════════════════════════════════════════╗
║          RESULTADO DEL ANÁLISIS          ║
╠══════════════════════════════════════════╣
║ Caracteres (con espacios):    1064       ║
║ Caracteres (sin espacios):    904        ║
║ Total de palabras:            159        ║
║ Total de líneas:              9          ║
╚══════════════════════════════════════════╝
```