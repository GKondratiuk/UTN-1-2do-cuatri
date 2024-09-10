
import java.util.Scanner;
import javax.swing.JOptionPane;

        //Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca 
//un numero negativo
public class Ciclos01{
public static void main (String Args[]){
	Scanner entrada = new Scanner(System.in);
	
	double num, cuadrado;
	boolean bandera;
	num = 0;
	bandera = true;
	

	do{
		System.out.println("");
		System.out.println("Escriba un numero");
		num = Double.parseDouble(JOptionPane.showInputDialog("Digite un número"));
		cuadrado = Math.pow(num, 2);
			if(num < 0){
				bandera = false;
				System.out.println("El programa finalizó por ser un numero negativo");
			}else{
				System.out.println("El numero " + num + " Elevado al cuadrado, es igual a " + cuadrado);
	}
	}while(bandera);





//	while(bandera){
//		System.out.println("");
//		System.out.println("Escriba un numero");
//		num = entrada.nextDouble();
//		cuadrado = Math.pow(num, 2);
//		
//		if(num < 0){
//			bandera = false;
//			System.out.println("El programa finalizó por ser un numero negativo");
//			}else{
//		
//		System.out.println("El numero " + num + " Elevado al cuadrado, es igual a " + cuadrado);
//	}
//		}
//        
//		
	


		
//	for(int i = 0; i < 100; i++ ){
//		System.out.println("");
//		System.out.println("Escriba un numero");
//		num = entrada.nextDouble();
//		cuadrado = Math.pow(num, 2);
//		
//		if(num < 0){
//			System.out.println("El programa finalizó por ser un numero negativo");
//			break;
//			}else{
//		
//		System.out.println("El numero " + num + " Elevado al cuadrado, es igual a " + cuadrado);
//		
//		
//		}	
//		
//	}
        
        

        
}
}

 
