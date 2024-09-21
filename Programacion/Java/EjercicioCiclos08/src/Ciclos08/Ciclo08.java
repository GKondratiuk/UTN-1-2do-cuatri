/*EJERCICIO 08: PEDIR UN NUMERO N Y MOSTRAR TODOS LOS NUMEROS DEL 1 AL N */
package Ciclos08;

import javax.swing.JOptionPane;

public class Ciclo08 {

    public static void main(String[] args) {

        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        int i = 1;

        while (i <= numero) {
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}
