/*EJERCICIO 3: LEER NÚMEROS HASTA QUE SE INTRODUZCA UN CERO PARA CADA UNO INDICAR SI ES PAR O IMPAR
PRIMERO LO HAREMOS CON LA CLASE SCANNER, LUEGO CON LA CLASE JOPTIONPANE*/
package Ciclos03;

import javax.swing.JOptionPane;
public class Ciclos03 {
    
    public static void main(String[] args) {
          

        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));

        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null,("El numero " + numero + " Es Par"));
                JOptionPane.showMessageDialog(null,("Ingrese Otro Número"));
                numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
            } else {
                JOptionPane.showMessageDialog(null,("El numero " + numero + " Es Impar"));
                System.out.println("Introduzca otro número");
                JOptionPane.showMessageDialog(null,("Ingrese Otro Número"));
                numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
            }
        }

    }
    
}
