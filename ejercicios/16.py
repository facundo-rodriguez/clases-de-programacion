#Un joven periodista debe relatar un partido de tenis, pero no conoce las reglas del deporte. 
#En particular, no ha logrado aprender como saber si un set ya terminó y quien lo ganó.
#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, 
#además debe haber ganado por lo menos dos juegos mas que su rival. 
#Si el set esta empatado a 5 juegos, el ganador es el que llegue a 7. 
#Si el set está empatado a 6 juegos, el set se define en el último juego, 
#en cuyo caso el resultado final es 7-6.
#Sabiendo que el jugador A ha ganado X juegos y el jugador B, Z juegos, 
#el periodista desea saber.
# Si A ganó el set, o
# Si B ganó el set, o
# Si el set todavía no termina, o
# Si el resultado es inválido (por ejemplo 8-6 o 7-3)




a=int(input("ingrese la cantidad de games del jugador A: "))
b=int(input("ingrese la cantidad de games del jugador B: "))


#ambas variables deben ser menores que 6, 
#ademas si alguna variable(a,b) es igual a 6 la otra variable debe ser 5.

#si a o b son mayor a 7, el resultado es invalido.

bandera=False

if((a>7)or(b>7)):
    print("el resultado es invalido")

elif( (a==7) and (b<5) ):
    print("el resultado es invalido")

elif((b==7) and (a<5)):
    print("el resultado es invalido")

elif( (a==7) and (b==7)):
    print("el resultado es invalido")

else:

    if(a<6) and (b<6):
        bandera=True

    elif(a==6) and (b==5):
        bandera=True

    elif(a==5) and (b==6):
        bandera=True

    elif(a==6) and (b==6):
        bandera=True

    else:

        if(a>b):
            print("el jugador A gano el set")
        else:
            print("el jugador B gano el set")


    if bandera==True:
        print("el partido todavia no termino")



#---------------------------------------------------------------------

print("-------------------------------------------")

a=int(input("ingrese la cantidad de juegos del jugador a: "))
b=int(input("ingrese la cantidad de juegos del jugador b: "))


resultado_invalido=True

#GANO EL JUGADOR A
if(a==6) and (b<=4):
    print("El ganador del set es el jugador A")
    resultado_invalido=False

else:
    if(a==7) and (b==5):
        print("El ganador del set es el jugador A")
        resultado_invalido=False

    else:


        #GANO EL JUGADOR B
        if(b==6) and (a<=4):
            print("El ganador del set es el jugador B")
            resultado_invalido=True
        else:
            if(b==7) and (a==5 or a==6):
                print("El ganador del set es el jugador B")
                resultado_invalido=False

            else:
#---------------------------------------------------------------------
#RESULTADO INVALDO
                
                if(a>=8) or (b>=8):
                    print("el resultado es invalido")

                else:
                        if (a==7) and((b<5) or (b==7)):
                            print("el resultado es invalido")
                        
                        else:
                            if(b==7) and ((a<5)or (a==7)):
                                print("el resultado es invalido")

                            else:
                                print("el est todavia no termina")
                #EL SET ESTA EN JUEGO

                if(a<=5) and (b<=5):
                    print("el set todavia no se termina")
                    resultado_invalido=False

                else:
                    if(a==6) and (b==5):
                        print("el set todavia no se termina")
                        resultado_invalido=False
                    
                    else:
                        if(a==5) and (b==6):
                            print("el set todavia no se termina")
                            resultado_invalido=False

                        else:
                            if(a==6) and (b==6):
                                print("el set todavia no se termina")
                                resultado_invalido=False

                            else:
                                resultado_invalido=True
                                print("El resultado ingresado no es valido")