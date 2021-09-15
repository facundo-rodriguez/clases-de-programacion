#FUNCIONES

#conjunto de codigo agupado.
#las funciones pueden o no devolver valores
#pueden o no tener paramatros
#funciones y metodos son sinonimos
#python solo funciones por referencia


def lineas():
    print("------------------------------------------")

def mensaje():
    
    lineas()#llamo una funcion dentro de otra funcion
    print("Sistema de calculo de votos")
    print("En este sistema podra ingresar los votantes")
    print("Ademas, podra calcular la cantidad de votantes")
    lineas()

mensaje()

a=input("Ingrese nombre:")

mensaje()

#-------------

for i in range(5):
    mensaje()     #llama a la funcion 5 veces



def suma(num1,num2):
    resultado=num1+num2

    if resultado>50:
        print("El resultado es mayor a 50")
    else:
        print("El resultado es menor que 50")

suma(20,25)


#Con retorno
def suma(num1,num2):
    resultado=num1+num2

    if resultado>50:
        print("El resultado es mayor a 50")
    else:
        print("El resultado es menor que 50")
    
    return resultado

#Cuando uso return tengo que llamar la funcion dentro de una variable
#para que se guarde el valor que devuelve el return

a=suma(20,25)
print("El resultado es:",a)

a=suma(50,25)
print("El resultado es:",a)

a=suma(10,25)
print("El resultado es:",a)
