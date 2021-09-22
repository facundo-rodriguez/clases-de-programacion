#Ingresar un número y mostrar su cubo. 
#Repetir esta operación hasta que se ingrese un número negativo o igual a cero.


while True:

    print("Para terminar ingrese un numero negativo o 0")

    numero=float(input("ingrese un numero: "))

    cubo=numero**3

    print("el cubo de ",numero," es ",cubo)

    if( (numero<0) or (numero==0) ):
        break
