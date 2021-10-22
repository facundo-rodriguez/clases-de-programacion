'''

'''

palabra="cielo"

array_lineas=["_","_","_","_","_"]

#print(array_lineas)



def imprimir_lineas():

    for i in range(len(array_lineas)):

        print(array_lineas[i]," ", end="")





def acerto():

    resultado=True

    for i in range(len(palabra)):

        if(palabra[i] != array_lineas[i]):

            resultado=False

    return resultado





def imprimoAhorcado(errores):

    if(errores==1):
        print("#####")
    
    if(errores==2):
        print("#####")
        print("{0 0}")
        print("{  }")

    if(errores==3):
        
        print("#####")
        print("{(2)  (2)}")
        print("{ = }")

   




imprimir_lineas()
print("")


opciones=0
fallo=0

while opciones<7 and not acerto() :
   
    bandera=False


    print("primer badndera", bandera)
    letra=input("ingrese una letra: ")

    for i in range(len(array_lineas)):

        if ( palabra[i]==letra ):

            array_lineas[i]=letra

            bandera=True

    
    if(bandera==False):
        fallo+=1

        imprimoAhorcado(fallo)
        print(bandera)


    opciones+=1



imprimir_lineas()

