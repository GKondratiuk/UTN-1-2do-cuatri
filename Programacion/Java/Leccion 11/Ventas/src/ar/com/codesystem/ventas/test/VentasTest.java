package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500);
        Producto producto2 = new Producto("Campera", 29900);
        Producto producto3 = new Producto("Remera", 10500);
        Producto producto4 = new Producto("Short", 5500);
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        System.out.println("---------------------------------------");
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.mostrarOrden();
        
        //Tarea:
        //Crear mas objetos del tipo Producto
        //crear mas objetos del tipo Orden
    }

}
