#2.-  Sistema de numeración.

#Escribir un programa que lea números hasta que se encuentre el cero. El segundo número se sumará al primero, luego el tercero se restará, el 
#cuarto se sumará, y así se deberá seguir alternando hasta que se llegue al cero. 
#Cuando se llegue a esta condición deberá imprimir el resultado y el  total de operandos de la operación (sin incluir el cero)

#ingresa numeros hasta que ingrese un 0
#un contador que empiece en 0. Si contador es par resto, si es impar sumo.

contador=0
resultado=0
opercaiones=0

print("Cuando ingrese 0 se mostrara el resultado y la cantidad de operandos")

numero=float(input("ingrese un numero"))

while(numero!=0):

    if(contador==0):
        resultado=numero

    else:
        
        if(contador%2==0):
        
             resultado=resultado-numero

             opercaiones+=1
             
        else:
        
             resultado=resultado+numero

             opercaiones+=1
            
    
    contador+=1 
   
    numero=float(input("ingrese un numero"))
    


print("el resultado es ",resultado)

print("la cantidad de operandos es ", contador-1) #o opercaiones


