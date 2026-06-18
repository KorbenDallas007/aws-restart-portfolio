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