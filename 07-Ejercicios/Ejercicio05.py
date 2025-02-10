class Vehiculo:
    vehiculosCreados = 0
    kilometrosTotales = 0
    def __init__(self):
        Vehiculo.vehiculosCreados += 1
    def aumentarKilometraje(self, kilometrosRecorridos):
        Vehiculo.kilometrosTotales += kilometrosRecorridos

class Coche(Vehiculo):
    kilometrosTotalesCoche = 0
    
    def __init__(self):
        super().__init__()
        
    def aumentarKilometrajeCoche(self, kilometrosRecorridos):
        Coche.kilometrosTotalesCoche += kilometrosRecorridos
        super().aumentarKilometraje(kilometrosRecorridos)
    def verKilometrajeCoche(self):
        print(f"Los kilometros totales de los coches es de {Coche.kilometrosTotalesCoche}")

class Bicicleta(Vehiculo):
    kilometrosTotalesBici = 0
    
    def __init__(self):
        super().__init__()
    
    def aumentarKilometrajeBici(self, kilometrosRecorridos):
        Bicicleta.kilometrosTotalesBici += kilometrosRecorridos
        super().aumentarKilometraje(kilometrosRecorridos)
    
    def verKilometrajeBici(self):
        print(f"Los kilometros totales de las Bicicletas es de {Bicicleta.kilometrosTotalesBici}")


coche = Coche()
bici = Bicicleta()


while True:
    print("\nVEHÍCULOS")
    print("---------")
    print("1. Aumentar Kilometraje Coche")
    print("2. Aumentar Kilometraje Bicicleta")
    print("3. Ver Kilometraje del Coche")
    print("4. Ver Kilometraje de la Bicicleta")
    print("5. Ver Kilometraje Total de Vehículos")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        km = int(input("Introduce los kilómetros recorridos por el coche: "))
        coche.aumentarKilometrajeCoche(km)
        print("Kilometraje del coche actualizado.")

    elif opcion == "2":
        km = int(input("Introduce los kilómetros recorridos por la bicicleta: "))
        bici.aumentarKilometrajeBici(km)
        print("Kilometraje de la bicicleta actualizado.")

    elif opcion == "3":
        coche.verKilometrajeCoche()

    elif opcion == "4":
        bici.verKilometrajeBici()

    elif opcion == "5":
        print(f"Kilómetros totales de todos los vehículos: {Vehiculo.kilometrosTotales}")

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
