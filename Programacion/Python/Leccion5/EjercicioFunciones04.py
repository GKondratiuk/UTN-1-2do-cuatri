#EJERCICIO 04: CALCULADORA DE IMPUESTOS
#CREAWR UNA FUNCION PARA CALCULAR EL TOTAL DE UN PAGO INCLUYENDO
#UN IMPUESTO APLICADO. (IVA)
#FORMULA: pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
#proporciones el pago sin impuesto = 1000
#proporcion el monto del impuesto: 21%
#pago con impuesto: xxxxx

#creamos la funcion que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

#ejecutamos la funcion 
pago_sin_impuesto = float(input("Digite el pago sin impuestos: "))
impuesto = float(input("Digite el monto del impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto,impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')