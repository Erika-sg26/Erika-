diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

#4.Si intentas acceder a una clave que no existe en el diccionario, como `diccionario['Alondra']['Estadística']`, ¿Qué ocurre y cómo puedes manejarlo?
 
#diccionario["Alondra"]["Estadística"]

#como no existe "Estadística" en el diccionario y sale un error, vamos a usar get() para evitar el error

clave = diccionario.get("Alondra", {}).get("Estadística", "Clave no encontrada")

print(clave)

