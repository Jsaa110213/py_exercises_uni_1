# 4 - Escribir una función donde se declare un arreglo que va a almacenar las potencias de 2 desde un valor mínimo a un valor máximo, ambos pedidos por teclado. Si por ejemplo, el valor mínimo es 3 y máximo es 5 entonces el arreglo debe contener:​

""" 2**3 = 8 en la posición 0 2**4 = 16 en la posición 1 2**5 = 32 en la posición 2. Para este ejemplo el arreglo debe ser de tamaño n.​ """

def potencia_dos(minimo, maximo):
    arreglo = [ ]
    for i in range(minimo, maximo + 1):
        arreglo.append(2 ** i)
    return arreglo

print("____________ Potencia de 2 ____________")
minimo = int(input("Ingrese el valor mínimo del arreglo: "))
maximo = int(input("Ingrese el valor máximo del arreglo: "))

if minimo > maximo:
    print("No son validos los digitos, ingrese correctamente los valores minimo y maximo del arreglo.")
else:
    print("Los números con potencia 2 dentro del arreglo son: ", str(potencia_dos(minimo, maximo)))