# 4.- Secuencia de Fibonacci
# En matemática, la sucesión de Fibonacci es la siguiente sucesión infinita de números naturales:

# 0,1,1,2,3,5,8,13,21,34,55,89,144

# La sucesión inicia con 0 y 1, y a partir de ahí cada elemento es la suma de los dos anteriores.
# A cada elemento de esta sucesión se le llama número de Fibonacci.
# Pedir al usuario que ingrese la cantidad de números de Fibonacci desea ver y mostrarlos por pantalla.

# Restricción: El usuario no puede ingresar un número menor a 3.

print("Ingrese la cantidad de números de Fibonacci que desea ver. La cantidad a pedir tiene que ser mayor a 3")

numero=int(input("ingrese un numero entero: "))


while(numero<3):
    
    print("El numero ingresado no es mayor a 3, ingreselo nuevamente")
    
    numero=int(input("ingrese un numero entero: "))


a=0
b=1
fib=[0,1]

for i in range(numero):
    
    c=a+b

    a=b
    b=c 
    
    fib.append(c)   

    

fib_str=str(fib)[1:-1]
print(f"los numeros pedidos son: {fib_str}")


    


