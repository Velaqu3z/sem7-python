suma=0
lim=int(input("ingrese valor limite: "))
for i in range(lim):
    number=int(input("ingrese el numero: "))
    suma += number
    promedio=suma/lim
print("la suma es " , suma)
print("el promedio es " , promedio)