#9.Escriba un programa que imprima los números primos hasta cierto número

num=int(input("Diga un nunero: "))

print("Número primo", num )

for i in range(2, num + 1):
    primo = True 
    for k in range(2, int(i**0.5) + 1):
        if i % k == 0:
            primo = False  
            break  
    if primo:
        print(i)
        
