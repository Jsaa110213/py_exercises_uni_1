# 2 - Escribir una función que retorne el valor más grande que esté contenido dentro de un arreglo de números.​

def valor_mas_grande(arreglo):
    maximo = 0
    for num in arreglo[1:]:
        if num > maximo:
            maximo = num
    return maximo

resultado = list(
    map(
        int, input("Ingrese los numeros del vector, separados por espacio: ").split()
    )
)

print("Numero mas grande dentro del vector: " + str(valor_mas_grande(resultado)))