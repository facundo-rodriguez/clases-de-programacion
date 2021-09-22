#Escribir un programa que pida al usuario dos palabras y que indique cual de ellas es la mas larga y 
#por cuantas letras lo es.


contador=1

array=[]

for i in range(2):

    print("ingrese la palabra numero: ",contador)

    palabra=input("ingrese la palabra: ")

    while(" " in palabra):
         print("lo ingresado esta mal, ingreselo nuevamente")
         print("ingrese la palabra numero: ",contador)
         palabra=input("ingrese la palabra: ")        

    array.append(len(palabra))

    contador+=1

long=array[0]

for i in range(len(array)):

    if(long>array[i]):
        cantidad_diferencia=long - array[i]
        print("la primer palabra es mas larga por ", cantidad_diferencia, " letras")
    
    else:
        if(long<array[i]):
            cantidad_diferencia=array[i] - long
            print("la segunda palabra es mas larga por ", cantidad_diferencia, " letras")

        else:
            continue 



print(array)

'''

palabra1=input("ingrese la primer palabra: ")
palabra2=input("ingrese la segunda palabra: ")


while True:

    if (" " in palabra1) or (" " in palabra2):
        print("lo ingresado esta mal, ingreselo nuevamente")
        palabra1=input("ingrese la primer palabra: ")
        palabra2=input("ingrese la segunda palabra: ")

    else:
        break

long_palabra1=len(palabra1)
long_palabra2=len(palabra2)


if(long_palabra1>long_palabra2):

    cantidad_diferencia=long_palabra1 - long_palabra2
    print("la primer palabra es mas larga por ", cantidad_diferencia, " letras")

elif(long_palabra2>long_palabra1):

    cantidad_diferencia=long_palabra2 - long_palabra1
    print("la segunda palabra es mas larga por ", cantidad_diferencia, " letras")

else:
    print("las dos tienen la misma cantidad de letras")

'''