puntoX = int(input("Introducir la coordenada X: "))
puntoY = int(input("Introducir la coordenada Y: "))

if puntoX > 0 and puntoY > 0:
    print("Situado en el primer cuadrante")
elif puntoX < 0 and puntoY > 0:
    print("Situado en el segundo cuadrante")
elif puntoX < 0 and puntoY < 0:
    print("Situado en el tercer cuadrante")
elif puntoX > 0 and puntoY < 0:
    print("Situado en el cuarto cuadrante")
elif puntoX != 0 and puntoY == 0:
    print("Situado en el eje de abcisas")
elif puntoX == 0 and puntoY != 0:
    print("Situado en el eje de coordenadas")
elif puntoX == 0 and puntoY == 0:
    print("Situado en el origen de coordenadas")