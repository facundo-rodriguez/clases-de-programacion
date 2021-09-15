#Se desea redondear un entero positivo N a la centena mas próxima y 
#visualizar la salida. Para ello la entrada de datos debe ser los cuatro dígitos
# A, B, C, D del entero N.
#Por ejemplo: Si A es 2, B=3, C=6 y D=2,
#entonces N es igual a 2362 y el resultado redondeado será 2400. 
#Si N es 2342, el resultado será 2300, y si N = 2962, 
#entonces el número será 3000. Diseñar el programa correspondiente.

#si c es mayor a 5 lo resto por 100 y despues a ese resultado lo sumo al numero ingresado.


#FORMA DEL PROFE

while a>0 or a>9:

    #while True:
    #   a=int(input("ingrese los miles: "))
    #   if a>=0 and a<=9:
    #       break
    
    a=int(input("ingrese los miles: "))
    b=int(input("ingrese los centenas: "))
    c=int(input("ingrese los decenas: "))
    d=int(input("ingrese los unidades: "))



    if(c>=5):
        b+=1
        c=0
        d=0

    #   if b==10:
    #      b=0
    #     a+=1   
    #de esta forma voy a tener que imprimir los cuatro numeros por separados

    #1715
    else:
        c=0
        d=0
    #1700

n=(a*1000) + (b*100) + (c*10) + d

print("el resultado redondeado es: ",n)



#ESTA ES MI FORMA :D

decimales=(c*10)+d

if decimales>=50:
    faltante=100-decimales
    n=n+faltante
else:
    n=n-decimales

print("el resultado es: ",n)