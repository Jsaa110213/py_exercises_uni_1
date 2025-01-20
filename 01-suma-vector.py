# 1 - Escriba una función que sume todos los elementos de un arreglo de tipo int. ​

def suma_componentes(vector):
    # Caso base: vector vacío
    if vector == []:
        return 0    
    # Caso recursivo: sumar primer elemento y llamar recursivamente
    return vector[0] + suma_componentes(vector[1:])

# Solicitar entrada del usuario y convertir a lista de enteros
input = list(
    map(
        int, input("Ingrese los números del vector separados por espacios: ").split()
    )
) 

# Llamar la función y mostrar el resultado
print("La suma de los componentes del vector es: ", suma_componentes(input))

