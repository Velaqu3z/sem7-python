pares=0
impares=0
suma=0
n=int(input("ingrese limite: "))
for i in range( n):
    numero=int(input("ingrese valor: "))
    if numero % 2 == 0:
        pares += numero
        
    else:
        impares += numero
    
print("la suma de pares es: " , pares) 
print("la suma de impares es: " , impares)       