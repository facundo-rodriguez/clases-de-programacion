#una empresa desea informar sus ventas.
#despues de hacer el relevamiento concluimos que los datos basicos de una venta son:
#-clientes cliente
#-total de factura total_factura
#-porcentaje de iva iva
#-codigo de articulo vendido cod_art_vend
#-cantidad vendida(unidades) cant_vend
#-nro de factura nro_fact

#sabemos que cada factura puede tener un solo articulo.
#el sistema debe cargar las facturas y a partit de los datos ingresados determinar:
#-a=cantidad total vendida(unidades)
#-b=promedio del importe neto de las facturas(funcion)
#-c=nro de factura con el importe total mas grande
#-d=articulo con el precio de venta por unidad y sin iva mas barato
#-e=cliente que mas gasto

#iva pos 2   factura[i][2]

#17%  1000(total)---100%
#     17%----------x= (17*100/1000)

#total de la factura pos 1 factura[i][1]


def calculo_iva(factura,i):
   
   ptf= factura[i][1]
   porcentaje_iva=factura[i][2]

   iva=(porcentaje_iva*ptf)/100
   pn=ptf-iva

   return pn

factura=[]

while True:
    #factura=[venta1, venta2,venta3,ect]

    cliente=input("ingrese cliente: ")
    total_factura=float(input("ingrese total de la factura: "))
    iva=float(input("ingrese el iva: "))
    cod_art_vend=int(input("ingrese codigo de articulo vendido: "))
    cant_vend=int(input("ingrese cantidad vendida en unidades: "))
    nro_factura=int(input("ingrese nro de factura: "))

    venta=[cliente, total_factura, iva, cod_art_vend, cant_vend, nro_factura]

    
    factura.append(venta)

    opcion=int(input("quiere ingresar otra venta? presione 1-si o 2-no :"))

    while(opcion!=1 and opcion!=2):
        opcion=int(input("quiere ingresar otra venta? presione 1-si o 2-no :"))
    
    
    if(opcion==2):

        break
        

#a
cant_total_vend=0

for i in range(len(factura)):

    cant_total_vend+=factura[i][4]


print("la cantidad total vendida es: ",cant_total_vend)


#      iva=(iva*ptf)/100
#       pn=ptf-iva

#b



importe_neto=0

for i in range(len(factura)):

    importe_neto+=calculo_iva(factura,i)


promedio=importe_neto/(len(factura))

print("el promedio del importe neto de las facturas es: ", promedio)



#c



for i in range(len(factura)):
    

    if(i==0):
        codigo_factura=factura[i][-1]
        
        importe_total=factura[i][1]

    else:

        if( factura[i][1]>importe_total ):

            codigo_factura=factura[i][-1]
        
            importe_total=factura[i][1]

print("el nro de factura con el importe mas grande es ",codigo_factura)





#d

producto=[]

for i in range(len(factura)):
        
    codigo_articulo=factura[i][3]
        
    cantidad_vendida=factura[i][4]
    
    importe_sin_iva=calculo_iva(factura,i)

    precio_unidad=importe_sin_iva / cantidad_vendida

    
    precio_codigo=[precio_unidad,codigo_articulo]

    producto.append(precio_codigo)



for i in range(len(factura)):

    if(i==0):
        precio=producto[i][0]
        codigo=producto[i][1]

    else:

        if(precio>producto[i][0]):
            
            precio=producto[i][0]
            codigo=producto[i][1]

print("el codigo del producto con el precio sin iva mas barato es: ",codigo)


'''    

#e

clientes=[]

for i in range(len(factura)):

    clien=factura[i][0]
    gasto=factura[i][1]
    
    clien_gasto=[clien,gasto]
    

    for j in range(len(factura)):
    
        if(j>0):#mal
            if(clien==factura[j][0]):
            
                clien_gasto[i][1]+=factura[j][1]
    
    
      
    clientes.append(clien_gasto)

'''            




