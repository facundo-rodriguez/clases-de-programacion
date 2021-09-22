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



