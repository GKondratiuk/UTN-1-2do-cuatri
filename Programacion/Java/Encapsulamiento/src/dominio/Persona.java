package dominio;
//CLASE PERSONA
public class Persona {
    //ATRIBUTOS - siempre en privado
    private String nombre;
    private double sueldo;
    private boolean eliminado;

    //CONSTRUCTOR - siempre publico con las variables
    public Persona(String nombre, double sueldo, boolean eliminado){
        //atributo + variable
        this.nombre = nombre; 
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    
    public double getSueldo(){
        return sueldo;
    }
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }
    //para los booleanos no se utiliza get, se utiliza is. 
    public boolean isEliminado(){
        return eliminado;
    }
    public void setEliminado(boolean eliminado){
        this.eliminado = eliminado;
    }
    
    
}
