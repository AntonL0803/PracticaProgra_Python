def producto(a, b):
    if b == 0: 
        return 0
    elif b % 2 == 0: 
        return producto(a * 2, b // 2)
    else: 
        return producto(a * 2, b // 2) + a

a = 3
b = 5
print(f"El producto de {a} y {b} es: ")
print(producto(a, b))