#Escribir un programa quedetermine si un año es bisiesto.
#Un añoes bisiesto si es múltiplo de 4 (por ejemplo, 1984).
#Sin embargo, los múltiplos de 100 sólo son bisiestos cuando a la vez son múltiples de 400 
#(por ejemplo, 1800 no es bisiesto, mientras que 2000 si lo es).

año=int(input("ingrese el año: "))

while año<0:
    print("el año ingresado esta mal, ingreselo nuevamente")
    año=int(input("ingrese el año: "))


if(año%100==0):
   
    if (año%400==0):
       print("el año es bisciesto xq es multiplo de 100 y 400")
    
    else:
        print("el año no es bisciesto")

else:
    if año%4==0:
        print("el año es bisciesto")  

    else:
        print("el año no es bisciesto")

