class Producto{
    static contadorProductos = 0;
    constructor(nombre,precio){
        this._idProducto = ++ Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto(){
        return this._idProducto;
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }

    get precio(){
        return this._precio;
    }
    set precio(precio){
        this._precio = precio
    }

    toString(){//template literals
        return`idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`
    }
} //fin de la clase Producto

let producto1 = new Producto('Pantalon',200)
let producto2 = new Producto('Camisa', 150)
console.log(producto1.toString());
console.log(producto2.toString());

//falta clase 3

class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = []; //esto es un array
        this._contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    } 

    agregarProductos(Producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(Producto) //este es un tipo de sinstaxis
            //this._productos[this._contadorProductosAgregados++] = producto; //segunda sintaxis
        }
        else{
            console.log("No se pueden agregar mas productos")
        }
    }//fin del metodo agregar producto

    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        }//fin ciclo for
        return totalVenta;
    }//fin del metodo calcularTotal

    mostrarOrden(){
        let productoOrden = ' ';
        for(let producto of this._productos){
            productoOrden += producto.toString()+' ';
        }//Fin del ciclo for
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productoOrden}`)
    }//fin metodo mostrar orden 
}//fin de la clase orden

//falta video 6 de la clase 10



