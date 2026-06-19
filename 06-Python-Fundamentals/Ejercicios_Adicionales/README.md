# Ejercicios Adicionales 📚

Ejercicios avanzados de Python para consolidar conocimientos y desarrollar habilidades.

## 📋 Contenido

Este módulo contiene:

- **Algoritmos**: Búsqueda, ordenamiento, recursión
- **Estructuras Avanzadas**: Árboles, grafos, colas, pilas
- **Casos de Uso Reales**: Web scraping, APIs, data processing
- **Problemas de Lógica**: Desafíos algorítmicos
- **Integración AWS**: Python con servicios AWS

## 🎯 Temas por Dificultad

### Intermedio
- List/dict comprehensions
- Generators y iterators
- Decorators
- Context managers
- Lambda functions

### Avanzado
- Algoritmos de ordenamiento (quicksort, mergesort)
- Búsqueda binaria
- Recursión y memoización
- Estructuras de datos custom
- Testing y debugging

### Aplicados
- Web scraping con BeautifulSoup
- Trabajo con APIs (requests)
- Procesamiento de datos (pandas)
- Automatización con scripts
- Integración con AWS SDK (boto3)

## 💡 Problemas Clásicos

1. **Fibonacci**: Recursión vs iteración vs memoización
2. **Tower of Hanoi**: Recursión compleja
3. **Sorting Algorithms**: Implementación de diferentes ordenamientos
4. **Binary Search**: Búsqueda eficiente
5. **Two Sum Problem**: Optimización de búsqueda
6. **Graph Traversal**: BFS y DFS
7. **Dynamic Programming**: Problemas de optimización

## 🐍 Ejemplos de Ejercicios

### Recursión - Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### List Comprehension
```python
# Generar lista de cuadrados
cuadrados = [x**2 for x in range(10)]

# Filtrar números pares
pares = [x for x in range(10) if x % 2 == 0]
```

### Generator
```python
def contador(max):
    i = 0
    while i < max:
        yield i
        i += 1
```

## 🔗 AWS Integration

### Trabajar con S3
```python
import boto3

s3 = boto3.client('s3')
s3.put_object(Bucket='mi-bucket', Key='archivo.txt', Body=b'contenido')
```

### Trabajar con DynamoDB
```python
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mi-tabla')
table.put_item(Item={'id': '123', 'nombre': 'Juan'})
```

### Lambdas con Python
```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hola desde Lambda!'
    }
```

## 📈 Progresión de Aprendizaje

1. Completar ejercicios básicos (nivel fácil)
2. Entender la solución y optimizaciones
3. Intentar variaciones del problema
4. Aplicar en contexto AWS
5. Crear soluciones propias

## 📚 Recursos

- [LeetCode](https://leetcode.com/) - Problemas algorítmicos
- [HackerRank](https://www.hackerrank.com/) - Desafíos de programación
- [Project Euler](https://projecteuler.net/) - Problemas matemáticos
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
