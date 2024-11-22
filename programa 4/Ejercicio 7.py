diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

#7.Crea una función en Python que calcule y devuelva el promedio de todas las notas de un estudiante dado, tomando como argumento el nombre del estudiante.

nombre=input("Nombre del estudiante: ")

if nombre in diccionario:
    notas = diccionario[nombre].values()
    promedio = sum(notas) / len(notas) if notas else 0
    print("El promedio de", nombre, "es: ", promedio)
else:
    print("El estudiante", nombre, "no se encontró en el diccionario")
