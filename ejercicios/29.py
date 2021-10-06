
def calculo_promedio(array):

    lista=0

    for i in range(len(array)):

        lista+=array[i]

    promedio=lista/len(array)

    return promedio


def menu():
    
    print("elija entre estas opciones: ")
    print("presione 1 para Mostrar los numeros de forma creciente")
    print("presione 2 para Mostrar los numeros de forma decreciente")
    print("presione 3 para Mostrar el mayor y el menor valor")
    print("presione 4 para el promedio")
    print("presione 5 para salir")


def mayor_menor(array):

    array.sort(reverse=True)
    print("el mayor valor es: ",array[0])
    print("el menor valor es: ",array[ len(array) - 1] )




array=[]
contador=0


while contador!=10:

    num=int(input("ingrese un numero entero positivo: "))

    if(num<0):
    
        print("error, el numero ingresado es negatvio, ingrese uno positivo")
        num=int(input("ingrese un numero entero positivo: "))

    else:
        array.append(num)
        contador+=1





while True:

    menu()

    opcion=int(input("ingrese el numero de opcion que quiera ver: "))

    if (opcion==1):

        array.sort()
        print(array)

    elif(opcion==2):

        array.sort(reverse=True)
        print(array)

    elif(opcion==3):
           
        mayor_menor(array)

    elif(opcion==4):

        promedio=calculo_promedio(array)
        print("el promedio es: ", promedio )

    else:
        if(opcion==5):
            break


