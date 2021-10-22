'''
Una heladeria desea saber cuantos kilos de helado debe comprar a partir de un estudio
de sus ventas. La heladeria comercia 10 gustos, y decidio la siguiente regla para comprar:

-si la venta de la ultima semana fue menos de 3kg, no realiza compras. no se incluye el 3

-si la venta fue entre 3kg y 5kg, compra un balde de 5kg. se incluye el 3 y el 5

-si la venta fue entre mas 5kg y 10 kg, compra un balde de 10 kg. no se incluye el 5  pero si el 10

-si la venta fue de mas de 10kg, compra dos baldes de 10kg. no se incluye el 10

Si el balde de 5kg sale $550 y el de 10kg $975 ¿cuanto va a pagar la heladeria para volver a tener stock?.

wifi: diosteoiga

'''

#entrada: float *10
#           ingresamos la cantidad vendida de los 10 gustos

#           la cantidad no puede ser menor a 0

#

#salida: $float


contador=1

cantidad=0

cantidad_pagar=0

while True:

    print("gusto ",contador)
    gusto=float(input("ingrese la cantidad vendida del gusto : "))

    if(gusto<0):
        print("cantidad incorrecta, ingreselo nuevamente")
        gusto=float(input("ingrese la cantidad vendida del gusto : "))

    else:

        if(gusto>=3) and (gusto<=5):
            cantidad_pagar+=550
            print("agregue 550")

        if(gusto>5) and (gusto<=10):
            cantidad_pagar+=975
            print("agregue 975")

        if(gusto>10):
            cantidad_pagar+=1950
            print("agregue 1950")

        
        cantidad+=gusto

        contador+=1

    
    if(contador==11):
        break


print("la cantidad es: ",cantidad,"kg")
print("tiene que pagar: $", cantidad_pagar)



'''

facundo sos un boludo, usa un for no un while, xq ya sabes cuantas veces los va a ingresar

la condicion lo pongo dentro del while

if(cantidad_vendida>=3) and (cantidad_vendida<=5):
    cantidad_pagar+=550

if(cantidad_vendida>5) and (cantidad_vendida<=10):
    cantidad_pagar+=975

if(cantidad_vendida>10):
    cantidad_pagar+=1950

'''