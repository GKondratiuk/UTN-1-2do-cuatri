package Ciclos03;

import java.util.*;

/*EJERCICIO 3: LEER NÚMEROS HASTA QUE SE INTRODUZCA UN CERO PARA CADA UNO INDICAR SI ES PAR O IMPAR
PRIMERO LO HAREMOS CON LA CLASE SCANNER, LUEGO CON LA CLASE JOPTIONPANE*/
public class Ejercicio03 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduzca un número");
        int numero = entrada.nextInt();

        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El número " + numero + " es par");
                System.out.println("Introduzca otro número");
                numero = entrada.nextInt();
            } else {
                System.out.println("El numero " + numero + " es impar");
                System.out.println("Introduzca otro número");
                numero = entrada.nextInt();
            }
        }

    }

}
