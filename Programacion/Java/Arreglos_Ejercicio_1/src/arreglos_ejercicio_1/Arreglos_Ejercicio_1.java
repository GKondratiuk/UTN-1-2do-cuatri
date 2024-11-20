/*
Ejercicio 1: Leer 10 numeros enteros, guardarlos en un arreglo. 
Debemos mostrarlos en el siguiente orden: 
primero, ultimo, segundo, penultimo y tercero
 */
package arreglos_ejercicio_1;
import java.util.Scanner;

public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numeros[] = new int[10];
        
        for (int i = 0; i < 10; i++) {
            System.out.println((i+1)+" Digite un numero: ");
            numeros[i] = entrada.nextInt();
        }
        
        
        System.out.println("El resultado es: ");
        for (int i = 0; i < 5; i++) {
                System.out.print(numeros[i]+" "); //primero,segundo
                System.out.print(numeros[9-i]+" "); //ultimo,penultimo
            }
        System.out.println(); //salto de linea
    }

}
