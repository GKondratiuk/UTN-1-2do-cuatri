#EJERCICIO 8: MENÚ INTERACTIVO - CAJERO AUTOMATICO 
#HACER UN PROGRAMA QUE SIMULE UN CAJERO AUTOMATICO CON UN SALDO 
#INICIAL DE $1000 Y TENDRÁ EL SIGUIENTE MENÚ DE OPCIONES:
#       1.INGRESAR DINERO
#       2.RETIRAR DINERO
#       3.MOSTRAR DINERO DISPONIBLE
#       4.SALIR

saldo = 1000
while True:
    print(".:MENU:.")
    print("1. INGRESAR DINERO")
    print("2. RETIRAR DINERO")
    print("3. MOSTRAR DINERO DISPONIBLE")
    print("4. SALIR")
    opcion = int(input("Digite una opcion"))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar ?"))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar ?"))
        if retirar > saldo:
            print("No tiene saldo suficiente")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar el cajero automatico, hasta pronto")
        break
    else:
        print("Error, se equivocó de opcion de menú")
        print()
        
