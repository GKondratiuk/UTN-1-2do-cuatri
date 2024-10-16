package domain;
//clase
public class Persona {

   
    //cargamos los atributos
    private int idPersona;
    private static int contadorPersona; //static porque no se reinician sus valores y para invocar a los atributos
    private String nombre;
    
    //Constructor
    public Persona(String nombre){
    this.nombre = nombre;
    //Incrementar el contador por cada objeto nuevo 
    Persona.contadorPersona++; //No utilizar el operador this
    //vamos a asignar un nuevo valor a la variable idPersona
    this.idPersona = Persona.contadorPersona; //el atributo no estatico que se asocia al estatico
    }
    
     public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
}
