#Escriba una función para multiplicar una matriz por un escalar.

def multiplicar_escalar(matriz, escalar):
        
        res_matriz=[]
    
        for i in matriz:
            nrows = []
            for elemento in i:
                nrows.append(elemento * escalar)
            res_matriz.append(nrows)
        r=Matriz("[]")
        r.matriz=res_matriz
        return r