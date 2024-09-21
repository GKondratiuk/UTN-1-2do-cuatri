#EJERCICIO 9: MOSTRAR UNA FRASE SIN ESPACION Y CONTAR LA LONGITUD
# HACER UN PROGRAMA DONDE EL USUARIO INGRESE UNA FRASE, SE LE
#DEVOLVERÁ LA MISMA FRASE PERO SIN ESPACIOS EN BLANCO Y 
#ADEMAS UN CONTADOR DE CUANTOS CARACTERES TIENE LA FRASE 
#(SIN CONTAR LOS ESPACIOS EN BLANCO)
#EJEMPLO:       frase = vivir por siempre en paz
#               frase final = vivirporsiempreenpaz
#               nº de caracteres = 20

frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2 
print(f"Frase final: {frase1}")
print(f"Nº de caracteres: {len(frase1)}")
 