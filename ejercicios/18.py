#Realizar el control de acceso a una caja fuerte. 
#La combinación será un número de hasta 4 cifras. 
#El programa nos pedirá la combinación para abrirla. 
#Si no acertamos, se nos mostrará el mensaje “Lo siento, esa no es la combinación” 
#y si acertamos se nos dirá “La caja fuerte ha sido abierta”. 
#La combinación es un número predeterminado dentro del programa. El usuario tiene hasta 4 oportunidades.


print("tiene 4 oportunidades")

combinacion=int(input("ingresa la combinacion de hasta cuatro cifras: "))

contador=4

llave=23


while contador>0:

    if(combinacion==llave):
        
        print("La caja fuerte ha sido abierta")
        break

    else:

        contador-=1

        if(contador==0):
            print("perdio")
            break
        

        print("Lo siento, esa no es la combinación")
        print("le quedan ",contador, " intentos")

        combinacion=int(input("ingresa la combinacion de hasta cuatro cifras: "))




'''
for i in range(contador):


    if(combinacion==llave):
        
        print("La caja fuerte ha sido abierta")
        break
    
    else:
        contador-=1

        if(contador==0):
            print("perdio")
            break

        
        print("Lo siento, esa no es la combinación")
        print("le quedan ",contador, " intentos")

        combinacion=int(input("ingresa la combinacion de hasta cuatro cifras: "))


'''

#-----------------------------------

'''

def numeros():
    
    combinacion=""
    digito=1

    for i in range(4):
        
        print("ingrese el digito",digito,": ")
        n=int(input(""))

        while True:

            if(n>9 or n<-9):
                print("el numero no puede tener dos digitos, ingreselo nuevamente")

                print("ingrese el digito",digito,": ")
                n=int(input(""))

            else:
                break

        n=str(n)
        combinacion+=n

        digito+=1

    combinacion=int(combinacion)

    return combinacion


intentos=4

llave=1234

combinacion=numeros()

while True:

    if(combinacion==llave):
        print("se abrio la caja fuerte")
        break
    
    else:

        intentos-=1

        if(intentos==0):
            print("perdio")
            break

        else:

            print("lo siento, esa no es la combinacion, ingreselo nuevamente")
            print("le quedan ",intentos," intentos")
            
            combinacion=numeros()

'''

