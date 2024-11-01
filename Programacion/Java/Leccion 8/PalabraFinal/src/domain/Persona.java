package domain;

public class Persona {
    // esto en java es una constante
    public final static int CONSTANTE_AQUI = 15;
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
    public void imprimir(){
        System.out.println("Metodo para imprmir");
    }
    
}
