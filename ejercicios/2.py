#2.- Un alumno desea saber qué nota necesita en el tercer certamen para aprobar un ramo. 
# El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)/3

#NF=NC*0.7 + NL*0.3

#Donde NC es el promedio de certámenes(examenes), NL el promedio de laboratorio y NF la nota final. 
#Escriba un programa que pregunte al usuario las notas de los dos primeros certámenes y la nota de laboratorio, 
#y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ejemplo:
#Ingrese nota certamen 1: 45
#	Ingrese nota certamen 2: 55
#	Ingrese nota laboratorio: 65
#	Necesita nota 72 en el certamen 3

#NF=NC*0.7 + NL*0.3
#60=  [(100+72/3)*0.7] + 65*0.3  #NO LLEGA A 60 :/
#60=  100+C3/3)*0.7    +  19.5


#despejar nc de nf y despues reemplazarlo en la formula nc

c1=float(input("ingrese nota certamen 1: "))
c2=float(input("ingrese nota certamen 2: "))
laboratorio=float(input("ingrese nota de laboratorio: "))

while(True):
    
    if(c1<0):
        print("el dato ingresado es incorrecto, ingreselo nuevamente")
        c1=float(input("ingrese nota certamen 1: "))

    elif(c2<0):
          print("el dato ingresado es incorrecto, ingreselo nuevamente")
          c2=float(input("ingrese nota certamen 2: "))
    
    elif(laboratorio<0):
        print("el dato ingresado es incorrecto, ingreselo nuevamente")
        laboratorio=float(input("ingrese nota de laboratorio"))

    else:
        break


nf=60

nl=laboratorio*0.3

nc=(nf-nl)/0.7
nc=round(nc,2)
print(nc)

c3=(nc*3)-(c1+c2)
c3=round(c3,2)

print("lo que necesita en el certamen 3 es: ",c3)


