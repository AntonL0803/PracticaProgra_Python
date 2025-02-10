class Pizza:
    pizzasPedidasTotales = 0
    pizzasServidas = 0
    entregadas = []
    def __init__(self, tipo, size, id):
        self.tipo = tipo
        self.size = size
        self.id = id
        Pizza.pizzasPedidasTotales += 1
    
    def servir(self, id):
        for numero in Pizza.entregadas:
            if numero == self.id:
                print("La pizza ya ha sido entregada")
                return
        Pizza.entregadas.append(id)
        Pizza.pizzasServidas += 1
        print("La pizza ha sido entregada")
        
    def __str__(self):
        return f"tipo: {self.tipo}, size: {self.size}"

p1 = Pizza("Margarita", "mediana", 1)
p2 = Pizza("Funghi", "familiar", 2)
p2.servir(p2.id)
p3 = Pizza("Cuatro quesos", "mediana", 3)
print(p1)
print(p2)
print(p3)
p2.servir(p2.id)
print(f"pedidas: {Pizza.pizzasPedidasTotales}")
print(f"servidas: {Pizza.pizzasServidas}")

            

    
        