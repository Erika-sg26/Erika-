#7. Calcular la distancia D entre dos puntos (x1, y1) y (x2, y2) en el planocartesiano. FÃ³rmula: D =p(x2 âˆ’ x1)2 + (y2 âˆ’ y1)2.
#Input= puntos (x1, y1) y (x2, y2)
#Output= Distancia

x1=float(input( "Escriba la cordenada x1: "))
x2=float(input( "Escriba la cordenada x2: "))
y1=float(input( "Escriba la cordenada y1: "))
y2=float(input( "Escriba la cordenada y2: "))

distancia= ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(" la distancia entre los puntos (x1,y1) y (x2,y2) en el planocarteciano es: ", distancia)