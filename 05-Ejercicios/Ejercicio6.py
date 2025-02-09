class ArrayOperaciones:
    def __init__(self, array):
        self.array = array

    def multiplicar_por_2(self, izq, der):
        for i in range(izq, der + 1):
            self.array[i] *= 2

    def invertir_rango(self, izq, der):
        self.array[izq:der + 1] = self.array[izq:der + 1][::-1]

    def contar_impares_posiciones_pares(self):
        return sum(1 for i in range(0, len(self.array), 2) if self.array[i] % 2 != 0)

    def contar_menores_que(self, x, n):
        return sum(1 for i in self.array[:n + 1] if i < x)

    def esta_ordenado(self):
        return all(self.array[i] <= self.array[i + 1] for i in range(len(self.array) - 1))

    def primera_subsecuencia_consecutiva(self):
        for i in range(len(self.array) - 2):
            if self.array[i] + 1 == self.array[i + 1] == self.array[i + 2] - 1:
                return i
        return -1

    def suma_mayor_que(self, x):
        suma = 0
        for num in self.array:
            suma += num
            if suma > x:
                return True
        return False

    def primera_subsecuencia_mayores(self, x, n):
        for i in range(len(self.array) - n + 1):
            if all(num > x for num in self.array[i:i + n]):
                return i
        return -1

    def posicion_ultimo_impar(self):
        for i in range(len(self.array) - 1, -1, -1):
            if self.array[i] % 2 != 0:
                return i
        return -1

    def suma_despues_del_primer_impar(self):
        for i in range(len(self.array)):
            if self.array[i] % 2 != 0:
                return sum(self.array[i + 1:])
        return 0
        
def main():
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operaciones = ArrayOperaciones(v)
    ultimo_indice = len(v) - 1


    while True:
        print("\nMenú:")
        print("a) Multiplicar por 2 los valores entre las posiciones dadas")
        print("b) Invertir los valores entre las posiciones dadas")
        print("c) Contar los impares en posiciones pares")
        print("d) Contar los menores que x hasta la posición n")
        print("e) Verificar si el array está ordenado ascendentemente")
        print("f) Buscar la primera subsecuencia consecutiva")
        print("g) Verificar si la suma de los elementos es mayor que x")
        print("h) Buscar subsecuencia de n enteros mayores que x")
        print("i) Obtener la última posición impar")
        print("j) Sumar los elementos tras el primer impar")
        print("0) Salir")

        opcion = input("Seleccione una opción (a-j o 0 para salir): ")

        if opcion == 'a':
            izq = int(input("Introduzca la posición izquierda: "))
            der = int(input("Introduzca la posición derecha: "))
            if izq >= 0 and der <= ultimo_indice:
                operaciones.multiplicar_por_2(izq, der)
        elif opcion == 'b':
            izq = int(input("Introduzca la posición izquierda: "))
            der = int(input("Introduzca la posición derecha: "))
            operaciones.invertir_rango(izq, der)
        elif opcion == 'c':
            operaciones.contar_impares_posiciones_pares()
        elif opcion == 'd':
            x = int(input("Introduzca el valor de x: "))
            n = int(input("Introduzca la posición n: "))
            operaciones.contar_menores_que(x, n)
        elif opcion == 'e':
            operaciones.esta_ordenado()
        elif opcion == 'f':
            operaciones.primera_subsecuencia_consecutiva()
        elif opcion == 'g':
            x = int(input("Introduzca el valor de x: "))
            operaciones.suma_mayor_que(x)
        elif opcion == 'h':
            x = int(input("Introduzca el valor de x: "))
            n = int(input("Introduzca la longitud de la subsecuencia n: "))
            operaciones.primera_subsecuencia_mayores(x, n)
        elif opcion == 'i':
            operaciones.posicion_ultimo_impar()
        elif opcion == 'j':
            operaciones.suma_despues_del_primer_impar()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()