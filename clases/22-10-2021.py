#ejercicio del 20/10/2021 resuelto por el profe



cliente=[]
casa=[]
casa_seguro=[]
oficina=[]
oficina_seguro=[]
ing_men=[]


while True:

    temp_cliente=input("ingrese codigo de cliente: ")
    cliente.append(temp_cliente)


    while True:

        temp_casa=input("posee casa propia? 1-si  0-no: ")
        
        if(temp_casa==0 or temp_casa==1):
            cliente.append(temp_casa)
            break



    temp_casa_seg=2
    while temp_casa_seg!=0 and temp_casa_seg!=1:

        temp_casa_seg=int(input("posee seguto de la casa 1-si  0-no: "))

        
    casa_seguro.append(temp_casa_seg)


    while True:

        temp_ofi=input("posee oficina propia? 1-si  0-no: ")
        
        if(temp_ofi==0 or temp_ofi==1):
            oficina.append(temp_ofi)
            break



    temp_oficina_seg=2

    while temp_oficina_seg!=0 and temp_oficina_seg!=1:

        temp_oficina_seg=int(input("posee seguto de la casa 1-si  0-no: "))

    oficina_seguro.append(temp_oficina_seg)


    temp_ingresos=float(input("ingrese el salario bruto mensual: "))
    ing_men.append(temp_ingresos)

    

    cargar_otro=int(input("desa cargar otro cliente? 1-si  0-no: "))
    
    if(cargar_otro==0):
        break
    
    print("-----------------------------------------------------------")




contador=0
suma=0
promedio=0
cant_clientes=0


while True:
    
    print("ingrese la consulta que desea")
    print("1= cantidad de clientes que poseen seguto de casa y/o oficina")
    print("2-promedio de ingresos de aquellos que tienen seguro de casa contratado")
    print("3-rango de ingresos brutos de cliente con casa propia(maximo y minimo")
    print("4-terminar el programa")

    opcion=0

    while(opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4):
        opcion=int(input("ingrese opcion"))

    if(opcion==1):
        
        for i in range(len(casa_seguro)):

            if(casa_seguro[i]==1):
                contador+=1

            else:
                if(oficina_seguro[i]==1):
                    contador+=1


        print("los clientes con seguro de casa y/o oficina son: ",contador)

    
    if(opcion==2):

        for i in range(len(casa_seguro)):
            
            if(casa_seguro[i]==1):
                suma+=ing_men[i]
                cant_clientes+=1

        promedio=suma/cant_clientes

        print("el promedio de clientes con seguto de casa contratado es: ",promedio)


    if(opcion==3):
        max=-1
        min=-1

        for i in range(len(casa)):
            if(casa[i]==1):

                if(min==-1 and max==-1):
                    min=ing_men[i]
                    max=ing_men[i]

                else:

                    if (ing_men[i]<min):
                        min=ing_men[i]

                    
                    if(ing_men[i]>max):
                        max=ing_men[i]

        print("el rango de ingresos para los clientes que tiene casa propia es: ",min,"-",max)

    
    if(opcion==4):
        break


vector=[6,8,10,2,6,7,9,20,2,10]

for i in range(10):
    
    if(i==0):
        min=vector[i]
        max=vector[i]

    else:
        if(vector[i]<min):
            min=vector[i]