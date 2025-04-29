# AUTOR: Carlos Castro

# Lista de alumnos
alumnos = []

# Entrada de datos
while True:
    nombre = input("Introduce el nombre y apellidos del alumno (o vacío para terminar): ")
    if not nombre:
        break
    try:
        notas = {
            "Programación": float(input("Nota Programación: ")),
            "Lenguaje de Marcas": float(input("Nota Lenguaje de Marcas: ")),
            "Bases de Datos": float(input("Nota Bases de Datos: ")),
            "Sistemas Informáticos": float(input("Nota Sistemas Informáticos: "))
        }
        alumnos.append({"nombre": nombre, "notas": notas})
    except ValueError:
        print("Introduce una nota válida (número).")
        continue

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
    if not alumnos or modulo not in alumnos[0]['notas']:
        print("Módulo no válido.")
        return
    notas = [alumno['notas'][modulo] for alumno in alumnos]
    print(f"Nota media en {modulo}: {sum(notas)/len(notas):.2f}")

def max_modulo():
    modulo = input("Nombre del módulo: ")
    if not alumnos or modulo not in alumnos[0]['notas']:
        print("Módulo no válido.")
        return
    max_alumno = max(alumnos, key=lambda x: x['notas'][modulo])
    print(f"Nota máxima en {modulo}: {max_alumno['notas'][modulo]} ({max_alumno['nombre']})")

def min_modulo():
    modulo = input("Nombre del módulo: ")
    if not alumnos or modulo not in alumnos[0]['notas']:
        print("Módulo no válido.")
        return
    min_alumno = min(alumnos, key=lambda x: x['notas'][modulo])
    print(f"Nota mínima en {modulo}: {min_alumno['notas'][modulo]} ({min_alumno['nombre']})")

# Menú
def menu():
    opciones = {
        "1": ("Mostrar todos los alumnos y sus notas", imprimir_curso),
        "2": ("Consultar notas de un alumno", notas_alumno),
        "3": ("Calcular nota media de un módulo", media_modulo),
        "4": ("Mostrar nota máxima de un módulo", max_modulo),
        "5": ("Mostrar nota mínima de un módulo", min_modulo),
        "6": ("Salir", exit)
    }

    while True:
        print("\n--- MENÚ ---")
        for k, v in opciones.items():
            print(f"{k}. {v[0]}")
        eleccion = input("Selecciona una opción: ")
        if eleccion in opciones:
            opciones[eleccion][1]()
        else:
            print("Opción no válida.")

# Ejecutar menú
menu()
