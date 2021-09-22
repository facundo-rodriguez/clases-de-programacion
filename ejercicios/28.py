#Una empresa de colectivos tiene 3 lineas de 12 coches cada una.
#Por cada viaje el chofer entrega al llegar a la terminal una planilla
#con el número de coche (de 1 a 12), número de línea (de 1 a 3) y la recaudación del viaje.
#Las planillas se entregan sin ningún orden. 
#Se pide informar por pantalla:
# La recaudación total por linea de colectivo.
# La recaudación total por coche.
# La recaudación total general.

linea_1=[0,0,0,0,0,0,0,0,0,0,0,0]
linea_2=[0,0,0,0,0,0,0,0,0,0,0,0]
linea_3=[0,0,0,0,0,0,0,0,0,0,0,0]

opcion=1

while opcion==1:
    linea=int(input("ingrese la linea (1,2 o 3)"))
    coche=int(input("ingrese el coche del 1 al 12"))

    recaudacion=float(input("ingrese la recaudacion: "))

    if linea==1:
        linea_1[coche-1]+=recaudacion

    if linea==2:
        linea_2[coche-1]+=recaudacion
    
    if linea==3:
        linea_3[coche-1]+=recaudacion

    opcion=3
    while opcion!=1 and opcion!=2:
        opcion=int(input("desea ingresar otra planilla: (1=SI / 2=NO"))



#------------------------------------------------------------------
    
total1=0
total2=0
total3=0

for i in range(12):
    total1+=linea_1[i]
    total2+=linea_2[i]
    total3+=linea_3[i]

print("El total por linea es: ")
print("Linea 1:",total1)
print("Linea 2:",total2)
print("Linea 3:",total3)


#------------------------------------------------------------------

print("linea 1")

for i in range(12):
    print("coche ",i+1, ":",linea_1[i])


print("linea 2")

for i in range(12):
    print("coche ",i+1, ":",linea_2[i])


print("linea 3")

for i in range(12):
    print("coche ",i+1, ":",linea_3[i])

#------------------------------------------------------------------

total_general=total1 + total2 + total3
print("el total general es: ",total_general)