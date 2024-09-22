
package Operaciones;


public class Aritmetica { //clase aritmetica 
    //Atributos de clase 
    int a;
    int b;
    
    //El constructor es un metodo especial - construye un objeto, reserva un espacio en memoria, inicializa los atributos de la clase
    public Aritmetica(){//constructor 1
        System.out.println("Se está ejecutando este constructor numero uno");
    }
    //Sobrecarga de constructores
    public Aritmetica(int a, int b){
        this.a = a; 
        this.b = b;
        System.out.println("Se está ejecutando el constructor numero dos");
    }
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    //Metodo dos
    public int sumarConRetorno(){
        //int resultado = a + b;++
        return this.a+this.b;
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return this.sumarConRetorno(); //podemos llamar a otro metodo que comparta la misma clase pero no es lo usual
    }
}
