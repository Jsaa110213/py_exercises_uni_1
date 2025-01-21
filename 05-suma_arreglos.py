""" 
5. Escribir una función que lea dos arreglos de cinco elementos y retorne un tercer arreglo con la suma de los elementos, posición a posición.​

Ejemplo:

arreglo1 = [2, 3, 4, 5, 5]​

arreglo2 = [7, 8, 9, 2, 3]

Entonces para sumar ambos arreglos se debe sumar posición a posición, es importante indicar que ambos arreglos deben tener el mismo tamaño, la salida debe ser:

respuesta = [9, 11, 13, 7, 8]
 """

def suma_arreglos(arreglo1, arreglo2):
    new_array = [ ]

    if len(arreglo1) != len(arreglo2):
        raise ValueError("Ambos arreglos deben tener la misma longitud")

    # Se recorren los arreglos y se suman los elementos de la misma posición
    for i in range(len(arreglo1)):
        item_arr_1 = int(arreglo1[i])
        item_arr_2 = int(arreglo2[i])

        new_item = item_arr_1 + item_arr_2
        new_array.append(new_item)

    return new_array

arreglo_1 = list(
    map(
        int, input("Ingrese los 5 números del 'arreglo-1' separados por espacios: ").split()
    )
)
arreglo_2 = list(
    map(
        int, input("Ingrese los 5 números del 'arreglo-2' separados por espacios: ").split()
    )
)

resultado = suma_arreglos(arreglo_1, arreglo_2)

print("El nuevo arreglo con la suma de los elementos es: ", resultado)
