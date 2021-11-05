



socios= cuotas()

socios.Carga_Socios()

print("sistema de club")
print("ingrese opcion")
print("1- cantidad de socios activos")
print("2-cantidad de ingreso por cuota social")
print("3-cantidad de socios activos que no pagaron la cuota")
print("4-promedio de ingresos por cuota social")
print("5-salir del progragrama")

opcion=int(input())

contador=0
if(opcion==1):

    for i in range(len(socios)):
        if(socios[i][1]==True):
            contador+=1

    print("la cantidad de socios activos es: ",contador)


acumulador=0
if(opcion==2):

    for i in range(len(socios)):
       
            acumulador+=socios[i][2]

    print("la cantidad de ingresos por cuota social es: ",acumulador)


contador=0
if(opcion==3):

    for i in range(len(socios)):
        if( (socios[i][1]==True) and (socios[i][2]==0) ):
            contador+=1

    print("la cantidad de ingresos por cuota social es: ",contador)




acumulador=0
contador=0

if(opcion==4):
    
    for i in range(len(socios)):

        if(socios[i][2]!=0):
            acumulador+=socios[i][2]
            contador+=1

    promedio=acumulador/contador
    
    print("el peomedio de ingresos por cuota del mes anterior es: ",promedio)
