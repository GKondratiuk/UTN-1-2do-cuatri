package Operaciones;

public class PruebaAritmetica {

    public static void main(String[] args) {
        var a = 10; //Variables locales
        int b = 7; //Memoria stack - memoria de variable local
        miMetodo(); //llamamos al metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;

        aritmetica1.sumarNumeros();
        //Para alamacenar objetos o atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado = " + resultado);

        System.out.println("Aritmetica1 a: " + aritmetica1.a);
        System.out.println("Aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8); //llamamos al constructor numero dos
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null; esto no hace falta porque se genera automaticamente
        //System.gc(); - pensado para limpiar residuos - no se utiliza 
        
        Persona persona = new Persona("Ariel","Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }
//Modularidad creamos un nuevo método
    public static void miMetodo() {
        // a = 10; variable limitada
        System.out.println("Aqui hay otro metodo");
    }
}
//creamos una nueva clase
class Persona{
    String nombre;
    String apellido; 
    
    Persona(String nombre, String apellido){//constructor
        super(); //llamada al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}
class Imprimir{
    public Imprimir(){
        super(); //el constructor de la clase padre, para reservar memoria
    }
    public void imprimir (Persona persona){
        System.out.println("Persona desde la clase imprmir " + persona);
        System.out.println("Impresion del objeto actual (this): " + this);
        
    }
}