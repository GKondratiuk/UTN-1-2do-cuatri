#EJERCICIO 05 FACTORIAL DE UN NUMERO POSITIVO
#HACER UN PROGRAMA PARA CALCULAR EL FACTORIAL DE UN NUMERO POSITIVO

numero = int(input("Digite un numero: "))
while numero < 0:
    print("Error -> El numero tiene que ser postivo")
    numero = int(input("Digite un numero: "))
factorial = 1
for i in range(1,numero+1):
    factorial *= i
print(f' El facotorial del numero {numero} positivo ingresado es: {factorial}')