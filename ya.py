frase1="KLASSLÑERLKGLKBLKTÑIJKM"
frase2="KLASSLÑESLKGLKBLKTÑIIKM"

frase3="IJTIJTIWEJTIWEJTIWETJIWJE"
frase4="IJTIJTIWEJTIWEJTIWETJJWJET"

frase5="ZKSJSJSEEKMRJRIJERLEPRLSJ"
frase6="ZKSJSJSEEKMRJRIJERLEPRLSJ"

frase7="OREOITKOEKFKOKDFIRMGOT"
frase8="OREOITIKOEKFKOKDFIRNGOT"


longitu_frase3=len(frase3)
longitu_frase4=len(frase4)

if(longitu_frase3==longitu_frase4):
    print("tienen la misma cantidad de letras")
else:
    print(longitu_frase3)
    print(longitu_frase4)

if(frase1==frase2):
    print("es la opcion 1")

elif(frase3==frase4):
    print("es la opcion 2")

elif(frase5==frase6):
    print("es la opcion 3")

elif(frase7==frase8):
    print("es la opcion 4")


cuenta1=14 / ( 3 + 4 ) + 9 - 10 / 2

print("La cuenta es: ",cuenta1)


resto1=21%7
resto2=21%3

resto3=777%7
resto4=777%3

resto5=651%7
resto6=651%3

resto7=100%7
resto8=100%3

resto9=980%7
resto10=980%3

if((resto1==0) and (resto2==0)):
    print("NO es la opcion 1")

    print("el resto1 es: ",resto1)
    print("el resto2 es: ", resto2)

if((resto3==0) and (resto4==0)):
    print("NO es la opcion 2")

    print("el resto3 es: ",resto3)
    print("el resto4 es: ", resto4)

if((resto5==0) and (resto6==0)):
    print("NO es la opcion 3")

    print("el resto5 es: ",resto5)
    print("el resto6 es: ", resto6)

if((resto7==0) and (resto8==0)):
    print("NO es la opcion 4")

    print("el resto7 es: ",resto7)
    print("el resto8 es: ", resto8)
else:
    print("el resto7 es: ",resto7)
    print("el resto8 es: ", resto8)


if((resto9==0) and (resto10==0)):
    print("NO es la opcion 5")

    print("el resto9 es: ",resto9)
    print("el resto10 es: ", resto10)
else:
    print("el resto9 es: ",resto9)
    print("el resto10 es: ", resto10)


array=[]

while True:

    i=int(input("ingrese los numeros: "))

    if( (i >= 3)  and  (i <=7) ):

        print("el valor", i ,"es correcto")

        array.append(i)
    
    else:
        print("el valor es incorrecto")
        print("los numeros correctos son: ", array)
        break
