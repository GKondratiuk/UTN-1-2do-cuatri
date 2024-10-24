class MiClase: # creamos la clase
#creamos variable de clase, dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): # metodo dunder init para instanciar la variable
    #creamos la variable instancia, dara diferentes valores
        self.variable_instancia = variable_instancia

    
#METODOS ESTATICOS: Los metodos estaticos se asocian a la clase y no al objeto
#para utilizarlos se llama a la clase y luego al metodo estatico
#el metodo estatico no puede acceder al dinamico ni a los atributos
    @staticmethod
    def metodo_estatico():#metodo estatico
        print(MiClase.variable_clase)

#METODO DE CLASE
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

print(MiClase.variable_clase)

#creamos un objeto y le pasamos un un argumento
miClase1 = MiClase('esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

#creamos otro objeto
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

#Creamos una segunda variable de clase - no es una forma tan comun de programar
MiClase.variable_clase2 = 'Valor de variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

#Llamamos al metodo estatico
MiClase.metodo_estatico()

MiClase.metodo_clase()

miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()