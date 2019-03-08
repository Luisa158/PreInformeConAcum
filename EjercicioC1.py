
x=int(input("Por favor, ingrese un número: "))
y=int(input("Por favor, ingrese un número: "))

for i in range (10):
    z=x
    x=y
    y=z
    z=o
    print(x,y)
aux=0
for i in range (14):
    print(i)
    if i==7:
        aux=i
print("El número intermedio es: ", aux)
