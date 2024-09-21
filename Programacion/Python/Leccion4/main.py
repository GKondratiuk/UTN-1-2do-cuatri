# lista = Ariel, Lliliana, Natalia, Osvaldo
#Colecciones en Python

#Las listas se conocen como arreglos o vectores en otros lenguajes
print("******************************")
print("****DEFINIMOS LISTAS**********")
print("******CON CORCHETES***********")
print("******************************")

nombres = ["Naty","Osvaldo","Lily","Ariel"]

#LA LISTA MANTIENE UN ORDEN Y SE PUEDE MODIFICAR - ES MUTABLE

print(nombres) # accedemos a la lista de manera general
print(nombres[0]) #accedemos a la lista de manera individual
print(nombres[1]) #accedemos a la lista de manera individual
print(nombres[3]) #accedemos a la lista de manera individual
print(nombres[-1]) #Para recorrer del ultimo numero en adelante podemos utilizar los numeros negativos
print(nombres[-2]) #Para recorrer del ultimo numero en adelante podemos utilizar los numeros negativos
print()
#RECUPERAR UN RANGO DE LA LISTA

print(nombres[0:2]) #Recorre desde el indice 0 hasta el 1
print(nombres[ :3]) #Recorre desde el indice 0 hasta el 2
print(nombres[1: ]) #Recorre desde el indice 1 hasta el final
print()
#MODIFICAMOS UN VALOR
print()
nombres[2] = "Liliana" #Modificamos lili por liliana
nombres[0] = "Natalia" #modificamos nati por natalia
print(nombres)
print()

#ITERAR UNA LISTA

for nombre in nombres: #nombre es singular, la lista es plural 
    print(nombre)
else:
    print("Se acabaron los nombres de la lista")
    print()

#PREGUNTAMOS CUANTOS ELEMENTOS TIENE

print(len(nombres))
print()

#AGREGAMOS UN ELEMENTO AL FINAL DE LA LISTA

nombres.append("Guille")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)
print()

#AGREGAMOS UN ELEMENTO EN UN INDICE ESPECIFICO DE LA LISTA
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)
print()

#ELIMINAMOS UN ELEMENTO DE NUESTRA LISTA
nombres.remove("Alberto")
print(nombres)
print()

#ELIMINAMOS EL ÚLTIMO ELEMENTO DE LA LISTA
nombres.pop()
print(nombres)
print()

#ELIMINAMOS UN INDICE ESPECIFICO
del nombres[2] #Eliminamos a Debora
print(nombres) 
print()

#ELIMINAMOS TODOS LOS ELEMENTOS
nombres.clear()
print(nombres)
print()

#ELIMINAMOS LA LISTA
del nombres
# print(nombres) nos dirá que "nombres" no está definido a modo de error

print("****************************************************")
print("              DEFINIMOS TUPLAS")
print("               CON PARENTESIS ")
print("****************************************************")
#LAS TUPLAS MANTIENE UN ORDEN PERO NO SE PUEDEN MODIFICAR - SON INMUTABLES
print()
cocina = ("cuchara","cuchillo","tenedor")
print(cocina)
print(len(cocina))#Muestra la cantidad de elementos

#ACCEDEMOS A UN ELEMENTO 
print(cocina[0])#el elemento 0 es "cuchara"
print(cocina[-1])#el elemento -1 es "tenedor"

#ACCEDER A UN RANGO 
print(cocina[0:2]) #nos mostrará solo dos elementos

#EJEMPLO
verduras = ("papa",) # en la tupla se necesita aunque sea un elemento y la coma ","
print()
#RECORREMOS ELEMENTOS EN LA TUPLA
for cocinar in cocina:
    print(cocinar, end=" ") #para la funcion print finaliza con un espacio en vez de un salto de linea

#Es una mala práctica pero se pueden modificar las tuplas, pasandolas a listas y a tuplas nuevamente
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print(cocina)
print()

#ELIMINAMOS LA TUPLA
# del cocina - lo comentamos porque sino tira error en el codigo
print(cocina)

