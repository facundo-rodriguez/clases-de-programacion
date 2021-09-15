matricula=int(input("ingrese la matricula: "))

basico=float(input("ingrese el suelde basico del empleado"))

antiguedad=int("ingrese la antiguedad del empleado: ")


if antiguedad<=3:
    sueldo_cobrar=basico

else:
    if antiguedad>3 and antiguedad<=6:
        sueldo_cobrar=basico*1.15

    else:
        if antiguedad<11:
            sueldo_cobrar=basico*1.3
        else:
             sueldo_cobrar=basico*1.5


if antiguedad<=3:
    sueldo_cobrar=basico

if antiguedad>3 and antiguedad<=6:
        sueldo_cobrar=basico*1.15

if antiguedad>6 and antiguedad<11: #o <=10
            sueldo_cobrar=basico*1.3

if antiguedad>10:
        sueldo_cobrar=basico*1.5


print("el sueldo a cobrar por el empleado es: ",sueldo_cobrar)