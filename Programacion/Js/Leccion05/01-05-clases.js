//clase
class Persona{ //clase padre

    static contadorPersonas= 0; //Atributo estatico
    //email = 'Valor default email'; // Atributo NO estático

    static get MAX_OBJ(){ //este metodo simula una constante
        return 5; //el máximo de objeto que vamos a poder crear
    }

    constructor(nombre,apellido){
        //los atributos no pueden llamarse igual que los getters and setters
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++ Persona.contadorPersonas;
        }
        else{
            console.log('Se ha superado el maximo de objetos permitidos')
        }
        
        //console.log('Se incrementa el contador: ' + Persona.contadorObjetosPersona)
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

    nombreCompleto(){
        return this.idPersona + ' ' +this._nombre + ' ' +this._apellido;
    }

    //Sobreescribiendo el metodo de la clase padre (Object)
    toString(){//Regresa un String
        //se aplica el polimorfismo que significa = multiples formas en tiempo de ejecucion
        //El metodo que se ejecuta depende si es una referencia de un tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log('saludos desde este metodo static');
    }
    static saludar2(persona){
        console.log(persona.nombre + ' ' + persona.apellido);
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

    //Sobre-escritura
    nombreCompleto(){
        return super.nombreCompleto() + ', ' + this._departamento;
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
console.log(empleado1.nombreCompleto())


//Object.prototype.toString esta es la manera de acceder a atributos y metodos de manera dinamica

console.log(empleado1.toString());
console.log(persona1.toString());

//persona1.saludar(); //no se utiliza desde el objeto - no es posible llamar un metodo estatico desde el objeto 

Persona.saludar(); //los metodos estaticos se deben asociar a los objetos
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona); //las clases hijas tambien heredan estos metodos

console.log(persona1.email);
console.log(empleado1.email);
console.log(Persona.email);//no se puede acceder desde la clase porque no es estatico
console.log(persona1.toString())
console.log(persona2.toString())
console.log(empleado1.toString())
console.log(Persona.contadorPersonas)//hay 3 instancias
let persona3 = new Persona('Carla', 'Pertosi');
console.log(persona3.toString());

console.log(Persona.MAX_OBJ); //el valor no se puede modificar ni alterar

let persona4 = new Persona('Franco','Diaz');
console.log(persona4.toString());
let persona5 = new Persona('Liliana','Paz');
console.log(persona5.toString());

