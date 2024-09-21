
package Operaciones;


public class Aritmetica { //clase aritmetica 
    //Atributos de clase 
    int a;
    int b;
    
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
