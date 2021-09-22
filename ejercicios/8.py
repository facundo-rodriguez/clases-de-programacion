#Sistema que muestra un menú donde las opciones sean
#“Equilatero”, “Isosceles” y “Escaleno”, pida una opción y calcule el perímetro del triángulo seleccionado.

#equilatero: 
#           3*l , tres lados iguales

#isosceles: 
#           2*l + l3 , dos lados iguales y uno distinto

#escaleno:
#         l+l+l, todos los lados distintos


print("Elija el tirangulo y se calulara el perimetro")

opcion=input("Equilatero, Isosceles, Escaleno: ")
opcion=opcion.lower()


triangulos=["equilatero","isosceles","escaleno"]



contador=1
perimetro=0

print("Ingrese la longitud de los lados ")

if(opcion=="equilatero"):
    
    lado=float(input("longitud: "))
    perimetro=lado*3

    print("El perimetro del triangulo ",opcion, "es: ",perimetro,"cm")

elif(opcion=="isosceles"):
    #print("ingrese la longitud de los los dos lados iguales")

    lado=float(input("ingrese la longitud de los los dos lados iguales: "))
    lado3=float(input("ingrese la longitud de lado desigual: "))

    if(lado==lado3):
        print("lo ingresado esta mal, es un triangulo Isosceles, solo dos lados son iguales")
        print("ingrese nuevamente los valores")

        lado=float(input("ingrese la longitud de los los dos lados iguales: "))
        lado3=float(input("ingrese la longitud del lado desigual: "))
    
    else:

        perimetro=lado*2 + lado3

        print("El perimetro del triangulo ",opcion, "es: ",perimetro,"cm")


elif(opcion=="escaleno"):

    lado=float(input("ingrese la longitud del lado 1: "))
    lado2=float(input("ingrese la longitud del lado 2: "))
    lado3=float(input("ingrese la longitud del lado 3: "))

    if(lado!=lado2):
        if(lado!=lado3):
            if(lado2!=3):

                perimetro=lado+lado2+lado3
                print("El perimetro del triangulo ",opcion, "es: ",perimetro,"cm")

            else:
                print("lo ingresado esta mal, es un triangulo Escaleno, sus tres lados no pueden ser iguales")  
                print("ingrese nuevamente los valores")

                lado2=float(input("ingrese la longitud del lado 2: "))
                lado3=float(input("ingrese la longitud del lado 3: "))


        else:
            print("lo ingresado esta mal, es un triangulo Escaleno, sus tres lados no pueden ser iguales")  
            print("ingrese nuevamente los valores")
            
            lado=float(input("ingrese la longitud del lado 1: "))
            lado3=float(input("ingrese la longitud del lado 3: "))
    
    
    else:
         print("lo ingresado esta mal, es un triangulo Escaleno, sus tres lados no pueden ser iguales")  
         print("ingrese nuevamente los valores")
        
         lado=float(input("ingrese la longitud del lado 1: "))
         lado2=float(input("ingrese la longitud del lado 2: "))

    


'''
while contador<4:
    print("Ingrese la longitud del lado ",contador)

    lado=float(input("longitud: "))

    perimetro+=lado

    contador+=1


print("El perimetro del triangulo ",opcion, "es: ",perimetro,"cm")

'''