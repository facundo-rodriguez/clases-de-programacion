saldo=0
operacion=9
valor=0
#operacion=int(input("ingrese operacion 1-acreditar 2-debitar o salir"))
 
while True:
 
    operacion=int(input("ingrese operacion: "))
 
    if(operacion==2):
        valor=float(input("ingrese valor: "))
 
        if(valor>saldo):
            print("saldo insuficiente")
 
        else:
            saldo=saldo-valor
 
    else:
        if(operacion==1):
            valor=float(input("ingrese valor: "))
            saldo=saldo+valor
        else:
            if(operacion==0):
                break
            else:
               print("operacion invalida")
 
 
print("saldo: ",saldo)
