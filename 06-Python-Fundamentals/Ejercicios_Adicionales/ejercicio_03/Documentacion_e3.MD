# Ejercicio 3: Dibujo de Rombo Centrado (Solo Figura)

## Descripción
Este programa genera un rombo de asteriscos (`*`) basado en un tamaño proporcionado por el usuario. La lógica del script permite que los mensajes informativos se mantengan alineados a la izquierda, mientras que **la figura geométrica se posiciona automáticamente en el centro horizontal de la terminal**, detectando dinámicamente el ancho de la ventana del usuario.

## Conceptos de Python utilizados
- **`shutil.get_terminal_size()`**: Detecta las dimensiones de la consola (columnas y filas) en tiempo real.
- **Método `.center(columnas)`**: Calcula y añade automáticamente el número exacto de espacios a la izquierda y derecha de una cadena de texto para centrarla en un ancho dado.
- **Bucle de Simetría**: 
    - Un bucle ascendente para la mitad superior (de 1 a N).
    - Un bucle descendente para la mitad inferior (de N-1 a 1).
- **Aritmética de Impares**: Se usa `(2 * i - 1)` para garantizar que cada fila tenga un número impar de asteriscos, permitiendo una punta simétrica.

## Código del Script (`ejercicio_03.py`)
```python
import shutil

def dibujar_rombo_centrado_figura():
    """
    Dibuja un rombo centrado en la terminal, manteniendo los textos a la izquierda.
    """
    # Obtener el ancho de la terminal para centrar la figura
    columnas = shutil.get_terminal_size(fallback=(80, 20)).columns

    print("--- Generador de Rombos Centrados ---")
    
    while True:
        entrada = input("Introduce el tamaño (número de filas de la mitad superior): ").strip()
        if entrada.isdigit() and int(entrada) > 0:
            n = int(entrada)
            break
        else:
            print("⚠️ Error: Por favor, introduce un número entero positivo.")

    print(f"\nGenerando rombo de tamaño {n}...\n")

    # Dibujo del rombo (Centrado dinámico)
    for i in range(1, n + 1):
        asteriscos = "*" * (2 * i - 1)
        print(asteriscos.center(columnas))

    for i in range(n - 1, 0, -1):
        asteriscos = "*" * (2 * i - 1)
        print(asteriscos.center(columnas))

    print("\n--- Fin del dibujo ---")

if __name__ == "__main__":
    dibujar_rombo_centrado_figura()
```

## Output (Representación en Consola)
> *Nota: El centrado visual dependerá del ancho de tu terminal.*

```text
PS D:\Documentos\Projects_GitHub\Python\ejercicio_03> python .\ejercicio_03.py
--- Generador de Rombos Centrados ---
Introduce el tamaño (número de filas de la mitad superior): 13

Generando rombo de tamaño 13...

                                     *
                                    ***
                                   *****
                                  *******
                                 *********
                                ***********
                               *************
                              ***************
                             *****************
                            *******************
                           *********************
                          ***********************
                         *************************
                          ***********************
                           *********************
                            *******************
                             *****************
                              ***************
                               *************
                                ***********
                                 *********
                                  *******
                                   *****
                                    ***
                                     *

--- Fin del dibujo --