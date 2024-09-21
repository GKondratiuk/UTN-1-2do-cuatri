let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
//Creamos un objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    nombreCompleto: function(){ //método o función 
        return this.nombre+' ' +this.apellido
    },
    //METODO GET
    get nombreEdad(){
        return this.nombre + ' edad: ' +this.edad 
    },
    get lang(){
        return this.idioma.toUpperCase(); //convierte minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    }
}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona.nombreCompleto());
console.log(" ");
console.log("Ejecutando con un objeto")
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = "Salada 14";
persona2.telefono = "45678-1234";

console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona['apellido']) //accedemos como si fuera un arreglo
console.log("usamos el ciclo for in")
//for in
for(propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad])
}
console.log("cambiamos y modificamos un error")
persona.apellida = "Kondratiuk";//cambiamos dinamicamente el valor de un objeto
delete persona.apellida; //Eliminamos
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: Forma 1");
console.log(persona.nombre+", "+persona.apellido);

//Numero 2: a traves del ciclo for
console.log("Distintas formas de imprimir un objeto: Forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad])
}

//Numero 3: la funcion object.values()
console.log("Distintas formas de imprimir un objeto: Forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: Forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString)

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad)

console.log('comenzamos con el metodo get y set para idiomas')
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre,apellido,email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+apellido;
    }
}
let padre = new Persona3('Leo','Lopez','lopezl@gmail.com');
padre.nombre = 'Luis' //se pueden modificar los datos
padre.telefono = '123456789'; //agregamos una nueva propiedad
console.log(padre);
console.log(padre.nombreCompleto())
let madre = new Persona3('Laura','Contrera','contreral@gmail.com')
console.log(madre)
console.log(madre.telefono); //salta undefined porque la propiedad no está definida
console.log(madre.nombreCompleto())

console.log('DISTINTAS FORMAS DE CREAR OBJETOS');
//DISTINTAS FORMAS DE CREAR OBJETOS
//CASO OBJETO Nº 1
let miObjeto = new Object(); //Formal
//CASO OBJETO Nº 2
let miObjeto2 = {}; //Breve y recomendada
//CASO STRING
let miCadena1 = new String('Hola'); //Sintaxis formal
//CASO STRING Nº2
let miCadena2 = 'Hola'; //simplificada y recomendada

//CASO CON NUMEROS 1 
let miNumero = new Number(1);//Formal no recomendable
//CASO CON NUMEROS 2
let miNumero2 = 1; //Sintaxis recomendada
//CASO BOOLEAN1
let miBoolean = new Boolean(false); //Formal
//CASO BOOLEAN 2 
let miBoolean2 = false; //sintaxis recomendada

//CASO ARREGLOS 1
let miArreglo1 = new Array();//Formal
//CASO ARREGLO 2 
let miArreglo2 = [];//Sintaxis recomendada

//CASO FUNCIONES 1 
let miFuncion1 = new function(){}; //todo despues de new es considerado objeto
//CASO FUNCIONES 2
let miFuncion2 = function(){};//simplificada y recomendada

console.log('USO DE PROTOTIPE') //Para agregar propiedades
//USO DE PROTOTIPE
Persona3.prototype.telefono = '261683';
console.log(padre);
madre.telefono = 54261583;
console.log(madre.telefono);

console.log('USO DE CALL')//LLAMAR A UN METODO DEFINIDO EN OTRO OBJETO 
//USO DE CALL 
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo,telefono){
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ' ' + telefono;
        //return this.nombre + ' ' + this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('lic.','99999'))
console.log(persona4.nombreCompleto2.call(persona5,'Ing.','011567123'));

console.log('METODO APPLY') //OTRO METODO PARA REALIZAR LLAMADAS
//METODO APPLY
let arreglo = ['Ing.','111111'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo))