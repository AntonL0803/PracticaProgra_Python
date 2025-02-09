import random

def crear_matriz(rango_min, rango_max):
    return [[random.randint(rango_min, rango_max) for _ in range(10)] for _ in range(10)]

def numero_en_matriz(matriz, numero):
    for fila in matriz:
        if numero in fila:
            return True
    return False

def contar_numero_en_matriz(matriz, numero):
    return sum(fila.count(numero) for fila in matriz)

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
        
def es_cuadrado_magico(matriz):
  
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False  
    
    
    suma_objetivo = sum(matriz[0])

    
    for fila in matriz:
        if sum(fila) != suma_objetivo:
            return False

   
    for col in range(n):
        suma_columna = sum(matriz[fila][col] for fila in range(n))
        if suma_columna != suma_objetivo:
            return False

    suma_diagonal_principal = sum(matriz[i][i] for i in range(n))
    if suma_diagonal_principal != suma_objetivo:
        return False

    suma_diagonal_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
    if suma_diagonal_secundaria != suma_objetivo:
        return False

    return True

def main():
    print("Bienvenido al programa de búsqueda en matrices.")
    rango_min = int(input("Introduce el valor mínimo del rango: "))
    rango_max = int(input("Introduce el valor máximo del rango: "))

    if rango_min > rango_max:
        print("El rango mínimo no puede ser mayor que el máximo. Intenta de nuevo.")
        return

    matriz = crear_matriz(rango_min, rango_max)
    print("\nMatriz generada:")
    imprimir_matriz(matriz)

    while True:
        numero = int(input("\nIntroduce un número para buscar en la matriz (o -1 para salir): "))
        if numero == -1:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if numero < rango_min or numero > rango_max:
            print(f"El número {numero} está fuera del rango [{rango_min}, {rango_max}]. Intenta de nuevo.")
        else:
            if numero_en_matriz(matriz, numero):
                repeticiones = contar_numero_en_matriz(matriz, numero)
                print(f"El número {numero} está en la matriz y aparece {repeticiones} veces.")
            else:
                print(f"El número {numero} no está en la matriz.")
    
    if es_cuadrado_magico(matriz):
        print("Es un cuadrado mágico")
    else:
        print("La matriz no es un cuadrdo mágico")

if __name__ == "__main__":
    main()
