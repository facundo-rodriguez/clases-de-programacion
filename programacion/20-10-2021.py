#los datos del cliente son:
#-nº de cliente a
#-posee casa propia b
#-posee una segunda casa con otra compañia c
#-posee oficina d
#-posee seguro de oficina con otra compañia e
#-ingresos brutos mensuales f


#persona=[ a, b, c, d, e, f]
#clientes=[[persona1],[persona2],[persona3],etc]


clientes=[]

#contador_clientes=0

while True:

    ingresar_cliente=input("¿quiere ingresar un cliente? si/no: ")

    if(ingresar_cliente=="si"):


        a=int(input("ingrese el nº de cliente: "))
        b=input("ingrese si posee casa propia si/no: ")
        c=input("ingrese si posee seguro de casa con otra compañia  si/no: ")
        d=input("posee oficina si/no: ")
        e=input("ingrese si posee seguro de oficina con otra compañia si/no: ")
        f=float(input("ingrese el salario bruto mensual: "))


        persona=[ a, b, c, d, e, f]
        
        clientes.append(persona)

        print(clientes)
        print(persona)
        #contador_clientes+=1

    else:
        break


#-cantidad de clientes que poseen seguro de casa y/o oficina
#-el promedio de ingresos brutos mensuales de aquellos clientes que tienen seguro de casa contratado
#-el rango de ingresos brutos(maximo y minimo) de los clientes con casa propia


#clientes=[ ["facu","25","san martin"], ["luca","14","san martin"]


'''
i:  0   
        j:  0  1  2  3  4   5

            1 si si si si 2000000
                  +     +
    1
            2 si si si si 4000000
                  +     +

    2
            3 si si si si 6000000
                  +     +

'''

clientes_seguros=0
salario=0

max_min=[]


for i in range(len(clientes)):

    if(clientes[i][1]=="si"):
 
        max_min.append(clientes[i][-1])


            
    if( clientes[i][2]=="si" ):
                
        clientes_seguros+=1
                
        print(clientes_seguros)

        salario+=clientes[i][-1]

    else:           
        if( clientes[i][4]=="si" ):

            clientes_seguros+=1       
            #salario+=clientes[i][-1]

        
    



max_min.sort(reverse=True)
print(max_min)
print("el maximo de ingresos brutos es: ", max_min[0])               

max_min.sort()
print(max_min)
print("el minimo de ingresos brutos es: ", max_min[0])

                

print("la cantidad de clientes con seguro es: ", clientes_seguros)

promedio_salario=salario/clientes_seguros
print("el promedio de los salarios de los clientes con seguro de casa contratado es: ",promedio_salario)




