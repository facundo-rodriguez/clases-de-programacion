#Cantidad de decimales que queremos, lo podemos redondear, decirle cuantos decimales queremos.
#Con la funcion round podemos redondear un numero pero hay que deirle cuantos decimales queremos.
#El segundo parametro es la cantidad de decimales.


#nuemro=round(10/3,2)

numero=10/3,2

numero_redondeado=round(numero,2)


#{:.2f} se refiere a una variable, el format es necesarion para que se imprima
# y los parametros del format tienen que estar en el orden que quiero que se imprima.
#El 2f es la cantidad de decimales que quiero ver.

numero2=20/3
print("{:.2f}".format(numero2))

altura=1.752
peso=65.658

print("mi altura es {:.2f} y mi peso {:.2f}".format(altura,peso))


#--------------------------------------------------------------

#Para sacar el promedio
notas=[5,6,7,8,9]

sumador=0

for i in notas:
    sumador=sumador+i


promedio=sumador/len(notas)

print(promedio)

#--------------------------------------------------------------------
#Bucle infinito


#Necesito un numero positivo

while True:
    
    notas=int(input("ingrese notas: "))
    
    if (notas>0):
        break     #cuando quiero que se rompa el while


while notas<=0:
    notas=int(input("ingrese nota:"))
    #cuando quiero que ingrese al while

#Necesito un numero negativo

while True:
    
    notas=int(input("ingrese notas: "))
    
    if (notas<0):
        break


#necesito un numero negativo o positivo pero que no sea 0

while True:
    
    notas=int(input("ingrese notas: "))
    
    if (notas!=0):
        break


#necesito un numero igual a 0

while True:
    
    notas=int(input("ingrese notas: "))
    
    if (notas==0):
        break



#----------------------------

#tp ejercicio 3


print("Sistema de votacion")

padron_norte=int(input("ingrese la cantidad de votantes en el padron en zona norte"))

while(True):

    votantes_norte=int(input("ingrese la cantidad de personas que fueron a votar en zona norte"))
    
    if (votantes_norte<=padron_norte):
        break

promedio_norte=round(votantes_norte*100,padron_norte,2)


