package domain;
//para asignar que una clase es hija de otra, se coloca la palabra 'extends'
public class Empleado extends Persona {
    //como la clase empleado no la va a heredar nadie, vamos a utilizar atributos 'private'
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //para incrementar
    
    //constructores
    public Empleado(){
    this.idEmpleado = ++Empleado.contadorEmpleados;
    }
    
    public Empleado(String nombre, double sueldo) {
        //super(nombre); //para ingresar a los atributos de la clase padre se utiliza 'super'
        this();//estamos llamando desde acá al constructor vacio(llamando al constructor interno)
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }


    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
}
