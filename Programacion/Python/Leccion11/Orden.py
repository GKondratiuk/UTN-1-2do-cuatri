from Producto import Producto
class Orden:
    contador_ordenes = 0 # variable de clase

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos) #creamos una lista que recibirá un procuto
    
    def agregar_producto(self,producto): #creamos una funcion
        self._productos.append(producto) #la funcion agrega un producto a la lista

    def calcular_total(self):
        total = 0 #variable temporal para almacenar el total temporal
        for producto in self._productos: # recurre todos los productos de la lista self._productos
            total += producto.precio # suma todos los precios de la lista
        return total #devuelve el total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+'|'
        return f'Orden: {self.id_orden}, \n Producto: {productos_str}'
    
if __name__ == '__main__':
    producto1 = Producto('Camiseta',100.00)
    producto2 = Producto('Pantalon',150.00)
    productos1 = [producto1, producto2] #lista de productos
    orden1 = Orden(productos1) #primer objeto orden pasando la lista de productos
    print(orden1)