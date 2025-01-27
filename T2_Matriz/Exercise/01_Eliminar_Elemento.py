# Ejercicio 1 - Eliminar un elemento de una matriz (sin usar del, remove, pop)

# Crear matriz de ejemplo o ingresarla manualmente
def crear_matriz():
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    matriz = []
    print("\nIngrese los elementos de la matriz fila por fila:")
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los {columnas} números de la fila {i+1}, separados por espacios: ").split()))
        matriz.append(fila)
    return matriz

# Función para eliminar un elemento de la matriz
def eliminar_elemento(matriz, del_element):
    nueva_matriz = []
    
    for fila in matriz:
        nueva_fila = [elemento for elemento in fila if elemento != del_element]
        nueva_matriz.append(nueva_fila)
    
    return nueva_matriz

# Crear matriz y mostrarla
matriz = crear_matriz()
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario el número que desea eliminar
del_element = int(input("\nIngrese el número que desea eliminar: "))

# Eliminar elemento y mostrar resultado
matriz_resultado = eliminar_elemento(matriz, del_element)
print("\nMatriz después de eliminar el elemento:")
for fila in matriz_resultado:
    print(fila)
