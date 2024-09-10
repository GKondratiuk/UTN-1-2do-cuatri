package Clases;

public class PruebaPersona {

    public static void main(String[] args) {
        Persona persona1 = new Persona(); //llamamos al constructor 
        persona1.nombre = "Ariel";
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion(); //Llamamos al metodo creado en el constructor Persona

        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2); //Nos muestra el espacio guardado en memora
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Osvaldo"; //Le asignamos un valor
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion(); //Llamamos al metodo creado en el cunstructor Persona

    }

}
