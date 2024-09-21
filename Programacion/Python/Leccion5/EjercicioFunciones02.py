#Ejercicio02: FUNCION CON * ARGS PARA MULTIPLICAR
#CREAR UNA FUNCION PARA MULTIPLICAR LOS VALORES RECIBIDOS
# DE TIPO NUMERICO, UTILIZANDO ARGUMENTOS VARIABLES *ARGS 
#COMO PARAMETRO DE LA FUNCION Y REGRESAR COMO RESULTADO
#LA MULTIPLICACION DE TODOS LOS VALORES PASADOS COMO ARGUMENTOS 

#Definimos la funcion para multiplicar 
def multiplicar_valores(*numeros): #el mas utiliado es *args como argumento
    resultado = 1 # por 0 no se puede multiplicar nada 
    for numero in numeros:
        resultado *= numero
    return resultado

#llamamos a la funcion
print(multiplicar_valores(3,5,15)) #le pasamos los argumentos