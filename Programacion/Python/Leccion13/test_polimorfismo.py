from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto) #De manera indirecta llama al str de la clase empleado o gerente
    print(type(objeto)) #para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if(isinstance(objeto,Gerente)): #imprime el departamento si la clase es gerente
        print(objeto.departamento)

empleado = Empleado('Ariel',50000)
imprimir_detalles(empleado)

gerente = Gerente('Natalia',60000,'Sistemas')
imprimir_detalles(gerente)

#EL POLIMORFISMO se trata de multiples formas en tiempo de ejecucion