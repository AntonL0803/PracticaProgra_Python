num1 = int(input("Introducir el numero 1: "))
num2 = int(input("Introducir el numero 2: "))

if num1 > 0 and num2 > 0:
    print("el producto de los dos números es positivo o nulo")
elif num1 < 0 and num2 < 0:
    print("el producto de los dos números es positivo o nulo")
elif num1 > 0 and num2 < 0:
    print("el producto de los dos números es negativo")
elif num1 < 0 and num2 > 0:
    print("el producto de los dos números es negativo")
    
