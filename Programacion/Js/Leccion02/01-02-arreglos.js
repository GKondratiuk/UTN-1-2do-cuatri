/*Forma vieja de declarar un array
let autos = new Array('Ferrari','Renault','BMW');
console.log(autos);
*/
//Forma moderna para declarar Array
const autos = ['Ferrari','Renault','BMW']
console.log(autos)
console.log()
//Recorremos los elementos de un array - manual
console.log(autos[0])
console.log(autos[2])
console.log();
//Recorremos los elementos del array - automatico
for(let i = 0; i < autos.length; i++){
    console.log(i +' : '+ autos[i])
}

//MODIFICAMOS LOS ELEMENTOS DE ARREGLO
autos[1] = 'Volvo';
console.log(autos);

//AGREGAMOS NUEVOS VALORES AL ARREGLO 
autos.push("audi");//agregamos el elemento al final
console.log(autos);

//OTRAS FORMAS DE AGREGAR ELEMENTOS AL ARREGLO
autos[autos.length] = "Porche";//agregamos al final
console.log(autos);

//TERCERA FORMA DE AGREGAR ELEMENTOS 
autos[6] = "Renault"; //tener cuidado en que indice colocamos el elementos
console.log(autos);

//Como preguntar si es un Array o un Arreglo
console.log(Array.isArray(autos))

//Otra manera de identificar si es un array
console.log(autos instanceof Array)