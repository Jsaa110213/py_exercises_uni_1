### Creación de arrays bidimensionales ###

# Definición de una matriz bidimensional (lista de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

# Acceder al primer y último elemento de la matriz
primer_elemento = matriz[0][0]  # Primer elemento de la primera fila
ultimo_elemento = matriz[-1][-1]  # Último elemento de la última fila
print(primer_elemento, ultimo_elemento)

# Otra matriz de ejemplo
array = [[23, 45, 43, 23, 45], [45, 67, 54, 32, 45], [89, 90, 87, 65, 44], [23, 45, 67, 32, 10]]
print(array)

## Acceder a valores

# Acceder a la primera fila
print(array[0])

# Acceder a la tercera fila
print(array[2])

# Acceder al tercer elemento de la primera fila
print(array[0][2])

# Acceder al cuarto elemento de la tercera fila
print(array[2][3])

# Iterar sobre el array usando ciclo for (recorrer filas y columnas)
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for rows in a:
    for columns in rows:
        print(columns, end=" ")  # Imprimir los elementos en la misma línea
    print()

# Generar una sola línea usando el método join()
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in a:
    print(' '.join([str(elem) for elem in row]))  # Convertir cada elemento a string y unirlos con un espacio

# Crear una nueva matriz con los cuadrados de los elementos
cuadrados = [[x**2 for x in fila] for fila in matriz]
print(cuadrados)

### Modificar elementos de una matriz ###

# Cambiar un elemento específico de la matriz
matriz[0][0] = 10  # Cambiar el primer elemento de la primera fila
print(matriz)

# Modificar una fila completa
array[2] = [0, 3, 5, 6, 7]
print(array)

# Insertar una fila en la matriz en un índice específico
array.insert(2, [1, 2, 3, 4, 5])
array.insert(2, [1, 2, 3, 4, 5])
array.insert(2, [1, 2, 3, 4, 5])
print(array)

# Agregar una fila al final de la matriz con append()
matriz.append([10, 11, 12])  # Añadir fila
print(matriz)

# Agregar una columna, añadiendo elementos a cada fila
for i in range(len(matriz)):
    matriz[i].append(i)  # Añadir un valor en cada fila
print(matriz)

# Eliminar una fila con el comando del
del array[2]  # Eliminar la tercera fila
del array[1]  # Eliminar la segunda fila
print(array)

# Obtener el número de filas de una matriz con len()
print(len(array))  # Devuelve el número de filas

# Eliminar todos los elementos de una matriz
array = [1, 2, 3]
array.clear()
print(array)

# Copiar los elementos de una matriz a otra
array = [1, 2, 3]
array1 = array.copy()  # Crear una copia
print(array1)

# Contar las apariciones de un elemento en una matriz
array = [1, 2, 3]
print(array.count(8))  # Cuenta cuántas veces aparece el número 8

# Extender una matriz con otra
array = [1, 2, 3]
array1 = [4, 5, 6]
array.extend(array1)  # Añadir los elementos de array1 a array
print(array)

# Encontrar el índice de un elemento en una matriz
array = [1, 2, 3]
print(array.index(3))  # Devuelve el índice del primer 3 en la matriz

# Eliminar un elemento por su índice
array = [1, 2, 3]
array.pop(2)  # Elimina el elemento en el índice 2
print(array)

### Uso de NumPy para operaciones avanzadas ###

# NumPy es una biblioteca para operaciones matemáticas avanzadas
# import numpy as np

# Crear una matriz con NumPy
# matriz_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Calcular la inversa de la matriz
# inversa = np.linalg.inv(matriz_np)  # Inversa de la matriz
# print(inversa)

# # Más sobre NumPy en: https://www.freecodecamp.org/espanol/news/curso-intensivo-de-python-numpy-como-construir-arreglos-n-dimensionales-para-aprendizaje-automatico/
