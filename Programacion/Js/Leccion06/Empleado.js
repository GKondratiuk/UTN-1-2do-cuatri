
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