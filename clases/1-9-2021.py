

vector=[1,5,"Terciario",1.5]

vectorAlumno=["Sebastian",25,3]
vectorAlumno2=["Maria",20,1]
vectorAlumno3=["Juan",35,2]
vectorAlumno4=["Julieta",19,2]

ListaGral=[ ["Sebastian",25,3], ["Maria",20,1], ["Juan",35,2,"Aprobado"], ["Julieta",19,2] ]

print(ListaGral[0]) #va a imprimir los datos de la posicion 0, es decir,
                    #sebastian,25,3.


#si quiero solo un dato del array anidado
print(ListaGral[2][0]) #va a imprimir Juan, xq es el primer elemento
                       #del array en la posicion 2.



#Esto recorre todo el array y me muestra los datos que tiene
for i in range(len(vectorAlumno)):
    print(vectorAlumno[i])


#Esto me va a imprimir todos los datos de cada posicion
for i in range(len(ListaGral)):
    print(ListaGral[i])


#el len se usa cuando no sabes cuantos elementos hay en el array

#Esto es para recorrer un array anidado dentro de otro
suma=0

for i in range(len(ListaGral)):
    print(i)
    
    for j in range(len(ListaGral[i])):
        if(j==1): #para imprimir solo las edades
            print(" ", j, ListaGral[i][j] )
            suma=suma+ListaGral[i][j]

promedio=suma/4 #si se cuantos alumnos hay
promedio1=suma/len(ListaGral) #si no se cuantos alumnos hay

print("el promedio es ",promedio1)


#Para guatadar datos del usuario dentro de un array
temperatura=[]
temp=float(input("ingrese la temperatura: "))
temperatura.append(temp)


#Con esto guardo un array dentro de otro array
nombre=input("ingrese el nombre del alumno: ")
edad=int(input("ingrese la edad del alumno: "))
curso=int(input("ingrese el curso a anotarse: "))

vector=[nombre,edad,curso]
ListaGral.append(vector)


#------------------------------------------------

#Escalera

pisos=int(input("ingrese la cantidad de escalones: "))

'''
for i in range(pisos):
    cantidad_imp= i+1 #si pisos=5  i va a valer 0,1,2,3,4
    print("")
    for j in range(cantidad_imp):
        print("#", end="")
'''

for i in range(pisos):
    cant=pisos + 1
    print(cant)

    for j in range(cant):
        print("  ",cant)