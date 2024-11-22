#10.Dados dos vectores calcular el producto punto

vector1=[5,7,1]
vector2=[3,0,9]

producto=0

x=len(vector1)
y=len(vector2)

if x==y:
    for i in range(x):
        producto+= vector1[i] * vector2[i]
else:
    print("vectores igaules")
    
print("El producto punto es: ", producto)