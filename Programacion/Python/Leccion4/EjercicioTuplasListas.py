import math #Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

#Dada la siguiente tupla
tupla = (13,1,8,3,2,5,8) #Definimos la tupla
#Crear una lista que solo incluya los números menores a 5 e imprima por consola [1,2,3]

lista = [] # Definimos la lista
#Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#EJERCICIO DE MATEMATICAS
#Para sacar la raiz cuadrade de un numero positivo
numero = int(input("Digite un numero positivo"))
while numero < 0:
    print('Error  -> deberia ser un numero postivo ')
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")#2f solo para que nos muestre solo 2 numeros