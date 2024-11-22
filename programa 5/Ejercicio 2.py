#2.Dada una lista de números retornar el número menor y su posición en la lista

lista=[87,25,46,63,73]

menor = lista[0]
posicion = 0

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        posicion = i
print("El numero menor es", menor, "en la posicion", posicion )
