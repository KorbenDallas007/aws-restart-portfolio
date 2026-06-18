import shutil

def dibujar_rombo_centrado_figura():
    """
    Dibuja un rombo centrado en la terminal, manteniendo los textos a la izquierda.
    """
    # Obtener el ancho de la terminal para centrar la figura
    columnas = shutil.get_terminal_size(fallback=(80, 20)).columns

    # Texto alineado a la izquierda (normal)
    print("--- Generador de Rombos Centrados ---")
    
    while True:
        entrada = input("Introduce el tamaño (número de filas de la mitad superior): ").strip()
        if entrada.isdigit() and int(entrada) > 0:
            n = int(entrada)
            break
        else:
            print("⚠️ Error: Por favor, introduce un número entero positivo.")

    print(f"\nGenerando rombo de tamaño {n}...\n")

    # Dibujo del rombo (Solo estas líneas se centran en la pantalla)
    # Parte superior
    for i in range(1, n + 1):
        asteriscos = "*" * (2 * i - 1)
        print(asteriscos.center(columnas))

    # Parte inferior
    for i in range(n - 1, 0, -1):
        asteriscos = "*" * (2 * i - 1)
        print(asteriscos.center(columnas))

    # Texto final alineado a la izquierda
    print("\n--- Fin del dibujo ---")

if __name__ == "__main__":
    dibujar_rombo_centrado_figura()