class Persona2:
    def __init__(self, nombre,apellido,edad):
        #el _ nos indica que esto va a estar encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property #decorador, es necesario para el getter
    def nombre(self): #metodo Getter
        print('Estamos utilizando el metodo get')
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self,nombre):
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido
    
    @edad.setter
    def edad(self,edad):
        self._edad = edad

    #funcion para borrar y liberar recursos - metodo destructor 
    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__': # con este if, si ejecutamos esta clase desde otro archivo no se va a visualizar

    persona1 = Persona2('Ariel','Betancud',41)
    # print(persona1._nombre) - esto no se debe hacer, no es una manera correcta
    print(persona1.nombre) #llamamos al metodo GET - esta es la manera correcta de llamar

    persona1.nombre ='Juan Pedro' #llamamos al metodo SET
    print(persona1.nombre) #otra vez el metodo GET
    print(persona1.mostrar_detalle()) # llamamos al metodo mostrar detalle

    #atributo read-only seria la edad porque no tiene el metodo set, no se puede modificiar
    persona1.edad = 40
    print(persona1.edad)

    #TAREA: CREAR TRES OBJETOS MAS UTILIZANDO LOS METODOS GETTER AND SETTER
    #PARA MOSTRAR Y MODIFICAR LOS CAMBIOS CON EL METODO MOSTRAR DETALLE

    persona2 = Persona2('Guillermo','Kondratiuk',32)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Guille'
    persona2.apellido = 'Kotiuk'
    persona2.edad = 33
    print(persona2.mostrar_detalle())

    persona3 = Persona2('Franciso','Valdez',34)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Fran'
    persona3.apellido = 'Val'
    persona3.edad = 35
    print(persona3.mostrar_detalle())

    persona4 = Persona2('Jorge','Martinez',25)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'George'
    persona4.apellido = 'Mar'
    persona4.edad = 26
    print(persona4.mostrar_detalle())

    print(__name__) #nos dice donde se está ejecutando el codigo 