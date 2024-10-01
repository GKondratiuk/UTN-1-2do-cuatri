//clase
class Persona{ //clase padre
    constructor(nombre,apellido){
        //los atributos no pueden llamarse igual que los getters and setters
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;   
    }
    set nombre(nombre){
        //accedemos al atributo del constructor
        // y lo igualamos al get
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido
    }
}

//creamos nuestra clase Empleado que extiende de persona
class Empleado extends Persona{
    constructor(nombre,apellido,departamento){
        //hay que llamar al constructor de la clase padre
        super(nombre,apellido);
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento
    }
    set departamento(departamento){
        this._departamento = departamento
    }
}

let persona1 = new Persona('Martin','Perez');
//console.log(persona1);-
//accedemos al valor del atributo a través del get
console.log(persona1.nombre);
//accedemos al set
persona1.nombre = 'Juan Carlos'
//mostramos el set
console.log(persona1.nombre)
console.log(persona1.apellido)
let persona2 = new Persona('Carlos','Lara');
//console.log(persona2);
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre)
console.log(persona2.apellido)

let empleado1 = new Empleado('María','Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombre)