import random

def es_primo(numero):
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


tamaño = int(input("Indica un tamaño de la lista: "))
num1 = int(input("Introduzca un valor: "))
num2 = int(input("Introduzca un segundo valor:"))
array = [] 

while len(array) < tamaño:
    numero = random.randint(num1, num2)
    if es_primo(numero):
        array.append(numero)
print(array)
numeroMayor = max(array)
print("El mayor numero es ", numeroMayor)