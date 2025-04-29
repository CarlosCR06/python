alumnos = []

while True:
    nombre = input("Introduce el nombre y apellidos del alumno (o vacío para terminar): ")
    if not nombre:
        break
    notas = {
        "Programación": float(input("Nota Programación: ")),
        "Lenguaje de Marcas": float(input("Nota Lenguaje de Marcas: ")),
        "Bases de Datos": float(input("Nota Bases de Datos: ")),
        "Sistemas Informáticos": float(input("Nota Sistemas Informáticos: "))
    }
    alumnos.append({"nombre": nombre, "notas": notas})

# Funciones
def imprimir_curso():
    for alumno in alumnos:
        print(f"{alumno['nombre']}: {alumno['notas']}")

def notas_alumno():
    nombre = input("Nombre del alumno: ")
    for alumno in alumnos:
        if alumno['nombre'] == nombre:
            print(alumno['notas'])
            return
    print("Alumno no encontrado.")

def media_modulo():
    modulo = input("Nombre del módulo: ")
    notas = [alumno['notas'][modulo] for alumno in alumnos]
    print(f"Nota media en {modulo}: {sum(notas)/len(notas):.2f}")

def max_modulo():
    modulo = input("Nombre del módulo: ")
    max_alumno = max(alumnos, key=lambda x: x['notas'][modulo])
    print(f"Nota máxima en {modulo}: {max_alumno['notas'][modulo]} ({max_alumno['nombre']})")

def min_modulo():
    modulo = input("Nombre del módulo: ")
    min_alumno