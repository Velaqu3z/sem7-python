pares=0
impares=0
for i in range(6):
    number=int(input("ingrese un numero: "))
    if number % 2 == 0:
        pares += 1
    else:
        impares +=1
print("números pares: " , pares )
print("los números impares son: " , impares)            


