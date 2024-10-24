class Persona:
    #Variable de clase
    contador_personas = 0

    #metodo de clase
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre,edad):
        #al colocar el metodo de clase, la linea de abajo ya no va
        # Persona.contador_personas += 1 #incrementa por cada objeto
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
        #metodo dunder str crea una cadena de objetos
    def __str__(self):
        return f'Persona [{self.id_persona} = {self.nombre} {self.edad}]'
    
persona1 = Persona('Ariel',40)
print(persona1)

persona2 = Persona('Osvaldo',45)
print(persona2)

persona3 = Persona('Liliana', 35)
print(persona3)

Persona.generar_siguiente_valor() # id n 4
persona4 = Persona('Natalia', 35)
print(persona4)

print(f'Valor contador Personas: {Persona.contador_personas}')

#Falta video 8 clase 10 pt 2