
print("empieza otra vez")

#ingreso la palabra
#la letra a esta en la palabra?
#cuantas veces esta la letra en la palabra?
#imprima la cantidad de veces

palabra=input("ingrese una palabra")
letra=input("ingrese una letra")

cantidad=0

for i in (palabra):

    if (i==letra):

        cantidad+=1
       

print("la letra aparece ", cantidad, " veces") 

encontrado = False
for i in range(1, 6):
    print(i)
    if i % 2 == 0:
        encontrado = True
if encontrado:
    print(f"Entre 1 y 5 hay al menos un múltiplo de 2.")
else:
    print(f"Entre 1 y 5 no hay ningún múltiplo de 2.")



#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).

#entrada: si o no
#proceso: que se repita la pregunta y se evalue la respuesta
#salida:que se se repita el proceso o imprime un mensaje hasta la vista


print("empieza otra vez")

#de esta forma cada que toco enter el programa sigue funcionando
'''
print("¿desea continuar con el programa?")
print("esta por entrar al while")

bandera=True

 
while(bandera):

    respuesta=input("si o no?")
    print("¿desea continuar con el programa?")
    

    if(respuesta=="no"):   #if(respuesta=="no"):
                                    #break
        bandera=False


print("hasta luego!")

  

'''
#de esta forma al hacer enter me lo toma como un no y sale del while
'''

respuesta=input("¿desea continuar con el programa? ¿si o no?")

while(respuesta=="si"):
  
   respuesta=input("¿desea continuar con el programa? ¿si o no?")

print("hasta luego!")
  '''

  