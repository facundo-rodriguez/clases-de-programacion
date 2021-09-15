#Programa de cajero automático.
#Pedir la cantidad a retirar y mostrar la combinación de billetes para llegar a la cantidad deseada.
#Billetes disponibles: 500, 100, 50, 10.

#entrada: 
#       pedimos la cantidad. (tiene que ser divisible por 10)

#proceso:
#       evaluamos la cantidad.

#       

'''
cantidad = int(input("ingrese cantidad: "))
 
cant500 = cantidad // 500
resto500 = cantidad % 500
print("el resto de 500 es: ",resto500)
cant200 = resto500 // 200
resto200 = resto500 % 200
print("el resto de 200 es: ",resto200)
cant100 = resto200 // 100
resto100 = resto200 % 100
 
print("cant de billetes de 500: ", cant500)
print("cant de billetes de 200: ", cant200)
print("cant de billetes de 100: ", cant100)

'''

#el numero ingresado no puede ser menor a 0 y tiene que ser multiplo de 10.
#el numero no puede ser 0.



while True:
    cant_solic=int(input("ingrese la cantidad deseada: "))

    resto=cant_solic%10

    if(cant_solic > 0) and (resto==0):
        break


#1670

resto_500= cant_solic%500  #calculo el resto sobre 500
#170      =  1670% 500
cant_redondeada=cant_solic-resto_500  #resto a la cantidad originial, el resto de la division por 500
#1500     =  1670-170
cant_bille500=cant_redondeada/500  #divido el numero divisible por 500
#3         =   1500/500


cantidad_100=resto_500


resto_100=cantidad_100%100 #calculo el resto sobre 100
#70         170%100
cant_redondeada=cantidad_100-resto_100 #resto al cantidad original, el resto de la divison por 100
#100                170-70
cant_bill100=cant_redondeada/100 #divido el numero divisible por 500
#1              100/100



cantidad=resto_100

resto_50=cantidad%50
#20     =    70%50

cantidad_redondeada=cantidad-resto_50
#50    =     70-20
cant_bill50=cantidad_redondeada/50
#1 =        50/50


cant_bille10=resto_50/10
#