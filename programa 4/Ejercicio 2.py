diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

#2.Escribe un bucle `for` en Python para iterar a través de todos los nombres en el diccionario y imprimir solo aquellos que tienen una clave 'Programación' en su diccionario anidado.

for k,i in diccionario.items():
    if "Programacion" in i :
        print(k)




