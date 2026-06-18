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

    # Leemos todo el contenido de la entrada estándar (soporta múltiples líneas)
    entrada = sys.stdin.read()
    
    # Eliminamos espacios en blanco al inicio y final pero mantenemos saltos de línea internos
    texto = entrada.strip()

    # Validación: Si el texto está vacío
    if not texto:
        print("\n⚠️ Error: No has ingresado ningún contenido para analizar.")
        return

    # Procesamiento de datos
    total_caracteres_con_espacios = len(texto)
    # Quitamos espacios, tabulaciones y saltos de línea para el conteo "puro"
    total_caracteres_sin_espacios = len("".join(texto.split()))
    total_palabras = len(texto.split())
    total_lineas = texto.count('\n') + 1 if texto else 0

    # Presentación de resultados con formato profesional
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