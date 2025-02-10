import random
monedas = {1: "1 centimo", 2: "2 centimos", 3: "5 centimos", 4: "10 centimos", 5: "20 centimos:", 6: "50 centimos:", 7: "1 euro:", 8: "2 euros:"}
opciones = {1: "cara", 2: "cruz"}

for i in range (1,6):
    monedaRandom = random.randint(1, 8)
    caraRandom = random.randint(1, 2)
    
    moneda = monedas[monedaRandom]
    cara = opciones[caraRandom]
    if i == 1:
        print("Moneda: ", moneda, "-", cara)
        casoAntiguo = moneda
        probabilidadAntigua = cara
    else:
        if moneda == casoAntiguo:
            print("Moneda: ", moneda, "-", cara)
            casoAntiguo = moneda
            probabilidadAntigua = cara
        else:
            print("Moneda: ", moneda, "-",probabilidadAntigua )
            casoAntiguo = moneda
            probabilidadAntigua = cara