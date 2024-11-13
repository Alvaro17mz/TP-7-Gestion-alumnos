def mostrar_todos(Datos):
    for alumno in Datos["Alumnos"]:
        print(alumno)

def agregar_alumno(Datos):
    nuevo_alumno = {
        "Nombre": input("Nombre del alumno: "),
        "Apellido": input("Apellido del alumno: "),
        "DNI": input("DNI del alumno: "),
        "Fecha de nacimiento": input("Fecha de nacimiento (DD/MM/AAAA):"),
        "Tutor": input("Nombre del tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0,
    }
    Datos["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado correctamente.")

def modificar_alumno(Datos):
    dni = input("Ingrese nuevo DNI del alumno: ")
    for alumno in Datos["Alumnos"]:
        if alumno["DNI"] == dni:
            print("1. Modificar nombre")
            print("2. Modificar apellido")
            print("3. Modificar fecha de nacimiento")
            print("4. Modificar tutor")
            print("5. Salir")
            opcion = input("Ingrese opción: ")
            if opcion == 1:
                alumno["Nombre"] = input("Ingrese nuevo nombre: ")
            elif opcion == 2:
                alumno["Apellido"] = input("Ingrese nuevo apellido: ")
            elif opcion == 3:
                alumno["Fecha de nacimiento"] = input("Nueva fecha de nacimiento: ")
            elif opcion == 4:
                alumno["Tutor"] = input("Nuevo tutor: ")
            elif opcion == 5:
                print("Saliendo del menú de modificación...")
                return
            print("Datos modificados.")
            return
    print("Alumno no encontrado.")