print()
print("****************************************************")
print("              DEFINIMOS SET O CONJUNTO")
print("                    CON LLAVES")
print("****************************************************")
print()
#TIPO SET 
#NO MANTIENE NINGUN INDICE, TIENE UN ORDEN ALEATORIO, SE PUEDE AGREGAR O ELIMINAR CONTENIDO.
# PERO NO SE PUEDE MODIFICAR NADA MAS - NO ES COMPLETAMENTE MUTABLE NI INMUTABLE 
planetas = {"Marte","Jupiter","Venus"}
print(len(planetas))
print("Marte" in planetas)
#Agregamos un elemento
planetas.add("Tierra")
planetas.add("Tierra") #SET no duplica
print(planetas)

planetas.remove("Jupiter")
print(planetas)#Removemos un archivo, tiene que ser con el nombre exacto o nos dará error el programa
planetas.discard("tierra") #Removemos un archivo, si no es el nombre exacto no nos cerrrá el programa pero no borrará el elemento
print(planetas)

planetas.clear() #limpiamos nuestro set
print(planetas)

# del planetas - eliminamos nuestro set

print()
print("****************************************************")
print("                    DICCIONARIO")
print("****************************************************")
print()
#EL DICCIONARIO ES MUTABLE
#"Maradona":10 Un diccionario está compuesto por dos elementos
#UNA LLAVE Y UN VALOR 
#DICT(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
print(len(diccionario)) #cantidad de elementos del diccionario
print(diccionario)
print(diccionario["IDE"]) #Accedemos a un elemento del diccionario con la llave(key)
print(diccionario.get("POO"))#Otra forma de obtener un elemento del diccionario
print(diccionario.get("SABD"))

diccionario["IDE"] = "ENTORNO DE DESARROLLO INTEGRADO"
print(diccionario)
print()
print("Recorremos el diccionario")
for termino in diccionario: 
    print(termino) #Imprime solo el termino
    
for termino, valor in diccionario.items():
    print(termino,valor) #Imprime termino y valor
    
#Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Estamos usando una función
    print(termino) #Muestra solo las llaves
    
for valor in diccionario.values():
    print(valor) #muestra solo valores sin las llaves
    
#Comprobar la existencia de algun elemento
print("IDE" in diccionario) # devuelve un booleano por si o por no

#Agregar un elemento
diccionario["PK"] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario 
del diccionario #borramos el diccionario
print()

#Concatenamos listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7,8,9,1]) #funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(5)) #funcion para ubicar en que indice se encuentra el valor ingresado
print(lista3.count(1)) #cuenta cuantos valores iguales hay adentro de la lista

#Para poner la lista al reves
lista3.reverse()
print(lista3)
print()
#para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3]*2 #multiplica la lista
print(lista)

lista3 = lista3 * 2
print(lista3)#Multiplica lista3
print()

#Metodos de ordenamiento - en python es una funcion
lista3.sort() #ordena los elementos de modo ascendente
print(lista3)
#ordenada de manera descendente
lista3.sort(reverse=True)
print(lista3)


#Repaso de tuplas
tupla = (4,'hola',6.78,[1,2,78],4,'hola')
print(tupla)

print(4 in tupla)# preguntamos si está el 4 en la tupla - devuelve booleano

print("****************************************************")
print("REPASO DE SET O CONJUNTO PARA DEFINIR UN CONJUNTO")
print("****************************************************")

#Los conjuntos se pueden instanciar de dos maneras
conjunto2 = set() #creamos conjunto vacío
conjunto1 = {'bye'} # creamos otro conjunto, pero de esta manera no se puede crear vacío

#Agregamos elementos
#en los Sets o conjuntos no se pueden agregar varios elementos en simultaneo.
conjunto2.add(7)
conjunto2.add('Hola')
conjunto1.add('Hola')
print(conjunto2)
print(conjunto1)
#preguntamos si el numero 3 NO está en el conjunto 1
print(3 not in conjunto1)
# comprobar si dos conjuntos son iguales
print(conjunto1 == conjunto2)

