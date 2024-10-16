from Persona2 import Persona2
print('Creacion de objetos'.center(50,'-')) #centra una cadena a traves de guiones
if __name__ == '__main__':
    persona5 = Persona2('Lionel','Messi',35)
    persona5.mostrar_detalle()

    print(__name__)

print('Eliminación de objetos'.center(50,'-'))
#esto no es algo que se vea normalmente, esto hace que todo se elmine para recuperar espacio en memoria
del persona5 