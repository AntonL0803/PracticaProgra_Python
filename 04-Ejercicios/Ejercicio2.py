#Primer condicional
x = 0
if x>= 0:
    x+=1
elif x>=1:
    x+=2
    
print(x)

#Segundo condicional
x = 0
if x>=0:
    x+=1
if x>=1:
    x+=2
    
print(x)

#Tercer condicional
x= 0
if x < 0:
    x+=1
else:
    x+=1
    x-=1
    
print(x)

#Cuarto condicional
x = 0
if x > 0:
    if x <=1:
        x+=1
    else:
        x-=1
print(x)