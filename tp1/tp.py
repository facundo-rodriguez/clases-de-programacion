# 1.-  Sistema de Promedios
# Escribir un programa para calcular el promedio de una lista de números positivos acabada en un número negativo.
# NOTA: El 0 (cero) se toma como negativo

# entrada: ingresar minimo dos numeros n mayores a 0
# proceso:imprimir todos los numeros de n
#        sumar todos los numeros
#        dividir el resultado de la suma por la cantidad de numeros (promedio)
# fin: obtuve el promedio



#while valor >0 

'''
bandera= True

cantidad= 0

num= float(input("ingrese un numero  positivo "))

lista=0

while(bandera):

    if(num <= 0):
        print("debe ingresar un numero positivo")
        num= float(input("ingrese un numero  positivo "))

    else:
        cantidad+=1
        lista+=num

        pregunta= input("¿quiere ingresar otro numero? ¿si o no?")
        pregunta= pregunta.lower()

        if(pregunta=="no" and cantidad<=1):
            print("Debe ingresar otro numero")
            num= float(input("ingrese un numero  positivo "))

        elif(pregunta=="si"):
            num= float(input("ingrese un numero  positivo "))

        else:
            break    


print(cantidad)
print(lista)

promedio=lista/cantidad

print(f"el promedio es {promedio}")
'''



#2.-  Sistema de numeración.

#Escribir un programa que lea números hasta que se encuentre el cero. El segundo número se sumará al primero, luego el tercero se restará, el 
#cuarto se sumará, y así se deberá seguir alternando hasta que se llegue al cero. 
#Cuando se llegue a esta condición deberá imprimir el resultado y el  total de operandos de la operación (sin incluir el cero)


#entrada: ingresar un numero n
#proceso: recorro el numero buscando un 0. Cuando lo encuentro termino el programa
          #for i in n
                #if i==0
                    #print("encontre el cero")
                    #break
         
        #Si no encuentro el 0:
        #Voy a necesitar dos contadores, un contador que empiece en 0. Si contador es par resto, si es impar sumo. Otro contador que empiece en 0
           #contador=0

           #if(contador==0):
                #resultado=i

           #elif(contador%2==0):
                #print("contador es par")
                #resultado=resultado-i

            #else
                #print("contador es impar")
                #resultado=resultado+i
            
            #contador+=1


'''

1º numero=n1+n2
2º numero=numero - n3
3º numero=numero + n4        
        
'''



numero=input("ingrese un numero")

contador=0
cantidad=0
resultado=0
bandera=True

while(bandera):
    espacio=" "
    
    if(espacio in numero):
        print("el numero no es valido, ingrese otro numero")
        numero=input("ingrese un numero")
    
    else:
        break

print("sali del while")

for i in (numero):


    #esto es par convertir el string en numero
    caracter=i
    num=int(caracter)
    print("num vale ",num)
    
    if(num==0):
        print("se encontro el 0")
        break

    if(contador==0):
        resultado=num

    elif(contador%2==0):
        
        resultado=resultado-num
        cantidad+=1
    else:
        
        resultado=resultado+num

    print("resultado vale",resultado)
            
    contador+=1

    



'''
print("el resultado es ", resultado)
print("la cantidad de operandos es ", contador)
print("cantidad es ", cantidad)

'''


'''
1º numero=n1+n2
2º numero=numero - n3
3º numero=numero + n4      

1º 2 2º 3 3º 4

numero=2
2=2+3=5
5=5-4=1
1=1+5=6
6=6-6=0

'''


#3.- Sistema de estadísticas de votos.
#El partido de Tres de Febrero esta dividido en tres secciones: norte, sur y centro. 
#El sistema debe solicitar el total de personas que están habilitadas a votar para cada sección.  
#Una vez ingresados el total de votantes, se debe ingresar la cantidad de personas que realmente fueron a votar.
#El sistema debe mostrar por pantalla, la cantidad y el porcentaje de votantes asistentes por cada sector.
#Restricciones: La cantidad de personas que fueron a votar no puede ser negativo ni mayor a la cantidad habilitada

#entrada: 
        # N ingresar habilitados para votar en:norte
        # C ingresar habilitados para votar en:centro
        # S ingresar habilitados para votar en:sur

        #VN ingresar los que votaron en:norte
        #VC ingresar los que votaron en:centro
        #VS ingresar los que votaron en:sur

#proceso:
        #evaluar si lo ingresado es valido. NO PUEDEN SER NEGATIVOS.
        #N,C,S deben ser mayor o igual a 0, sino que se ingresen otra vez
        #VN,VC,VS deben ser menor o igual a N,C,S pero mayor o igual que 0, sino que lo ingrese otra vez
        #










#en el dos ingresa numeros hasta que ingrese un 0

