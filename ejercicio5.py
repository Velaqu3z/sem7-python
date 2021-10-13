a=0
b=1
n=int(input("ingrese limite: "))
suma=0
for i in range(n):
    c=a+b
    a=b
    b=c
    print(b, end=", ")
    suma += b
print("la suma es " , suma)   