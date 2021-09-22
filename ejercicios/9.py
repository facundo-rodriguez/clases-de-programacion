#Sistema que lee una hora en hora:minutos:segundos y diga si es una hora posible.

segundos_ingresados=int(input("ingrese los segundos: "))
minutos_ingresados=int(input("ingrese los minutos: "))
horas_ingresados=int(input("ingrese las horas: "))

if(segundos_ingresados>=60):
    print("los segundos estan mal, la hora no es posible :/")

elif(minutos_ingresados>=60):
    print("los minutos estan mal, la hora no es posible :/")

else:
    print("la hora ingresada esta bien")

    print("la hora es: ",horas_ingresados,":",minutos_ingresados,":",segundos_ingresados)