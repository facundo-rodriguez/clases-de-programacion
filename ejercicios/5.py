#Se leen tres valores que corresponden al día, mes y año. Verificar si los datos constituyen una fecha posible.

#meses con 31 dias:
#                  enero(1),marzo(3),mayo(5),julio(7),agosto(8),octubre(10),diciembre(12)

#meses con 30 dias:
#                  abril(4),junio(6),septiembre(9),noviembre(11)

# febrero(2) tiene 28 dias

# Proceso:
#          me ingresa el dia. si dia>31 o dia<1  no va
#          me ingresa el mes. si mes es menor a 1 o mayor a 12 no va.

#                             si mes es 4 o 6 o 9 o 11, y dia>30 no va

#                             si mes es 2, y dia>28 no va

#          me ingresa el año. si año<0 no va.


meses_30=[4,6,9,11]

dia=int(input("ingrese el numero de dia: "))
mes=int(input("ingrese el numero de mes: "))
año=int(input("ingrese el numero de año: "))


def dia_incorrecto():
        print("el dia ingresado no es posible, ingreselo nuevamente")
        dia=int(input("ingrese el numero de dia: "))
        return dia

while True:

    if ((dia>31) or (dia<1)):
        #print("el dia ingresado no es posible, ingreselo nuevamente")
        #dia=int(input("ingrese el numero de dia: "))
        dia=dia_incorrecto()
    
    elif((mes<1) or (mes>12)):
        print("el mes ingresado no es posible, ingreselo nuevamente")
        mes=int(input("ingrese el numero de mes: "))

    elif(año<0):
        print("el año ingresado no es posible, ingreselo nuevamente")
        año=int(input("ingrese el numero de año: "))

    else:

        if((mes in meses_30) and dia>30):
           # print("el dia ingresado no es posible, ingreselo nuevamente")
           # dia=int(input("ingrese el numero de dia: "))
           dia=dia_incorrecto()

        elif((mes==2) and (dia>28)):
         #   print("el dia ingresado no es posible, ingreselo nuevamente")
         #   dia=int(input("ingrese el numero de dia: "))
            dia=dia_incorrecto()
        
        else:
            break

print("la fecha ingresada es: ",dia,"/",mes,"/",año)

