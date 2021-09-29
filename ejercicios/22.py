#Escribir un programa que calcule y visualice el mas grande, el más pequeño y el promedio de N números. 
#El ingreso de número termina cuando el usuario introduce un cero.


print("el programa terminara cuando ingrese un 0")

array=[]

lista=0

while True:
   
    num=float(input("ingrese un numero: "))

    if(num==0):
        break

    array.append(num)

   

contador=len(array)


for i in range(len(array)):

    lista+=array[i]


promedio=lista/contador

print("el promedio de los numeros es: ",promedio)
    


mayor=array[0]

for i in range(len(array)):

    if(mayor < array[i]):
        
        mayor=array[i]

print("El mayor numero es",mayor)



menor=array[0]

for i in range(len(array)):

    if(menor>array[i]):

        menor=array[i]

print("El menor numero es",menor)


'''
print("el programa terminara cuando ingrese un 0")

array=[]

contador=0
lista=0

while True:
   
    num=float(input("ingrese un numero: "))

    if(num==0):
        break

    lista+=num

    array.append(num)

    contador+=1

    

promedio=lista/contador

array.sort(reverse=True)
print("el numero mas grande es: ",array[0])

array.sort()
print("el numero mas chico es: ",array[0])

print("El promedio de los numeros ingresados es: ", promedio)

'''