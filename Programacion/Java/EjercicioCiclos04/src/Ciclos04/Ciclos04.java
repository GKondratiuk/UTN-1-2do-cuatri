
/*EJERCICIO 4: PEDIR NUMEROS HASTA QUE SE TECLEE UNO NEGATIVO, Y MOSTRAR CUANTOS NUMEROS SE HAN INTRODUCIDO. 
LO HACEMOS PRIMERO EN LA CLASE SCANNER Y LUEGO CON LA CLASE JOPTION PANE*/
package Ciclos04;

import javax.swing.JOptionPane;

public class Ciclos04 {
    public static void main(String[] args) {
         
        int contador = 0;
        
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un Numero"));
        
        while(numero > -1){
            JOptionPane.showMessageDialog(null, "Se registró el numero " + numero);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro Numero"));
            contador = contador + 1;
        }
         JOptionPane.showMessageDialog(null, "Se Ingresó un total de " + contador + " Numeros sin contar el negativo");
    }
    
}
