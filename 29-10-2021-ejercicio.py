#Ejercicio modelo de parcial.


#Una empresa de tratamiento de efluentes desea analizar la capacidad y producción de una de sus plantas, 
#para ello se programó la clase Aguas, con un método con la siguiente información del último mes:

#Día del mes (nombre del campo: dia)

#Cantidad en litros de efluentes que ingresaron en la planta. (nombre del campo: efluentes)

#Cantidad de litros de agua que salieron de la planta. (nombre del campo: agua)

#Cantidad en kilos de material descartado (nombre del campo: descarte)


#Generar un objeto de la clase Aguas y llamar al método Cargar_Datos(), 
#este método transformará al objeto en un vector, 
#en donde en cada posición va a guardar los datos de cada día, detallados anteriormente.
#Generar un menú al usuario con las siguientes opciones:

#Mostrar el día que se generaron más litros de agua.

#Mostrar el promedio de kilos descartados en el mes.

#Mostrar el porcentaje de agua generada a partir de los litros de efluentes que ingresaron para todo el mes.

#       dia,efluentos,agua,descarte
agua=[ [1,4500,2000,5.50], [15,3000,10000,200], [20,5000,50000,40]]


mayor_cantidad=0
dia_mes=0
menor_cantidad=0
for i in range(len(agua)):

    if(menor_cantidad==0 and mayor_cantidad==0):
        menor_cantidad=agua[i][0]
        mayor_cantidad=agua[i][0]

    else:
        if(agua[i][2]>mayor_cantidad):
            mayor_cantidad=agua[i][2]
            dia_mes=agua[i][0]
    
    
print("el dia en que se generaron mas litros de agua es: ",dia_mes)


total_kilos=0
contador=0
for i in range(len(agua)):
    
    if(agua[i][3]!=0):
    
        total_kilos+=agua[i][3]
        contador+=1

promedio=total_kilos/contador #para mi es promedio=total_kilos/len(agua)

print("el promedio de kilos descartados por mes es: ",promedio,"kg")


efluentes_mes=0
agua_mes=0
for i in range(len(agua)):

    efluentes_mes+=agua[i][1]
    agua_mes+=agua[i][2]


porcentaje=(agua_mes*100)/efluentes_mes

print("el porcentaje de agua generada a partir de los efluentes que ingresaron para todo el mes es: ",porcentaje,"%")





