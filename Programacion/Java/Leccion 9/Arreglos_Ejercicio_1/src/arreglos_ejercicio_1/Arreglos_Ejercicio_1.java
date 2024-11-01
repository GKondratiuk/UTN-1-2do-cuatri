package arreglos_ejercicio_1;
import java.util.Scanner;
public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float[] arreglo = new float[5];
        System.out.println("Guardando los datos en el arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Digite un numero: ");
            arreglo[i] = entrada.nextFloat();
            //falta video 7 de la clase 11 pt 1
        }
    }
}
