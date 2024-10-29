from Empleado import Empleado 

class Gerente(Empleado):
    def __init__(self,nombre,sueldo,departamento):
        super().__init__(nombre,sueldo)#llamamos al metodo init de la clase empleado para que gerente herede sus atributos
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'
