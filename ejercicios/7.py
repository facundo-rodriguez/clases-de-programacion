#Sistema que pida un número del 1 al 12 y muestre a que mes corresponde.

meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

numero=int(input("ingrese un numero entre 1 y 12: "))

while True:

    if((numero<1) or (numero>12)):
        print("el numero ingresado es incorrecto, ingreselo nuevamente.")
        numero=int(input("ingrese un numero entre 1 y 12: "))

    else:
        numero-=1
        mostrar_mes=meses[numero]

        print("el mes correspondiente es: ", mostrar_mes)

        opcion=input("quiere saber otro mes? si/no")
        opcion=opcion.lower()

        if opcion=="si":
            numero=int(input("ingrese un numero entre 1 y 12: "))
        
        else:
            break

print("fin del programa")
