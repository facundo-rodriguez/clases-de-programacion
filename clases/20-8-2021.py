motos=["XR","Ninja","Honda"]
autos=["Corsa","Unos","600"]
numeros=[5,6,7,9,2,1]
colores=["Rojo","Naranja","Blanco","Verde"]

print(numeros)
numeros.append(8) #agrega el 8 al final del array
print(numeros)

print(colores)
colores.append("Negro") #el append agrega un valor al final del array
print(colores)


#El clear() limpia el array, es decir, borrar todos los elementos

print(numeros)
numeros.clear() #elimina todo los elementos del array numeros
print(numeros)


variable=numeros.copy() #copia todo el array
#lo tengo que guardar en una variable


#El count() busca un elemento en particular y devuelve
#cuantas veces aparece ese elemento en el array


variable2=numeros.count(3) #busca el 3 en el array numeros y 
#guarda en la variable cuantas veces aparece en el array
print(variable)

#El extend() agrega un array a otro array, 
#agrega los elementos de un array a otro array, lo agrega al final

vehiculos=[]
print(vehiculos)

vehiculos.extend(motos)
print(vehiculos)

vehiculos.extend(autos)
print(vehiculos)

#El index() busca un elemento y devuelve ala posicion en la que est
#si el elemento esta repetido devuelve el primero que encuentra

x=colores.index("Naranja")


#El insert() agrega un elemento al final del array o en una posicion determinada
colores.insert(1,"Negro") #agrega Negro al array colores en la posicion 1



#El metodo pop() borra un elemento de una posicion especifica

autos.pop(1) 
#esta borrando del array el elemento en la posicion 1, 
#es decir, el segundo elemento



#El remove() busca un elemento en especifico y lo borra

colores.remove("Naranja") 
#busca Naranja y lo borra, pero solo al primero que encuentra
#es decir que si hay mas Naranja, solo borra al primero que encuentra


#bucle infinito salgo con break


variable3= colores.count("Naranja")

#Lo que estamos haciendo es buscar cuantas veces aparece Naranja,
#luego pasamos al for esa cantidad gurdada en variable3 para que se repita esa cantidad de veces,
#luego como el remove solo borra el primero que aparece, aca va a recorrer el array buscando y borrando al primero,
#despues recorre otra vez buscando y borrando el elemento tantas veces como se encuentre en el array
for i in range(variable3): 
    colores.remove("Naranja")


#El sort() ordena los elementos de menor a mayor, en orden alfabetico
#si tiene numeros y letras me tira error
#van los numeros con los numeros y los strings con los strings

#Si le paso el parametro sort(reverse=True), 
#me ordena el array de mayor a menor


numeros.sort()
print(numeros)

colores.sort()
print(colores)

autos.sort()
print(autos)



colores_ordenados=colores.copy()
colores_ordenados.sort()


#El metodo reverse da vuelta el array, es decir, 
#al ultimo elemento lo pasa a la posicion 0 y el de la posicion 0 lo pasa a la ultima posicion
