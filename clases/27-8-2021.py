#calculadora que tenga suma, resta, division,
#que calcule si un numero es par o impar.


def menu():

    print("Sistema de Calculadora")
    print("Ingrese Opcion: ") 
    print("1=suma")
    print("2=resta")
    print("3=multiplicacion")
    print("4=division")
    print("5=calculo de numero par/impar")
    print("0=salir")


def suma():
    cantidad=int(input("cuantos numeros desea suma?: "))
    suma=0
    array=[]

    for i in range(cantidad):
        num=float(input("ingrese el numero: "))
        array.append(num)
        
        suma=suma + num

    for i in range(len(array)):
        print("los valores ingresados son: ")
        print(array[i])
    
    print("el resultado de la suma es: ",suma)


def resta(cant):
    for i in range(cant):
        if(i==0):
           resta=float(input("ingrese el numero: "))
        
        else:
            num=float(input("ingrese el numero: "))
            resta=resta-num
    
    print("el resultado de la resta es: ",resta)     



def multiplicacion():
    
    print("multiplicacion. Se multiplicaran lo numeros hasta que ingrese un 0(cero)")
    resultado=1
    
    while(num_ingresado !=0):
        
        num_ingresado=float(input("ingrese numero a multiplicar"))
        
        if(num_ingresado!=0):
            resultado=resultado * num_ingresado
    
    return resultado



def division():
    num1=float(input("ingrese el dividendo"))
    
    while(True):
        num2=float(input("ingrese el divisor"))
        if (num2!=0):
            break
    
    division=num1/num2
    print("el resultado de la divisio es: ",division)



def par_impar(a):
    resultado=a%2
    
    return resultado


while(True):

    menu()


    while (True):
        opcion=int(input("ingrese opcion"))
        
        if (opcion>=0 and opcion<=5):
            break


    if(opcion==1):
        suma()


    if(opcion==2):
        cantidad=int(input("cuantos numeros desea restar?: "))
        resta(cantidad)


    if(opcion==3):
    
        rdo=multiplicacion()
        print("el resultado de la multiplicacion es ",rdo)

        print("el resultado de la multiplicacion es: ",multiplicacion())


    if(opcion==4):
        division()



    if(opcion==5):
        nro=int(input("ingrese numero a verificar si es par o impar"))

        resto=par_impar(nro)

        if(resto==1):
            print("el numero ingresado es impar")
        
        else:
            print("el numero ingresado es par")
        

    if(opcion==0):
        break