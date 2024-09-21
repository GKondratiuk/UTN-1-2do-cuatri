/*EJERCICIO 09: PEDIR EL DIA, MES Y AÑO DE UNA FECHA E INDICAR SI LA FECHA ES CORRECTA. 
SUPONIENDO QUE TODOS LOS MESES SON DE 30 DIAS*/
package Ciclos09;

import javax.swing.JOptionPane;


public class Ejercicio09 {
    public static void main(String[] args) {
          
        
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el Dia"));
        
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el Mes"));
        
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el Año"));
        
        if((dia != 0)&&(dia <=30)){
            if((mes != 0)&&(mes <=12)){
                if((anio !=0)&&(anio<=2024)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+ dia+"/"+mes+"/"+"/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha Incorrecta, Año incorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null, "Fecha Incorrecta, Mes incorrecto");
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha Incorrecta, Dia incorrecto");
        }
        
    }
    
}
