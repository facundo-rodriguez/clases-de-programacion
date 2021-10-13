#La secuencia de Collatz de un número entero se construye de la siguiente manera:
#Si el número es par, se lo divide por dos;
#Si es impar, sele multiplica tres y se le suma uno;
#La sucesión termina al llegar a uno.
#La conjetura de Collatz afirma que, al partir desde cualquier número, la secuencia siempre llegará a 1. A pesar de ser una afirmación a simple vista muy simple, no se ha podido demostrar si es cierta o no.
#Desarrollar un programa que entregue la secuencia de Collatz a partir de un número entero.

#n=18
#18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

num=int(input("ingrese un numero entero: "))

array=[]

while True:
    
    array.append(num) 
    #print(num)

    if(num==1):
        break
    
    else:
        if(num%2==0):
            #print("es par")
            num/=2
            #print(num)

        else:
        #print("es impar")
            num*=3
            num+=1
        
    
    



for i in range(len(array)):

    print(array[i],"",end="")