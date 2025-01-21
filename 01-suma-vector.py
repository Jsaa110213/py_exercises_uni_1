# Ejercicio 1 - Escriba una función que sume todos los elementos de un arreglo de tipo int.
def suma_elementos(arreglo):
    suma = 0
    for num in arreglo:
        suma += num
    return suma

# Solicitar entrada del usuario y convertirla a una lista de enteros
resultado = list(
    map(
        int, input("Ingrese los números del vector, separados por espacios: ").split()
    )
)

print("La suma de los elementos del vector es: " + str(suma_elementos(resultado)))