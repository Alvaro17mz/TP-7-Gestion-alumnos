from gestion.datos import *
#import os
#os.system ('cls')

def menu():
    print("1. Mostrar todos los alumnos")
    print("2. Agregar alumno")
    print("3. Modificar datos")
    print("4. Eliminar alumno")
    print("5. Mostrar alumno")
    print("6. Salir")
    return int(input("Seleccion opcion: "))

def opciones():
    while True:
        opcion = menu(Datos)
        if opcion == 1:
            mostrar_todos(Datos)
        elif opcion == 2:
            agregar_alumno(Datos)
        elif opcion == 3:
            modificar_alumno(Datos)
        elif opcion == 4:
            eliminar_alumno(Datos)
        elif opcion == 5:
            mostrar_alumno(Datos)
        elif opcion == 6:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    opciones()