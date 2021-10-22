#escribir un programa que pida al usuario un numero y muestre por pantalla si es primo o no

num=int(input("ingrese el numero: "))


contador=0

for i in range(num,0,-1):
    
    modulo=num%i

    if(modulo==0):
        contador+=1


if(contador>2):
    print("el numero no es primo")

else:
    print("el numero es primo")

