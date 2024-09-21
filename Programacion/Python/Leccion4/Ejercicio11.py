#EJERCICIO 11: AGENDA TELEFONICA
#HACER UN PROGRAMA QUE SIMULE UNA AGENDA DE CONTACTOS. CREAR UN DICCIONARIO DONDE
# LA CLAVE SEA EL NOMBRE DEL USUARIO Y EL VALOR SEA EL TELEFONO
#EL PROGRAMA TENDRÁ EL SIGUIENTE MENÚ DE OPCIONES:
# 1. NUEVO CONTACTO
# 2. BORRAR CONTACTO
# 3. VER CONTACTOS EXISTENTES
# 4. SALIR

agenda = {}

while True:
    print('.:MENU:.')
    print('1. NUEVO CONTACTO')
    print('2. BORRAR CONTACTO')
    print('3. VER CONTACTOS EXISTENTES')
    print('4. SALIR')
    
    opcion = int(input("Digite una opcion de Menu: "))
    if opcion == 1:
        nombre = input("Digite nombre del contacto")
        telefono = input("Digite el numero de telefono")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agendado con exito")
        else:
            print("Ya existe el nombre de contacto")
    elif opcion == 2:
        nombre = input("Ingrese nombre del contacto")
        if nombre in agenda: 
            del (agenda[nombre])
            print("Se eliminó el contacto")
        else:
            print("Contacto inexistente")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():#con esta funcion podemos ver llave y valor
            print(f'Nombre: {clave}, Telefono:{valor}') 
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
        