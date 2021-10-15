#Escribir un programa que diga si un número introducido por teclado es o no primo.
#Un número primo es aquel que sólo es divisible entre él mismo y la unidad.

num=int(input("ingrese un numero entero: "))

contador=0

for i in range(num,0,-1):

    if(num%i==0):
        contador+=1

    


if(contador>2):
    print("el numero ",num, " no es primo")

else:
    print("el numero ",num," es primo")

