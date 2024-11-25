from gestion.datos import *
import os
os.system ('cls')


Datos = {
    "Alumnos": [
        {
            "Nombre": "Juan",
            "Apellido": "Pérez",
            "DNI": "12345678",
            "Fecha de nacimiento": "01/01/2005",
            "Tutor": "María López",
            "Notas": [8, 9, 7],
            "Faltas": 3,
            "Amonestaciones": 1
        }
    ]
} # datos de prueba


def menu():
    print("1. Mostrar todos los alumnos")
    print("2. Agregar alumno")
    print("3. Modificar datos")
    print("4. Eliminar alumno")
    print("5. Agregar notas")
    # print("6. Agregar faltas")
    # print("7. Agregar amonestaciones")
    print("8. Salir")
    return int(input("Seleccion opcion: "))

def opciones():
    while True:
        opcion = menu()
        if opcion == 1:
            mostrar_todos(Datos)
        elif opcion == 2:
            agregar_alumno(Datos)
        elif opcion == 3:
            modificar_alumno(Datos)
        elif opcion == 4:
            eliminar_alumno(Datos)
        elif opcion == 5:
            agregar_notas(Datos)
        # elif opcion == 6:
        #     agregar_faltas(Datos)
        # elif opcion == 7:
        #     agregar_amonestaciones(Datos)
        elif opcion == 8:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    opciones()