/*EJERCICIO 08: PEDIR UN NUMERO N Y MOSTRAR TODOS LOS NUMEROS DEL 1 AL N */

package Ciclos08;

import java.util.Scanner;

public class Ejercicio08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1; 
        
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
