#EJERCICIO 10: NO REPETIR CARACTERES
#HACER UN PROGRAMA QUE PIDA UNA CADENA POR TECLADO, 
#LUEGO METER LOS CARACTERES EN UNA LISTA SIN REPETIR CARACTERES 

cadena = input("Digite una cadena: ")
lista =[]
for i in cadena: 
    if i not in lista: #si el caracter aun no está en la lista 
        lista.append(i)# lo agregamos a la lista
print(f'lista de caracteres sin repetir ninguno: \n {lista}')