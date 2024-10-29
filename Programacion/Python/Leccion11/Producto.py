class Producto:
    contador_productos = 0 #variable de clase
    
    #metodo inicializador dunder init con parametros
    def __init__(self, nombre,precio):
        Producto.contador_productos += 1 #el contador se irá incrementando por cada producto
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    #agregamos getters and setters

    @property #decorador para el get
    def nombre(self):
        return self._nombre
    
    @nombre.setter #decorador para el set
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,precio):
        self._precio = precio

    #metodo str genera una cadena 

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio {self._precio}'


if __name__ == '__main__': #solo sera visible la prueba desde aqui
    producto1 = Producto('Camiseta',100.00)
    print(producto1)
    producto2 = Producto('Pantalon',150.00)
    print(producto2)