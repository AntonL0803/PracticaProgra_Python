def potencia(a, b):
    if b == 0:  
        return 1
    elif b == 1:  
        return a
    elif b > 1 and b % 2 == 0:  
        mitad = potencia(a, b // 2)
        return mitad * mitad
    elif b > 1 and b % 2 != 0:  
        mitad = potencia(a, b // 2)
        return mitad * mitad * a


print(potencia(12, 4))  
