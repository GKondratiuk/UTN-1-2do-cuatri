#EJERCICIO 2: MODIFICAR LOS ELEMENTOS DE UNA LISTA
#LLENAR UNA LISTA CON LOS NUMEROS DEL 1 AL 10, LUEGO MODIFICAR LOS 
#ELEMENTOS DE LA LISTA MULTIPLICANDOLOS POR UN VALOR INGRESADO POR EL USUARIO

lista = list(range(1,11))
print('Lista original')
for i in lista:
    print(i,end='-')
valor = int(input('\nDigite un valor a multiplicar: '))

#Multiplicamos tods los valores de la lista

for indice, i in enumerate(lista): #Funcion para modificar los indices de la lista
    lista[indice] *= valor #en esta linea multiplicamos los valores

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i,end='-')