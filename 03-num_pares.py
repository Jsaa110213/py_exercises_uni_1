"""
3 - Escriba una función donde se declare un arreglo 
    de tipo int de tamaño n e inicialícelo con valores 
    pares 0, 2, 4, etc. Use un ciclo.​
 """

def arr_num_pares(rango):
    new_arr = []
    for i in range(0,rango):
        new_arr.append(i * 2)
    return new_arr

result = int(input("Ingresa el numero de elementos que quieres imprimir: "))

print("Los numeros pares dentro del arreglo son: ", arr_num_pares(result))