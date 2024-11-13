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