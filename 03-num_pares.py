# Ejercicio 3 - Escriba una función donde se declare un arreglo de tipo int de tamaño "n" e inicialícelo con valores pares 0, 2, 4, etc. Use un ciclo.​
def numeros_pares(n):
    
    arreglo = [ ]
    for i in range(0, n * 2, 2):  
        arreglo.append(i)
    return arreglo

tamaño = int(input("Ingrese el tamaño del arreglo: "))
print("Los números pares dentro del arreglo son:", numeros_pares(tamaño))
