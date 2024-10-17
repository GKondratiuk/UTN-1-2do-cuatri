class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

        #METODO GET
    @property
    def nombre(self):
        return self._nombre
        #METODO SET
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def __str__(self): #Override = Sobreescribir
        return f'Persona: [Nombre: {self._nombre}, Edad: {self._edad}]' 
    

class Empleado(Persona): #empleado es hija de la clase persona
    # hay que colocar los atributos de la clase padre tambien en la clase hija
    def __init__(self, nombre, edad, sueldo):
        # hay que agregar estas propiedades de la clase padre
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Sueldo: {self._sueldo} {super().__str__()}]'

empleado1 = Empleado('Ariel', 40, 75000) # creamos un nuevo objeto
print(empleado1) #nos muestra el numero en memoria
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#Tarea: Encapsular los atributos y agregar los metodos getters n setters
# Crear otro objeto, pasar los dastos para nombre, edad y sueldo
#Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Liliana',38,70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = 'Natalia'
empleado2.edad = 35
empleado2.sueldo = 75000

print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
