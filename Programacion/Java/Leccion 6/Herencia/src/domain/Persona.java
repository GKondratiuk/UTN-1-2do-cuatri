package domain;

//clase
public class Persona {
    //atributos
    //se utiliza protected porque es la unica manera en que las clases hijas puedan heredar atributos 
    //aunque las mismas esten en otro paquete
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;
    //creamos un constructor vacio
    public Persona (){
        
    }
    //constructor 2 con parametro
    public Persona(String nombre){
    this.nombre = nombre;
    }
    //constructor 3 con todos los parametros
    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    //cuando generamos los getters, el ide no coloca los 'this'
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    //creamos metodo toString

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{");
        sb.append("nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append(", ").append(super.toString()); //para que nos muestre el espacio en memoria donde está alojado el objeto(clases padre e hijas)
        sb.append('}');
        return sb.toString();
    }

   
    
    
}
