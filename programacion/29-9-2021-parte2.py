saldo = 0
operacion = 9
valor = 0

while operacion != 0:
    operacion = int(input("Ingrese una operación (1.Deposito, 2.Retiro, 0.Salir): "))
    if operacion == 2:
        valor = float(input("Ingrese monto a retirar: "))
        if valor > saldo:
            print("Fondos insuficientes")
        else:
            saldo = saldo - valor
    else: 
     if operacion == 1:
        valor = float(input("Ingrese un monto a depositar: "))
        saldo = saldo + valor
    if operacion == 0:
        print("Su saldo es: ",saldo)
        print("")