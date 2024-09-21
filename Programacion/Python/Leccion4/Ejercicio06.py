#EJERCICIO 6: TABLA DE MULTIPLICAR
# HACER UN PROGRAMA QUE PIDA UN NUMERO POR TECLADO Y GUARDE 
#EN UNA LISTA SU TABLA DE MULTIPLICAR HASTA EL 10. POR EJEMPLO:
#SI DIGITA EL 5 LA LISTA TENDRÁ: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Digite un numero: "))
lista = [] # creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
    print(f'Tabla de multiplicar del {numero}: \n {lista} ')

for indice,i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}') #formato tabla de multiplicar