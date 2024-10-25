class Persona{

    static contadorPersonas = 0;

    constructor(nombre,apellido,edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona(){
        return this._idPersona;
    }

    get nombre(){
        return this._nombre
    }
    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }

    get edad(){
        return this._edad;
    }
    set edad(edad){
        this._edad = edad;
    }

    toString(){
        return`
        ${this._idPersona}
        ${this._nombre}
        ${this._apellido}
        ${this._edad};
        `
    }
}


//creamos la clase
class Empleado extends Persona{
    //creamos el contador con metodo static porque esta asociado a la clase
        static contadorEmpleados = 0;
    //creamos un constructor
        constructor(nombre,apellido,edad,sueldo){
            //llamamos a los atributos de la clase padre
            super(nombre,apellido,edad);
            this._idEmpleado = ++Empleado.contadorEmpleados;
            this._sueldo = sueldo;
        }
    
        //metodos get y set 
            get idEmpleado(){
                return this._idEmpleado;
            }
    
            get sueldo(){
                return this._sueldo
            }
            set sueldo(sueldo){
                this._sueldo = sueldo;
            }
    //creamos metodo toString para realizar una cadena de caracteres, tambien llamamos al toString de la clase padre
            toString(){
                //return super.toString()+' '+this._idEmpleado+' '+this._sueldo;
                //podemos convertirlo en un template string
                return `
                ${super.toString()}
                ${this._idEmpleado} 
                ${this._sueldo}`;
            }
    }

    class Cliente extends Persona{

        static contadorClientes = 0;
    
        constructor(nombre,apellido,edad,fechaRegistro){
            super(nombre,apellido,edad);
            this._idCliente = ++Cliente.contadorClientes;
            this._fechaRegistro = fechaRegistro;
        }
    
        get idCliente(){
            return this._idCliente;
        }
    
        get fechaRegistro(){
            return this._fechaRegistro
        }
    
        set fechaRegistro(fechaRegistro){
            this._fechaRegistro = fechaRegistro
        }
    
        toString(){
            return `
            ${super.toString()}
            ${this._idCliente}
            ${this._fechaRegistro}
            `;
        }
        
    }

    //VIMOS HASTA EL VIDEO 5 CLASE 9