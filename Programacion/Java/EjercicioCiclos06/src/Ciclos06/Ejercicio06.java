//PEDIR UN NUMERO HASTA QUE SE TECLEE UN 0, MOSTRAR LA SUMA DE TODOS LOS NUMEROS INTRODUCIDOS
package Ciclos06;

import java.util.Scanner;

public class Ejercicio06 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        }while(numero != 0);
        System.out.println("La suma de todos los numeros introducidos es: " + suma);
    }

}
