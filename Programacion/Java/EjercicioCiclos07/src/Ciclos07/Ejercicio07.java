//PEDIR NUMEROS HASTA QUE SE INTRODUZCA UNO NEGATIVO
//Y CALCULAR LA MEDIA(PROMEDIO)
package Ciclos07;

import java.util.Scanner;

public class Ejercicio07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        
        System.out.println("Digite un numero:");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            suma += numero;
            conteo ++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo == 0){
            System.out.println("Error, la division entre 0 no existe");
        }
        else{
            promedio = (float)suma/conteo;
            System.out.println("El promedio es: " + promedio);
        }
    }

}
