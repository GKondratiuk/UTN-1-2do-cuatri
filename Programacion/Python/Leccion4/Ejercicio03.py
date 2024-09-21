#EJERCICIO 03: INSERTAR ELEMENTOS Y ORDENARLOS
#PEDIR NUMEROS Y METERLOS EN UNA LISTA, CUANDO EL USUARIO
#INTRODUZCA UN NUMERO 0, NUESTRO PROGRAMA DEJARÍA DE INSERTAR
#POR ULTIMO MOSTRAR LOS NUMEROS DE MENOR A MAYOR

lista = []
salir = False

while not salir:
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()#la lista está ordenada - ordena la lista
print(f'\nLista ordenada: \n{lista}')