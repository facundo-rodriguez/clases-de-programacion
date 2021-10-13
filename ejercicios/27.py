#Leer dos vectores A y B de 10 posiciones. 
#Generar un tercer vector C, tambien de 10 posiciones donde el componente C[i] es igual al menor valor entre A[i] y B[i]. 
#Mostrar los tres vectores.

a=[]

b=[]

c=[]

contador=1

print("ingrese 10 valores en los vectores A y B")

while contador<=10:

    print("valor ",contador)

    num1=float(input("ingrese un numero para el vector A: "))
    num2=float(input("ingrese un numero para el vector B: "))

    a.append(num1)
    b.append(num2)

    contador+=1


for i in range(len(a)):

    if( a[i] > b[i] ):
        
        c.append(b[i])

    elif( a[i]==b[i] ):
        
        c.append(b[i])

    else:
        c.append( a[i] )



print("el vector A: ",a)
print("el vector B: ",b)
print("el vector C: ",c)