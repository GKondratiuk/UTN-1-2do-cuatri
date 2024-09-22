package caja;

public class Caja {//clase publica caja
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (acciones)
    public Caja(){//Constructor 1 = vacio
    }
    
    //Constructor con parametros
    
    public Caja(int ancho, int alto, int profundo){//Constructor 2 con parametros
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    //Metodo
    
    public int calcularVolumen(){//Metodo para calcular
        return ancho * alto * profundo;
    }
    
}

