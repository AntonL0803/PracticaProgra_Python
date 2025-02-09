def natural(n):
    if n > 0:
        natural(n-1)
        print(n)
        
natural(10)

def natural2(n):
    if n < 0:
        print(n)
        natural2(n-1)
        
natural2(10)

