/*EJERCICIO 5: REALIZAR UN JUEGO PARA ADIVINAR UN NUMERO PARA ELLO GENERAR UN NUMERO ALEATORIO ENTRE 0-100 Y LUEGO IR PIDIENDO 
NUMEROS INDICANDO "ES MAYOR" O "ES MENOR" SEGUN SEA MAYOR O MENOR 
CON RESPECTO A N EL PROCESO TERMINA CUANDO EL USUARIO ACIERTA Y MOSTRAMOS EL NUMERO DE INTENOS HECHOS*/
package Ciclos05;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos05 {
    public static void main(String[] args) {
           Scanner entrada = new Scanner(System.in);
        
        int numero, aleatorio, conteo = 0;
        
        aleatorio = (int)(Math.random()*100);//genera un numero aleatorio
        
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null, "Felicitaciones, adivinaste el número");
            }
            conteo ++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en: " + conteo + " intentos");
    }

}
