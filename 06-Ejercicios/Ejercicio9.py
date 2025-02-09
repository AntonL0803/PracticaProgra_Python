def convertidorBinario(n):
    if n == 1:
        return str(n)
    else:
        return str(n%2) + convertidorBinario(n // 2)
    
print(convertidorBinario(35))