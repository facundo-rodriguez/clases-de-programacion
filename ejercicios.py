'''
Ejercicios para usar for
1.	Escribir un programa que muestre los números del 1 al 10 por pantalla.
2.	Escribir un programa que muestre los números impares del 1 al 50 por pantalla
3.	Escribir un programa que muestre los números del 50 al 70
4.	Escribir un programa que muestre los números pares del 100 al 200

'''

'''

print("ejercicio 1")

for i in range(1,11):
    print(i)

print("ejercicio 2")

for i in range(1,51,2):
    print(i)

print("ejercicio 3")

for i in range(50,71):
    print(i)

print("ejercicio 4")

for i in range(100,202,2):
    print(i)


'''

'''

Ejercicios para utilizar condicionales
1.	Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula
3.	Programa que pida la nota de un alumno y muestre desaprobado, aprobado según la misma.



print("empieza otra vez")

palabra=input("escriba algo")
#palabra.isalpha
#palabra.isdigit

for i in palabra:

    if(i==" "):
        continue

    elif(i.isalpha()):
        print(i," es una letra")

        if(i.islower()):
            print(i, " es minuscula")
        else:
            print(i, " es mayuscula")    
        
        break
    
    elif(i.isdigit()):
        print(i, " es un numero")
        
        break

    else:
        print(i, " no es letra ni numero")

        break        
'''

#2.	Se leen tres valores que corresponden al día, mes y año. Verificar si los datos constituyen una fecha posible o no.

dia=int(input("ingrese el numero de dia"))
mes=int(input("ingrese el numero de mes"))
año=int(input("ingrese el año"))

#si el mes es febrero o 2 el dia no puede ser mayor a 28
#si el mes es enero o 1, marzo o 3, mayo o 5, julio o 7, agosto o 8, octubre o 10, diciembre o 12, el dia no puede ser mayor a 31

#Dias=range(1,32)
#list=list(Dias)

#Meses=range(1,13)
#Mlist=list(Meses)
mes30=[2,4,6,9,11]
mes31=13578

if((mes>=13 or mes<=0) or (dia>=32 or dia<=0) or (año<=0)):
    print("la fecha no es posible, ingresela otra vez")

elif((mes in (2,4,6,9,11)) and (dia>30)):
     print("la fecha no es posible, ingresela otra vez")

elif((mes==2 and dia>29)):
        print("esta fecha no es posible")

else: 
    print("la fecha es posible")
    print("la fecha es ",dia,"/",mes,"/",año)
    
    





#if(mes in x):
#    print("mes esta en la lista")


#print(x[3])



'''
print("escalera de *")
#escalera de *
pisos=int(input("ingrese un numero"))

for i in range(pisos,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")   
'''
'''
pisos = int(input("Ingresa la cantdad de pisos a imprimir"))
pisos += 1
for i in range(pisos,0,-1):
	for j in range(i):
	 print("*", end="")

	print("\n")
'''