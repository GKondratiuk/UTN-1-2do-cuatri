#EJERCICIO05: CONVERTIDOR DE TEMPERATURAS
#REALIZAR DOS FUNCIONES PARA CONVERIT DE GRADOS A CELSIUS
#A FAHRENHEIT Y VICEVERSA
#INVESTIGAR LAS FORMULAS

#FUNCION QUE CONVIERTE DE CELSIUS A FARENHEIT

def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit -32) * 5 / 9

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F --> {resultado:.2f}')

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C --> {resultado:.2f}')