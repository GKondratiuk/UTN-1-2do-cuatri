
import java.util.Scanner;


public class Ejercicio01 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
	
	double num, cuadrado;
	boolean bandera;
	num = 0;
	bandera = true;
        
        	while(bandera){
		System.out.println("");
		System.out.println("Escriba un numero");
		num = entrada.nextDouble();
		cuadrado = Math.pow(num, 2);
		
		if(num < 0){
			bandera = false;
			System.out.println("El programa finalizó por ser un numero negativo");
			}else{
		
		System.out.println("El numero " + num + " Elevado al cuadrado, es igual a " + cuadrado);
	}
		}
        
		
	
    }
    
}
