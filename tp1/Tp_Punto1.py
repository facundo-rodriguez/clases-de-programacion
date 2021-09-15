# 1.-  Sistema de Promedios
# Escribir un programa para calcular el promedio de una lista de números positivos acabada en un número negativo.
# NOTA: El 0 (cero) se toma como negativo

cantidad= 0

print("Sistema para calcular el promedio")


num= float(input("ingrese un numero  positivo "))

lista=0

while(cantidad==0 and num<=0):

    print("error, debe ingresar al menos un numero positivo")
    num= float(input("ingrese un numero  positivo "))
    
    

while(num>0):

    lista+=num
    cantidad+=1
    
    print("Si ingresa el 0 o un numero negativo podra ver el promedio")
    num= float(input("ingrese un numero  positivo "))




   
promedio=lista/cantidad

print(f"el promedio es {promedio}")




