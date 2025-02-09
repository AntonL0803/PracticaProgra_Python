def suma_digitos(n):
    if n < 10: 
        return n
    else:  
        return n % 10 + suma_digitos(n // 10)

print(suma_digitos(12345)) 


def contar_digitos(n):
    if n < 10:
        return 1
    else:  
        return 1 + contar_digitos(n // 10)

print(contar_digitos(12345))  


def invertir_digitos(n):
    if n < 10: 
        return str(n)
    else:  
        return str(n % 10) + invertir_digitos(n // 10)

print(invertir_digitos(12345))  
