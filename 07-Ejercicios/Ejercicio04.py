import math


class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def invertir(self):
        return Fraccion(self.denominador, self.numerador)
    
    def simplificar(self):
        divisor = math.gcd(self.numerador, self.denominador)
        nuevo_numerador = self.numerador / divisor
        nuevo_denominador = self.denominador / divisor
        return Fraccion(nuevo_numerador, nuevo_denominador)
        
    def multiplicar(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        nueva_fraccion = Fraccion(nuevo_numerador, nuevo_denominador)
        return nueva_fraccion
    def dividir(self, otra_fraccion):
        return self.multiplicar(otra_fraccion.invertir())
    
if __name__ == "__main__":
    fraccion1 = Fraccion(4, 8)
    fraccion2 = Fraccion(3, 9)
    
    fraccion_invertida = fraccion1.invertir()
    print(f"Fracción 1 invertida: {fraccion_invertida}")
    
    fraccion_simplificada = fraccion2.simplificar()
    print(f"Fracción 2 simplificada: {fraccion_simplificada}")
    
    producto = fraccion1.multiplicar(fraccion2)
    print(f"Producto de fracción 1 y fracción 2: {producto}")
    
    cociente = fraccion1.dividir(fraccion2)
    print(f"Cociente de fracción 1 entre fracción 2: {cociente}")