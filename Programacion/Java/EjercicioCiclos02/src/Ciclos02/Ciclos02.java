package Ciclos02;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos02 {

    public static void main(String[] args) {

        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while (numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es positivo");
            } else {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es negativo");
            }
            System.out.println("");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite Otro número"));

        }
        JOptionPane.showMessageDialog(null, "El número " + numero + " Finaliza el programa");
    }

}
