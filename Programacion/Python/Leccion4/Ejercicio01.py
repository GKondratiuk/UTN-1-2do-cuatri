#EJERCICIO01: LLENAR UNA LISTA
#LLENAR UNA LISTA CON LOS NUMEROS DEL 1 AL 50, LUEGO MUESTRA
#LA LISTA CON EL BUCLE FOR, LOS ELEMENTOS DEBEN MOSTRARSE 
#DE LA SIGUIENTE FORMA: 
#1-2-3-4-5...-50
'''
lista = []
i = 1 

while i < 51:
    lista.append(i)
    i += 1
'''
lista = list(range(1,51))#Algoritmo mas eficaz
for i in lista: 
    print(i, end='-')