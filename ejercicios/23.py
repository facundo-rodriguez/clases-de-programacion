#Escribir un programa que muestre todos los divisores del número ingresado.
#ingrese numero: 200
#1 2 4 5 8 10 20 25 40 50 100 200



num=int(input("ingrese un numero: "))

array=[]

if(num>=0):

    for i in range(1,num+1):
        
        #print(i)
        if(num%i==0):
            array.append(i)

else:
    
    for i in range(num,0):
        
        #if(i==0):
        #   i=1

        if(num%i==0):
            array.append(i)



for i in range(len(array)):

    print(array[i],"",end="")

