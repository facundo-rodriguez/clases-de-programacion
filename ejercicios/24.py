#Desarrollar un programa que permita ingresar los tiempos de viaje de los tramos
#y entregue como resultado el tiempo total del viaje en formato horas:minutos
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

total_min=0

while True:

    tiempo=int(input("ingrese la duracion del tramo en minutos: "))

    if(tiempo<0):
        
        print("el tiempo ingresado es incorrecto, hagalo nuevamente")

        tiempo=int(input("ingrese la duracion del tramo en minutos: "))

    
    total_min+=tiempo

    if(tiempo==0):
        break



minutos_mostrar=total_min%60

horas_mostrar= (total_min - minutos_mostrar)/60

print("el tiempo total del viaje es: ",horas_mostrar,"hs : ",minutos_mostrar,"min")

#total de minutos ingresados print(total_min)
#print(total_min%60) minutos a mostrar
#print(total_min//60) horas a mostrar