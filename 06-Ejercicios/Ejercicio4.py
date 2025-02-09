def dividir(a, b):
    contador = 0
    if a < b:
        return 0
    elif a >= b:
        return (a-b)//b+1

print(dividir(12, 3))
