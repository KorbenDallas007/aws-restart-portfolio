# Laboratorios Base 🚀

Laboratorios fundamentales para aprender Python desde cero.

## 📋 Contenido

Este módulo cubre:

- **Sintaxis Básica**: Variables, tipos, operadores
- **Control de Flujo**: if/else, loops
- **Funciones**: Definición, parámetros, retorno
- **Strings**: Manipulación y formateo
- **Listas y Tuples**: Secuencias
- **Diccionarios**: Pares clave-valor
- **Manejo de Excepciones**: try/except
- **Archivos**: Lectura y escritura

## 🎯 Estructura

### Laboratorio 1: Introducción a Python
- Instalar Python y configurar entorno
- Primer programa: "Hola Mundo"
- REPL interactivo

### Laboratorio 2: Variables y Tipos
```python
nombre = "Juan"        # String
edad = 30              # Integer
altura = 1.75          # Float
es_adulto = True       # Boolean

print(f"{nombre} tiene {edad} años")
```

### Laboratorio 3: Operadores
```python
# Aritméticos
a + b, a - b, a * b, a / b, a ** b

# Comparación
a == b, a != b, a > b, a < b

# Lógicos
a and b, a or b, not a
```

### Laboratorio 4: Control de Flujo
```python
if edad >= 18:
    print("Es adulto")
elif edad >= 13:
    print("Es adolescente")
else:
    print("Es menor")

for i in range(10):
    print(i)

while condicion:
    # código
```

### Laboratorio 5: Funciones
```python
def saludar(nombre, apellido="Desconocido"):
    """Saluda a una persona"""
    return f"Hola {nombre} {apellido}"

# Llamar función
resultado = saludar("Juan", "García")
```

### Laboratorio 6: Strings
```python
# Métodos útiles
texto.upper()
texto.lower()
texto.strip()
texto.split(",")
",".join(lista)

# Formateo
f"Hola {nombre}"
"Hola {}".format(nombre)
"Hola %s" % nombre
```

### Laboratorio 7: Listas
```python
lista = [1, 2, 3, 4, 5]

# Métodos
lista.append(6)
lista.insert(0, 0)
lista.remove(3)
lista.pop()

# Iteración
for elemento in lista:
    print(elemento)

# Slicing
primeros_tres = lista[:3]
```

### Laboratorio 8: Diccionarios
```python
usuario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso
print(usuario["nombre"])
print(usuario.get("email", "No especificado"))

# Iteración
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
```

### Laboratorio 9: Manejo de Excepciones
```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes ingresar un número válido")
except ZeroDivisionError:
    print("No puedes dividir entre cero")
finally:
    print("Operación completada")
```

### Laboratorio 10: Archivos
```python
# Lectura
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

# Escritura
with open("archivo.txt", "w") as archivo:
    archivo.write("Nuevo contenido")

# Append
with open("archivo.txt", "a") as archivo:
    archivo.write("Más contenido\n")
```

## 💡 Mejores Prácticas

✅ Usar nombres descriptivos  
✅ Agregar comentarios  
✅ Documentar funciones  
✅ Manejar excepciones  
✅ Seguir PEP 8  
✅ Testear código  

## 🛠️ Herramientas Necesarias

```bash
# Instalar Python 3
python --version

# Entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# IDE recomendado
pip install jupyter
jupyter notebook
```

## 📚 Recursos

- [Python Tutorial Oficial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
