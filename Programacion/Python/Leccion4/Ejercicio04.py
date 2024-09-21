#EJERCICIO 04: SUMAR NUMEROS PARES DENTRO DE UN RANGO
#HACER UN PROGRAMA PARA SUMAR NUMERO PARES DENTRO
#DE UN RANGO, POR EJEMPLO: 
#               SUMA DE NUMEROS PARES DEL 2 AL 30
#               SUMA = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Hasta donde quiere llegar a sumar: "))
suma = 0

for i in range(a,b+1):
    if i%2==0:
        suma +=i
print(f'\nLa suma de numero pares dentro de l rango es: {suma}')