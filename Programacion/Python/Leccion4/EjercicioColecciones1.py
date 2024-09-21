#EJERCICIO 1: Eliminar duplicados en una lista
#Escriba un programa donde tenga una lista y que a continuacion
# Elimine los elementos repetidos, por ultimo mostrar la lista

#Creamos una Lista - CORCHETES.
lista = [1,2,3,"Ariel",7,7,3,"Alberto",5,"Ariel",1,2,3]

#Set o conjuntos no admite repetidos o duplicados
#conjunto = set(lista) # convertimos la lista a un conjunto
#print(conjunto)

#convertimos el set o conjunto a una lista
#lista = list(conjunto)

lista = list(set(lista)) #convertimos la lista en un conjunto y el conjunto en una lista
print(lista)

