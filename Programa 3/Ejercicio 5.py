#5.Escriba un programa para hacer un patrón como un triángulo rectángulo con un número que repetirá un número seguido.

x = int(input("número para el triángulo: "))


for i in range(1, x + 1):    
    print(str(i) * i)

    