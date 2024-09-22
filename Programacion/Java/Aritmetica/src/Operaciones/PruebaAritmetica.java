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

    }

    public static void miMetodo() {
        // a = 10; variable limitada
        System.out.println("Aqui hay otro metodo");
    }
}
