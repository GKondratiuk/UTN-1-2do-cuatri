/*
EJERCICIO 11: DISEÑAR UN PROGRAMA QUE MUESTRE EL PRODUCTO DE LOS 10 PRIMEROS NUMEROS IMPARES 
*/
package ciclos11;

import javax.swing.JOptionPane;


public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i<=20; i+= 2){
            producto *= i;
        }
        JOptionPane.showMessageDialog(null,"El producto de los numeros impares es: " + producto);
    }
    
}
