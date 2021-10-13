pares=0
impares=0
neu=0
pos=0
neg=0
for i in range(6):
    number=int(input("ingrese un numero: "))
    if number % 2 == 0:
        pares += 1
    else:
        impares +=1
    if i>0:
         pos =pos+1
    else:
          neg += 1
    if i==0:
        neu += 1
print("números pares: " , pares )
print("los números impares son: " , impares)            
print("los numeros positivos son " , pos)
print("numeros neutros: ", neu)
print("numeros negativos son: " , neg)