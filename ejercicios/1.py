#Escribir un programa que reciba como entradas las longitudes de los dos catetos a y b de un triangulo rectángulo,
# y que entregue como salida el largo de la hipotenusa c del triángulo, dado por el teorema de Pitágoras.

#entrada: 
          #longitudes a y b
          #no pueden ser menor o igual a 0

#proceso:
        #pitagora: c=(a**2) + (b**2)
                  #c=sqrt(c)

#salida: hipotenusa c


#RAIZ CUADRADA: 

#-FORMA 1:
#raiz=81**0.5
#print(raiz)

#FORMA2:
#import math
#math.sqrt(x)

#FORMA 3:
#raiz=81**(1/2) o (1/2.0) o (1.0/2), raiz cubica (1/3) probar

import math


def hipotenusa(num1,num2):
    h=(num1**2)+(num2**2)
    h=math.sqrt(h) #saco la raiz cuadrada
    return h


def longitudes():
    long1=float(input("ingrese la longitud a: "))
    long2=float(input("ingrese la longitud b: "))

    while(long1<=0 or long2<=0):
        print("los datos ingresados son erroneos, ingreselos nuevamente")

        long1=float(input("ingrese la longitud a: "))
        long2=float(input("ingrese la longitud b: "))

    return long1,long2


print("calcule la hipotenusa c de un triangulo rectangulo")

while(True):

    a,b=longitudes()

    c=hipotenusa(a,b)

    print("la hipotenusa es: ",c)

    opcion=input("desea continuar? si/no: ")
    opcion=opcion.lower()

    if(opcion=="si"):
        
        a,b=longitudes()

        c=hipotenusa(a,b)

        print("la hipotenusa es: ",c)

        opcion=input("desea continuar? si/no: ")

    #else:
        #break
    break

print("fin del programa")


