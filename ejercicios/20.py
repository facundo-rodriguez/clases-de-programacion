#Escribir un programa que, dados dos números, saque por pantalla todas las potencias con base al primer número 
#y exponentes entre uno y el segundo numero ingresado. 
#Por ejemplo, si introducimos 2 y 5, se deberán mostrar el resultado de:
# 2 a la una
# 2 al cuadrado
# 2 al cubo
# 2 a la cuarta
# 2 a la quinta


base=float(input("ingrese un numero: "))

exponente=int(input("ingrese el exponente: "))


if(exponente>0):
   
    for i in range(1,exponente+1):

        potencia=base**i

        print("la potencia de ",base," elevado a ",i," es: ",potencia)

else:

    for i in range(exponente,2):

        potencia=base**i

        print("la potencia de ",base," elevado a ",i," es: ",potencia)



