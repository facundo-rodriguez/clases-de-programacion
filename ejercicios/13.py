#Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de refacciones.
#La empresa, dependiendo del monto total de la compra, decidirá que hacer para pagar al fabricante.
#Si el monto total de la compra excede de $500000 la empresa tendrá la capacidad de invertir de su propio dinero
#un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante. 
#Si el monto total de la compra no excede de $500000 la empresa tendrá capacidad de invertir de su propio dinero un 70% 
#y el restan 30% lo pagará solicitando un crédito al fabricante. 
#El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. 
#Mostrar por pantalla como queda la operación.

monto_total=float(input("ingrese el monto a pagar de la compra"))

while True:

    if(monto_total<0):
        print("lo ingresado esta mal, ingreselo nuevamente")
        monto_total=float(input("ingrese el monto a pagar de la compra"))
    
    else:
        break
    

prestamo_banco=0

if(monto_total>=500000):
   
    inversion_empresa=(55*monto_total)/100

    prestamo_banco=(30*monto_total)/100

    credito_fabricante=monto_total - inversion_empresa - prestamo_banco

else:

    inversion_empresa=(70*monto_total)/100

    credito_fabricante=monto_total - inversion_empresa - prestamo_banco


intereses_fabricante=(20*credito_fabricante)/100


print("La inversion de la empresa es: ",inversion_empresa)
print("El prestamo del banco es: ",prestamo_banco)
print("El credito del fabricante es: ", credito_fabricante)
