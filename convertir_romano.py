

numeros=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
letras=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

romano=''

while True:
    num=int(input("ingrese un numero entero mayor a 0: "))

    if(num>0):
        break
    else:
        print("el numero ingresado es incorrecto, hagalo nuevamente")



i=0
while num>0:

    if(num>=numeros[i]):

        romano+=letras[i]

        num-=numeros[i]
    
    else:
        i+=1


print(romano)