print("****************************************************")
print("OPERACIONES EN COJUNTOS")
print("****************************************************")
#Unimos dos conjuntos
conjunto3 = conjunto1 | conjunto2 #los conjuntos no "duplican" elementos
print(conjunto3)
#Guarda solo los elementos que tienen en comun
conjunto3 = conjunto1 & conjunto2
print(conjunto3)
#muestra los valores que están en el conjunto 2 y no en el conjunto1
conjunto3 = conjunto2 - conjunto1
print(conjunto3)
#imprimen valores que no comparten
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)
#Vemos si son subConjuntos o no 
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))
#Como saber si uno es un superConjunto de otro
print(conjunto3.issuperset(conjunto1))
#Como saber si uno es disconexo(que no comparte conexion) con otro
print(conjunto1.isdisjoint(conjunto2))#es falso porque comparten el "Hola"
#Convertir un conjunto totalmente inmutable
conjunto1 = frozenset #no se puede agregar, modificar o eliminar elementos del conjunto

print("****************************************************")
print("*************REPASO DICCIONARIOS********************")
print("****************************************************")
#{llave:valor}
diccionarioNuevo = {'Azul':'Blue','Rojo':'Red','Verde':'Green','Amarillo':'Yellow'}

#Como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel':{'Adad':40,'Altura':183},'Osvaldo':[45,1.85],'Natalia':[35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10:{'Nombre':'Lionel Messi', 'Edad':35, 'Altura':1.70,'Precio':'50 Millones','Posicion': 'Extremo Derecho'},
    11:{'Nombre':'Angel Di María', 'Edad':34, 'Altura':1.80,'Precio':'12 Millones','Posicion': 'Extremo Derecho'},
    24:{'Nombre':'Paulo Dybala', 'Edad':28, 'Altura':1.77,'Precio':'35 Millones','Posicion': 'Medio Campo'},
    19:{'Nombre':'Nicolas Otamendi', 'Edad':34, 'Altura':1.83,'Precio':'3.5 Millones','Posicion': 'Defensa Central'},
    1:{'Nombre':'Franco Armani', 'Edad':35, 'Altura':1.89,'Precio':'3.5 Millones','Posicion': 'Portero'},
    3:{'Nombre':'Guillermo Kondratiuk','Edad':32,'Altura':1.75,'Precio':'11 Millones','Posicion':'Lateral Izquierdo'},
    15:{'Nombre':'Camila Alvarez','Edad':29, 'Altura':1.65,'Precio':'11.5 Millones','Posicion':'Toda la Cancha'},
    7:{'Nombre':'Conejito Saviola','Edad':41,'Altura':1.68,'Precio':'40Millones','Posicion':'Extremo Derecho'}
}
#Imprime los datos de un jugador
#print(seleccionArgentina[10]) 

#Recorremos el diccionario
for llave,valor in seleccionArgentina.items():
    print(llave, valor)
#Nos indica al cantidad de elementos
print(len(seleccionArgentina))

print("****************************************************")
print("**********************PILAS*************************")
print("****************************************************")
#Pilas usando listas
pila = [1,2,3]
#Agregamos elementos a la pila por el final, agregamos o quitamos siempre al final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos por el final
elementoBorrado = pila.pop() #Quita el ultimo elemento y lo guarda en una variable
print(f'Sacamos elelemento: "{elementoBorrado}"')
print(f'pila quedó asi: {pila}')


print("************************************************************")
print("               Colas con listas")
print("Estructura de datos de tipo fifo(First input / First ouput)")
print("*************************************************************")
#Primero en entrar, primero en salir


cola = ['Ariel','Osvaldo','Liliana','Pilar']

#Agregamos elementos al final de la cola 
cola.append('Natalia')
cola.append('Jose')
print(cola)
print("")

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)
print('')
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)
print('')
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)

#OTRA MANERA DE RECORRER UN DICCIONARIO
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
print("")
#LA MANERA MAS SENCILLA DE RECORRER UN DICCIONARIO
for i in seleccionArgentina:
    print(f"{seleccionArgentina[i]}")