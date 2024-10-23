class MiClase: # creamos la clase
#creamos variable de clase, dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): # metodo dunder init para instanciar la variable
    #creamos la variable instancia, dara diferentes valores
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)

#creamos un objeto y le pasamos un un argumento
miClase1 = MiClase('esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

#creamos otro objeto
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
