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


class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){ //SIMULA UNA CONSTANTE
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
            productoOrden += '\n{' + producto.toString()+'} ';
        }//Fin del ciclo for
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productoOrden}`)
    }//fin metodo mostrar orden 
}//fin de la clase orden

let producto1 = new Producto('Pantalon',200);
let producto2 = new Producto('Camisa', 150);
let producto3 = new Producto('Cinturon',50);
let Orden1 = new Orden();
let Orden2 = new Orden();
Orden1.agregarProductos(producto1);
Orden1.agregarProductos(producto2);
Orden1.agregarProductos(producto3);
Orden2.agregarProductos(producto1);
Orden2.agregarProductos(producto2);
Orden2.agregarProductos(producto3);
Orden1.mostrarOrden();
Orden2.mostrarOrden();
