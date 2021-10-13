#Escribir un programa que cargue un vector de 10 elementos. 
#Luego leer dos números mas e indicar si éstos están entre los anteriores.

array=[]

print("ingrese 10 numeros")

for i in range(10):

    print("valor numero ",i+1)
    n=float(input("ingresar un numero: "))

    array.append(n)


for i in range(2):

    num=float(input("ingresa el numero a buscar: "))

    if( num in array):

        print("el ",i+1,"º ","numero ingresado ",num," se encuentra en el array")

    else:
        print("el ",i+1,"º ","numero ingresado ",num," no se encuentra en el array")

