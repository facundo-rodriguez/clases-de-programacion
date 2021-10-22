#necesitamos mostrar un contador de 5 digitos(xxxxx), 
# que muestre los numeros de 0 0 0 0 0 al 9 9 9 9 9 con 
#la particularidad que cada vez que aparezca
#un 3 lo sustituya por una E

n=0

n1=0
n2=0
n3=0
n4=0
n5=0


array=[n1,n2,n3,n4,n5]

contador=1

for i in range(5):

    print("digito ",contador)
    
    if n==9:
        n=0

    for j in range(9):

        n+=1

        if(n==3):
            print([0,0,0,0,"E"])
        else:
            print([0,0,0,0,n])

    contador+=1

