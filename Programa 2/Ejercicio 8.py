#8.Escriba un programa para ingresar cualquier caracter y verifique si es vocal o consonante.

letra=input("Diga una letra: ")
vocales= ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

if letra in vocales:
    print("es vocal")
else:
    print("es consonante")
