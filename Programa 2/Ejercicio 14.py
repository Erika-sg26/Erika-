#14.Escriba un programa para verificar si el triángulo es equilatero, isósceles o escaleno.

x=float(input("Lado x: "))
y=float(input("Lado y: "))
z=float(input("Lado z: "))

if x > 0 and y > 0 and z > 0:
    if x==y==z:
        print("Es un triangulo equilatero")
    if (x==y and x != z) or (y==z and y != x ) or (x==z and x != y):
        print("Es un triangulo isosceles")
    else:
        print("Es un triangulo escaleno")
else:
    print("No es ningun triangulo")
    