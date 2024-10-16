package test;

import dominio.Persona; /*hay que importar "el dominio" porque está en otro paquete*/

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57000, false);
         System.out.println("Persona 1: " + persona1);
        System.out.println("persona1 su nombre es: " + persona1.getNombre()); //esta es la manera de traer informacion
        
        //Modficiamos a traves de los metodos
        persona1.setNombre("Juan Ignacio"); //Modificamos el nombre con el metodo setNombre
        //persona1.nombre = "Juan ignacio"; - antes modificabamos de esta manera
        //System.out.println("Nombre es: " + persona1.nombre); - Esto era una manera anterior para acceder al nombre
        System.out.println("persona1 su nombre es: " + persona1.getNombre()); // esta es la forma de obtener informacion de los objetos
        System.out.println("El resultado para el sueldo es: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado()); //nos trae la informacion del buleano
        
        //Tarea: Crear otro objeto de tipo Persona, asginar valores de manera inicial
        //Imprimir, luego modificar sus valores y volver a impirimir
        System.out.println(" ");
        
        Persona persona2 = new Persona("Guillermo",100000, true);
        System.out.println("Nombre: " + persona2.getNombre());
        System.out.println("sueldo: " + persona2.getSueldo());
        System.out.println("Nombre: " + persona2.isEliminado());
        
        System.out.println(" ");
        
        persona2.setNombre("Morena");
        persona2.setSueldo(200000);
        persona2.setEliminado(false);
        System.out.println("Nombre: " + persona2.getNombre());
        System.out.println("sueldo: " + persona2.getSueldo());
        System.out.println("Nombre: " + persona2.isEliminado());
        
        System.out.println(" ");
        
        System.out.println("Persona 1: " + persona1); //accede al toString, cosa que antes no se podía 
    }
}
