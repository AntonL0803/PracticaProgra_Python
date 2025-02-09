numero = int(input("Escribe un numero positivo "))
for i in range(1, numero + 1):
    for j in range(i, numero + 1):
        resultado = i + j + 2 * i * j
        print(resultado)