def menu():
    print(" Aplicación Fechas ")
    print("--------------------------")
    print("1.- Obtener fecha actual")
    print("2.- Obtener hora actual")
    print("3.- Sumar días")
    print("4.- Restar días")
    print("5.- Fecha anterior o posterior")
    print("0.- Salir")
    print("Seleccione [0..5]: ")
    
def main():
    menu()
    opcion = int(input("Elige una opcion: "))
    if opcion == 0:
        print("Saliendo del programa...")
    elif opcion == 1:
        print("Opcion 1")
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        print("Opcion 5")

if __name__ == "__main__":
    main()