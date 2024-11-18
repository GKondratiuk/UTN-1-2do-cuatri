
package ar.com.codesystem.ventas;


public class Orden {
    //Atributos de clase
    private int idOrden;
    private Producto[] productos; //Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10; //es una constante, las constante van en mayusculas, las constante nunca se modifican
    
    //constructo vacio
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    //Metodos - relacionamos la clase Orden, con la clase Producto
    public void agregarProducto(Producto producto){
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){
            //sumamos un nuevo producto al contador de producto y agregamos el producto al array
            this.productos[this.contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ah superado el maximo de productos: " + Orden.MAX_PRODUCTOS);
        }
    }
}

//hicimos hasta la clase 12 ejercicio 4