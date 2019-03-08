
x=int(input("Por favor, ingrese un número: "))
y=int(input("Por favor, ingrese un número: "))
z=int(input("Por favor, ingrese un número"))
for i in range (14):
    o=x
    x=y
    y=z
    z=x
    print(x,y,z)
aux=0
for i in range (14):
    print(i)
    if i==7:
        aux=i
print("El número intermedio es: ", aux)
