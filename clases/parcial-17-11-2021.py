#numero de factura   nf
#codigo de auto parte    cod_auto_parte
#automotriz que puede ser Chevrolet 1, Peugeot 2, Citroen 3
#Precio unitario  precio_unitario
#Cantidad vendida  cantidad_vendida
#precio total  precio_total


#objeto= Partes()
#objeto.Cargar_Datos()

#facturas=[ [nf, cod_auto_parte, 1, precio_unitario, cantidad_vendida, precio_total ], [nf, cod_auto_parte, 1, precio_unitario, cantidad_vendida, precio_total ]  ]

objeto=[ [1, 2, "chevrolet", 300, 20, 1000], [2, 3, "peugeot", 300, 10, 2000], [3, 2, "chevrolet", 300, 20, 5000], [3, 2, "peugeot", 300, 20, 5000]]


def promedio():

    cantidad_vendida=0
    cantidad_facturas=0

    for i in range(len(objeto)):

        cantidad_vendida+=objeto[i][4]
        cantidad_facturas+=1

    promedio=cantidad_vendida/cantidad_facturas

    print("el promedio de la cantidad vendida por factura es: ", promedio)



def precios():

    vector=[]

    for i in range(len(objeto)):

        vector.append(objeto[i][5])

    vector.sort()

    cantidad=len(vector)
    posicion_final=cantidad-1

    print("el precio total de la factura con mayor valor es de ",vector[posicion_final])
    print("el precio total de la factura con menor valor es de ",vector[0])



def automotriz():

    peugeot=0
    chevrolet=0
    citroen=0

    for i in range(len(objeto)):

        marca=objeto[i][2]
        cantidad_vendida=objeto[i][4]
        
        if(marca=="peugeot"):
            
            peugeot+=cantidad_vendida

        if(marca=="chevrolet"):
            chevrolet+=cantidad_vendida

        if(marca=="citroen"):
            citroen+=cantidad_vendida


    if(peugeot>citroen)and (peugeot>chevrolet):
            print("La automotriz que mas vendio fue: peugeot")

    elif(citroen>peugeot)and(citroen>chevrolet):
            print("La automotriz que mas vendio fue: citroen")

    else:
        if(chevrolet>peugeot)and (chevrolet>citroen):
                print("La automotriz que mas vendio fue: chevrolet")
        
        else:
            print("todas las marcas vendieron lo mismo")




while True:

    print("elija que quiere ver:")
    print("1-promedio de cantidad vendida por factura")
    print("2- precio total de factura con menor y mayor valor")
    print("3-automotriz que mas unidades compro en el año")
    print("4-salir")

    opcion=0

    while(opcion>4 or opcion<1):
        opcion=int(input("ingrese el numero de opcion: "))

   
    if(opcion==1):
        promedio()

    elif(opcion==2):
        precios()

    elif(opcion==3):
        automotriz()

    else:
        if(opcion==4):
            break