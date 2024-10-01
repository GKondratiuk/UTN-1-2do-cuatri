#EJERCICIO 03: FUNCION RECURSIVA
#IMPRIMIR NUMEROS DE 5 A 1 DE MANERA DESCENDENTE USANDO FUNCIONES RECURSIVAS
#PUEDE SER CUALQUIER VALOR POSITIVO, POR EJEMPLO, SI PASAMOS EL
#VALOR DE 5, DEBE IMPRIMIR:
#5
#4
#3
#2
#1
#En caso de ser el numero 3 debe imprimir:
#3
#2
#1
#SI SE INGRESAN NUMERO NEGATIVOS NO IMPRIME NADA

def imprimir_numeros_recursivos(numero):
    if numero >= 1: 
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')
        
imprimir_numeros_recursivos(int(input("Digite un numero entero"))) #Tarea, que el numero lo ingrese el usuario