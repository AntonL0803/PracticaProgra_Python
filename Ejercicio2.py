a = input("Introduce un numero")
b = input("Introduce un segundo numero")

print("numero 1 = " + a + ", numero2 = " + b)
c = b 
b = a
a = c

print("numero 1 = " + a + ", numero2 = " + b)

a, b = b, a