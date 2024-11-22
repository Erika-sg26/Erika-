#6.Dada una lista de números hallar la varianza

lista=[19,26,42,38,54]

suma = 0
n = 0

for i in lista:
    suma += i
    n += 1
    
media = 0
if n > 0:
    media = suma / n

diferencias = 0

for i in lista:
    diferencias += (i - media) * (i - media)

varianza = 0

if n > 0:
    varianza = diferencias / n
print("La varianza de la lista es: ", varianza)



