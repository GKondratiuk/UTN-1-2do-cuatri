package domain;

public class Empleado extends Persona{//si la clase padre se declara cmo final, no podria tener clase hija
    @Override
    public void imprimir(){
        System.out.println("Metodo imprmir desde la clase hija");
    }
}
