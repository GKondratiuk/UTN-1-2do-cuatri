'''
definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y
Bicicleta, ambas heredan de la clase padre Vehiculo. La clase padre
debe tener los siguientes atributos y metodos:

Vehiculo (clase padre)
-Atributos(color,ruedas)
-Metodos(__init__(color,ruedas) y __str__())

Auto(clase hija de Vehiculo)
-Atributos(velocidad(km/hr))
-Metodos(__init__(color,ruedas,velocidad) y __str__())

Bicicleta(clase hija de Vehiculo)
-Atributos(tipo(urbana/montania/etc))
-metodos:(__init__(color,ruedas,tipo) y __str__())

Crear un objeto de cada clase
'''
class Vehiculo:

    def __init__(self,color,ruedas): #metodo dunder init
        self.color = color
        self.ruedas = ruedas

    def __str__(self): #metodo dunder str
        return 'Color: ' + self.color + ' Ruedas: ' + str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ', Tipo ' + (self.tipo)

#Primer objeto de la clase padre vehiculo
vehiculo = Vehiculo('Blanco',4)
print(vehiculo)

    #Segundo objeto pero de la clase auto 
auto = Auto('Amarillo',4, 120)
print(auto)

bicicleta = Bicicleta('Azul', 2, 'Urbana')
print(bicicleta)