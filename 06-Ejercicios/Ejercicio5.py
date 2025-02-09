def condicional(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a*(b-1)+ a

print(condicional(6, 9))