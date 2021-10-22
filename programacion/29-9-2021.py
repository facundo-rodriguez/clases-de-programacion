saldo = 0
operacion = 9
valor = 0

if operacion == 0:
    print("El saldo es: ",saldo)
else:
    int(input("Ingrese una operación: "))
    if operacion == 2:
        int(input("Ingrese un valor: "))
        if valor > saldo:
            print("Fondos insuficientes")
            print("Operación invalida")
        else:
            saldo = saldo - valor
            print("Operación invalida")
    else:
        if operacion == 1:
            int(input("Ingrese un valor: "))
            saldo = saldo + valor
            print("Operación invalida")
        else:
            if operacion == 0:
                print("El saldo es",saldo)
            else:
                    print("Operación invalida")        