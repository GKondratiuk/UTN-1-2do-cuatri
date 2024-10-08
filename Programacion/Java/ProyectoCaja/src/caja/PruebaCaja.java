/*
Proyecto Caja: 
Ejercicio1: Crear un proyecto segun las espeficicaciones 
mostrada a continuacion. 
la formula es: volumen = ancho * alto * profundidad
*/
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        //Variables locales
        int medidaAncho = 3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();//Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho;//le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //llamamos al metodo
        //primer resultado
        System.out.println("Resulado volumen de caja 1: " + resultado);
        
         Caja caja2 = new Caja(2,4,6); //llamamos al constructor 2 con nuevos argumentos
        //llamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("Resultado volumen Caja 2: " + caja2.calcularVolumen());
          
    }

}
