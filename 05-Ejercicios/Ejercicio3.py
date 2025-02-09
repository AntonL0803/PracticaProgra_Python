import random


tamaño = int(input("Indica un tamaño de la lista: "))
array = [0] * tamaño
num1 = int(input("Introduzca un valor: "))
num2 = int(input("Introduzca un segundo valor:"))

for i in range(0, len(array)):
    array[i] = random.randint(num1, num2)
print(array)