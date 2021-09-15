#El precio final de un producto para un comprador es la suma total del costo del producto, 
#un porcentaje de beneficios que obtiene el vendedor y el IVA. 
#Diseñar un algoritmo para obtener el precio final de un producto sabiendo su costo, 
#el porcentaje de beneficios y el IVA aplicable.



#calculo iva:
#Tomar el total de la factura y dividirlo por 1,21. Así se obtendrá el importe neto de la factura (el precio sin IVA).
#A este importe se le debe aplicar la alícuota del IVA, por ejemplo el 21%. Multiplicando el neto por el porcentaje se obtiene el impuesto.
#Sumar el neto obtenido en el punto 1 y el IVA obtenido en el punto 2 y se tendrá el total de la factura.


#entrada:
#       ingreso del costo producto(cp).  no puede ser menor a 0
#       ingreso un porcentaje del vendedor(porcentaje). no puede ser menor a 0 
#       ingreso el porcentaje del iva que quiere calcular(iva). no puede ser menor a 0

#proceso:
#       calcular cual es el precio del producto(pp) con el porcentaje de ganancia(pg), es decir,pp= cp + pg.
#       para eso el porcentaje del vendedor se saca con respecto al precio costo:
#       100%-----cp
# porcentaje-----pg     
#                    (porcentaje*cp)/100=pg

#       al precio obtenido agregarle el iva y obtengo el precio final, pf=pp*1.21
#       pf=pp*1.iva    si el iva es menor a 10 queda 1.0iva
#           o
#       iva=(iva*pp)/100
#       pf=pp+iva


print("calcule el precio de venta de su producto con el iva incluido")


def ingreso_datos():

    costo_producto=float(input("ingrese el monto del costo de su producto: "))

    porcentaje=float(input("ingrese el porcentaje de ganancia que desea obtener: "))

    iva=float(input("ingrese el porcentaje de iva correspondiente: "))

    return costo_producto, porcentaje, iva



def evaluar(costo_producto, porcentaje, iva):

    while(True):#while( (cp<0) or (porcentaje<0) or (iva<0) )
        
        if(costo_producto<0):
            print("el costo ingresado esta mal, ingreselo nuevamente")
            costo_producto=float(input("ingrese el monto del costo de su producto: "))
        
        else:
            if(porcentaje<0):
                print("el porcentaje ingresado esta mal, ingreselo nuevamente")
                porcentaje=float(input("ingrese el porcentaje de ganancia que desea obtener: "))
            
            else:
                if(iva<0):
                    print("el iva ingresado esta mal, ingreselo nuevamente")
                    iva=float(input("ingrese el porcentaje de iva correspondiente: "))
                
                else:
                    return costo_producto, porcentaje, iva 



def calculo_precio(costo_producto,porcentaje,iva):


    porcentaje_ganancia=(porcentaje*costo_producto)/100

    precio_producto=costo_producto + porcentaje_ganancia

    iva=(iva*precio_producto)/100

    precio_final=precio_producto + iva

    return precio_final



costo_producto,porcentaje,iva=ingreso_datos()

costo_producto,porcentaje,iva=evaluar(costo_producto, porcentaje, iva)

precio_final=calculo_precio(costo_producto,porcentaje,iva)

print("el precio final del producto con iva incluido es: ",precio_final)


while (True):

    opcion=input("quiere calcular el precio de otro producto? si/no: ")
    opcion=opcion.lower()

    if(opcion=="si"):

        costo_producto,porcentaje,iva=ingreso_datos()

        costo_producto,porcentaje,iva=evaluar(costo_producto, porcentaje, iva)

        precio_final=calculo_precio(costo_producto,porcentaje,iva)

        print("el precio final del producto con iva incluido es: ",precio_final)

        #opcion=input("quiere calcular el precio de otro producto? si/no: ")
    
    else:
        break


print("fin del programa")