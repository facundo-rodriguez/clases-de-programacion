

                    
#objeto=[ [n_usuario, año,mes,consumo, origen,precio],[n_usuarioaño,mes,consumo,origen,precio], ect ]

#si origen es 1=solar, 2=eolica, 3=hidrica

#objeto=Consumos()
#objeto.Cargar_Datos()


objeto=[ [2,2018,"diciembre", 200, 1, 2000], [3,2019,"enero", 300, 3, 1000],[4,2018,"marzo", 400, 1, 4000] ]




def consumo_origen(objeto):

    
    origen1=1
    origen2=2
    origen3=3
    consumo_uno=0
    consumo_dos=0  #se inician en 0 porque es suma,
    consumo_tres=0 #si es multiplicaion se inicia en 1
    
    for i in range(len(objeto)):
        if(objeto[i][1]==2018 and origen1==objeto[4]):
            
            consumo_uno+=objeto[i][3]

        elif(objeto[i][1]==2018 and origen2==objeto[4]):
            consumo_dos+=objeto[i][3]

        elif(objeto[i][1]==2018 and origen3==objeto[4]):

            consumo_tres+=objeto[i][3]
            



    return consumo_uno,consumo_dos,consumo_tres

    
#print("el consumo es", consumo_origen(objeto))


def promedio_consumo(objeto):
    
    cantidad_usuarios=0
    consumo_total=0

    for i in range(len(objeto)):

        if( (objeto[i][2]=="enero") and (objeto[i][1]==2019)):

            cantidad_usuarios+=1
            
            consumo_total+=objeto[i][3]

        
    promedio=consumo_total/cantidad_usuarios

    return promedio

   


def consumo_energia(objeto):
    mayor_menor=[]
    for i in range(len(objeto)):

        consumo=objeto[i][3]

        mayor_menor.append(consumo)


    mayor_menor.sort()

    menor=mayor_menor[0]
    mayor=mayor_menor[-1]

    return menor,mayor
            


objeto=Consumos()
objeto.Cargar_Datos()



while True:

if(opcion==1):
    solar,eolica,hidrica=consumo_origen(objeto)

