#11.Escriba un programa para que dado el número del mes, indique el número de días del mes

mes=int(input("Diga el numero del mes: "))
dias = 0

if mes == 1:  
    dias = 31
elif mes == 2: 
    dias = 28  
elif mes == 3: 
    dias = 31
elif mes == 4: 
    dias = 30
elif mes == 5:  
    dias = 31
elif mes == 6:  
    dias = 30
elif mes == 7:  
    dias = 31
elif mes == 8:  
    dias = 31
elif mes == 9:  
    dias = 30
elif mes == 10:
    dias = 31
elif mes == 11:  
    dias = 30
elif mes == 12:  
    dias = 31
else:
    print("No hay mes")

if 1 <= mes <= 12:
    print("El mes", mes, "tiene", dias, "días.")
