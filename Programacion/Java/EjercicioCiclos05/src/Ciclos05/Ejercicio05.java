/*EJERCICIO 5: REALIZAR UN JUEGO PARA ADIVINAR UN NUMERO PARA ELLO GENERAR UN NUMERO ALEATORIO ENTRE 0-100 Y LUEGO IR PIDIENDO 
NUMEROS INDICANDO "ES MAYOR" O "ES MENOR" SEGUN SEA MAYOR O MENOR 
CON RESPECTO A N EL PROCESO TERMINA CUANDO EL USUARIO ACIERTA Y MOSTRAMOS EL NUMERO DE INTENOS HECHOS*/
package Ciclos05;

import java.util.Scanner;

public class Ejercicio05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, aleatorio, conteo = 0;
        
        aleatorio = (int)(Math.random()*100);//genera un numero aleatorio
        
        do{
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("¡¡¡Felicidades, adivinaste el numero !!");
            }
            conteo ++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: " + conteo + " intentos");
    }
    
}
