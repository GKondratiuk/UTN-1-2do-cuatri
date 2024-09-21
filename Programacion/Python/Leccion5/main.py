#Comenzamos con funciones
#mi_funcion() #No se puede llamar antes de definir una funcion
#Definimos una funcion

def mi_funcion():#para identificar la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")
    
mi_funcion()#estamos llamando a la funcion
mi_funcion() #se puede llamar a una funcion N cantidad de veces.

#Desempaquetamos un lista para que se pueda mostrar 
def show(name, lastName):
    print(name + " " + lastName)
person = ["Guillermo", "Kondratiuk"]
show(person[0],person[1])
show(*person)#esto es lo mismo que lo anterior pero todo junto

person2 = ("Osvaldo", "Giordanini")#Desempaquetamos tupla
show(person2[0],person2[1])
show(*person2)

person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3) #ponemos ** porque hay que desempaquetar 1 cosa mas 

numbers = [1,2,3,4,5] #aunque la lista esté vacía se ejecuta el else
for n in numbers: 
    print(n)
    if n == 3:
        break #es la unica manera de que no se ejecute el else, es poniendo un break
else:
    print("Esto se termina")
    
# List Comprehension, lista de comprension
names = ["Paolo","Rodrigo","Lupe","Pepe"]
alongp = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongp)

bottleC = [{"name":"Quilmes", "country":"Argentina"},
           {"name":"Corona", "country":"Mexico"},
           {"name":"Stella Artois", "country":"Belgica"}]
arg = [b for b in bottleC if b["country"]== "Argentina"]
print(arg)
print(bottleC)

#Paso de Argumentos (funciones)

def mi_funcion2(name,lastName):
    print("Saludos a todos a traves del canal de youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2('Jorge','Lucero')

#La Palabra Return en funciones
#Creamos una funcion para sumar

def sumar(a,b):
    return a+b
resultado = sumar(78,22)
# print(f'El resultado de la suma es {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')#se puede llamar a la funcion desde la funcion print

def sumar2(a:int = 0,b:int = 0) -> int: #le damos un valor por default 
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22,66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #normalmente se utiliza *args
    for nombre in nombres: # se van a convertir en tuplas
        print(nombre)
listarNombres('Lucas','Jose','Alan','Patricio','Carlos','Marcos')
listarNombres('Lucia','Andrea','Azul','Candela','Carolina','Catalina')

def listarTerminos(**terminos):#por defecto se utiliza **kwargs
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos() #no recibe nada, nada se va a mostrar
listarTerminos(IDE = 'Integrated Develoment Enviroment', PK='Primaruy KEY')
listarTerminos(Nombre = 'Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres: 
        print(nombre)
nombres2 = ['Tito','Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('carla')
#desplegarNombres(10) - esto no es un objeto iterable
desplegarNombres((10, 11)) #esto si porque es una tupla
desplegarNombres([22,55]) #esto si porque es una lista

#Funciones Recursivas
def factorial(numero):
    if numero == 1: #Caso Base
        return 1 
    else:
        return numero * factorial(numero-1) #caso recursivo
    
numeroFactorial = int(input("Digite un numero para calcular el factorial: "))
resultado = factorial(5)# lo hacemos en codigo duro
print(f'El facotorial del numero {numeroFactorial} es: {resultado}') #tarea que el usuario ingrese el numero para realizar el factorial