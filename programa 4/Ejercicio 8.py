diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

#8.Escribe un código que liste todos los estudiantes que tienen una nota en 'Probabilidad' mayor a 3.0.

nombres= []

for k, i in diccionario.items():
    if i.get("Probabilidad", 0) > 3.0:
        nombres.append(k)

print("Los estudiantes con nota en", "Probabilidad", "mayor a 3.0:")
for estudiante in nombres:
    print(estudiante)
