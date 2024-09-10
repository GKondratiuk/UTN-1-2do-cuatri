
package Ciclos04;

import java.util.Scanner;

/*EJERCICIO 4: PEDIR NUMEROS HASTA QUE SE TECLEE UNO NEGATIVO, Y MOSTRAR CUANTOS NUMEROS SE HAN INTRODUCIDO. 
LO HACEMOS PRIMERO EN LA CLASE SCANNER Y LUEGO CON LA CLASE JOPTION PANE*/
public class Ejercicio04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int contador = 0;
        
        System.out.println("Ingrese un numero");
        var numero = Integer.parseInt(entrada.nextLine());
        
        while(numero > -1){
            System.out.println("Se registró el numero " + numero);
            System.out.println("Ingrese otro numero");
            numero = Integer.parseInt(entrada.nextLine());
            contador = contador + 1;
        }
        System.out.println("Se ingresaron un total de " + contador + " Numeros sin contar el negativo");
    }
}
