#EJERCICIO 7: JUEGO ADIVINA EL NUMERO
#REALIZAR UN JUEGO PARA ADIVINAR UN NUMERO. PARA ELLO SE DEBE
#GENERAR UN NUMERO ALEATORIO ENTRE 1 - 100 Y LUEGO IR PIDIENDO
#NUMEROS INDICANDO "ES MAYOR" O "ES MENOR" SEGUN SEA MAYOR O MENOR 
#CON RESPECTO A N. EL PROCESO TERMINA CUANDO EL USUARIO ACIERTA 
# Y ALLÍ SE DEBE MOSTRAR EL NUMERO DE INTENTOS 

import random #esto es para poder colocar un numero aleatorio
print("\t.:JUEGO ADIVINA EL NUMERO:.")
aleatorio = random.randint(0,100) #toma de 0 a 100 para darnos un numero aleatorio
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("No es el numero, digite un numero MENOR")
    elif numero < aleatorio:
        print("No es el numero, digite un numero MAYOR")
    else:
        print(f'FELICITACIONES, acabas de adivinar el numero {aleatorio}')
        break
print(f"Numero de intentos: {contador}")
