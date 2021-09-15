
'''
Esta forma se utiliza cuando no sabemos cuantas posiciones tenemos
que agragar al array.

'''

temperatura=[]

for i in range(7):

    grados=float(input("Por favor ingrese la temperatura promedio:"))
    
    temperatura.append(grados)


#------------------------------------------------------

'''
De esta forma cargamos valores en un array que ya tiene
las posiciones creadas.
'''
temp=[0,0,0,0,0,0,0]


for i in range(7):

    temp[i]=float(input("Por favor ingrese la temperatura promedio:"))



#-------------------------

suma=temp[0] + temp[1] + temp[2] + temp[3] + temp[4] + temp[5] + temp[6]


suma=0
suma= suma + temp[0]
suma= suma + temp[1]
suma= suma + temp[2]
suma= suma + temp[3]
suma= suma + temp[4]
suma= suma + temp[5]
suma= suma + temp[6]


'''
Con este for obtengo la suma de todas las posiciones(elementos) del array.
'''
suma=0
for i in range(7):

    suma= suma + temp[i]

promedio=suma/7

len("Frase")

nombre="Gaston"
len(nombre)


#Esto devuelve la cantidad de elementos o posiciones que hay en el array
cantidad=len(temp)

suma=0
for i in range(cantidad):
    
    suma=suma + temp[i]

promedio=suma/cantidad


print("La temperatura promedio es: ",promedio)


#----------------------------------------

print("La temperatura es: ",temp[0])
print("La temperatura es: ",temp[1])
print("La temperatura es: ",temp[2])
print("La temperatura es: ",temp[3])
print("La temperatura es: ",temp[4])
print("La temperatura es: ",temp[5])
print("La temperatura es: ",temp[6])

'''
lo de arriba da lo mismo que lo de abajo
'''

for i in range(7):
    print("La temperatura es: ",temp[i])




#-------------------------------------------------

'''
Como no tengo con que compararlo inicio la variable con el primer elemento del array.
'''
mayor=temp[0]

for i in range(7):

    if (temp[i]>mayor):
        
        mayor=temp[i]

print("La mayor temperatura es: ",mayor)



menor=temp[0]

for i in range(7):

    if (temp[i]<menor):
        
        menor=temp[i]

print("La mayor temperatura es: ",menor)