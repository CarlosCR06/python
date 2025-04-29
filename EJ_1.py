from datetime import date, datetime
from typeguard import typechecked
import calendar


@typechecked
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


@typechecked
def parsear_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%d/%m/%Y").date()


@typechecked
class MiFecha:
    def __init__(self, fecha):
        self.__fecha = fecha

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    def añadir_dias(self, n):
        año = self.__fecha.year
        mes = self.__fecha.month
        dia = self.__fecha.day
        while n != 0:
            if n > 0:
                dias_mes = calendar.monthrange(año, mes)[1]
                if dia < dias_mes:
                    dia += 1
                else:
                    dia = 1
                    if mes == 12:
                        mes = 1
                        año += 1
                    else:
                        mes += 1
                n -= 1
            else:
                if dia > 1:
                    dia -= 1
                else:
                    if mes == 1:
                        mes = 12
                        año -= 1
                    else:
                        mes -= 1
                    dia = calendar.monthrange(año, mes)[1]
                n += 1
        self.__fecha = date(año, mes, dia)

    def añadir_meses(self, n):
        mes = self.__fecha.month - 1 + n
        año = self.__fecha.year + mes // 12
        mes = mes % 12 + 1
        dia = min(self.__fecha.day, calendar.monthrange(año, mes)[1])
        self.__fecha = date(año, mes, dia)

    def añadir_años(self, n):
        try:
            self.__fecha = self.__fecha.replace(year=self.__fecha.year + n)
        except ValueError:
            self.__fecha = self.__fecha.replace(day=28, month=2, year=self.__fecha.year + n)

    def dias_entre(self, otra):
        return abs((self.__fecha - otra.fecha).days)

    def formato_largo(self):
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        dia_semana = dias_semana[self.__fecha.weekday()]
        mes_nombre = meses[self.__fecha.month - 1]
        return f"{dia_semana}, {self.__fecha.day} de {mes_nombre} de {self.__fecha.year}"

    def __str__(self):
        return self.__fecha.strftime("%d/%m/%Y")

    def __repr__(self):
        return f"MiFecha({self.__fecha.isoformat()})"

    def __eq__(self, otro):
        return isinstance(otro, MiFecha) and self.__fecha == otro.fecha

    def __lt__(self, otro):
        return self.__fecha < otro.fecha

    def __gt__(self, otro):
        return self.__fecha > otro.fecha


@typechecked
class Menu:
    def __init__(self):
        self.__opciones = []
        self.__mi_fecha = None

    def añadir_opcion(self, texto, funcion):
        self.__opciones.append((texto, funcion))

    def mostrar(self):
        while True:
            print("\n--- MENÚ ---")
            for i, (texto, _) in enumerate(self.__opciones, start=1):
                print(f"{i}. {texto}")
            try:
                eleccion = int(input("Selecciona una opción: "))
                if 1 <= eleccion <= len(self.__opciones):
                    self.__opciones[eleccion - 1][1]()
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Debes escribir un número.")

    def introducir_fecha(self):
        entrada = input("Introduce la fecha (dd/mm/aaaa): ")
        if validar_fecha(entrada):
            self.__mi_fecha = MiFecha(parsear_fecha(entrada))
            print("Fecha guardada:", self.__mi_fecha)
        else:
            print("Fecha inválida.")

    def añadir_dias(self):
        if self.__mi_fecha:
            try:
                n = int(input("¿Cuántos días quieres añadir (o restar)? "))
                self.__mi_fecha.añadir_dias(n)
                print("Nueva fecha:", self.__mi_fecha)
            except ValueError:
                print("Introduce un número válido.")
        else:
            print("Primero debes introducir una fecha.")

    def añadir_meses(self):
        if self.__mi_fecha:
            try:
                n = int(input("¿Cuántos meses quieres añadir (o restar)? "))
                self.__mi_fecha.añadir_meses(n)
                print("Nueva fecha:", self.__mi_fecha)
            except ValueError:
                print("Introduce un número válido.")
        else:
            print("Primero debes introducir una fecha.")

    def añadir_años(self):
        if self.__mi_fecha:
            try:
                n = int(input("¿Cuántos años quieres añadir (o restar)? "))
                self.__mi_fecha.añadir_años(n)
                print("Nueva fecha:", self.__mi_fecha)
            except ValueError:
                print("Introduce un número válido.")
        else:
            print("Primero debes introducir una fecha.")

    def comparar_fecha(self):
        if self.__mi_fecha:
            entrada = input("Introduce otra fecha para comparar (dd/mm/aaaa): ")
            if validar_fecha(entrada):
                otra = MiFecha(parsear_fecha(entrada))
                if otra < self.__mi_fecha:
                    print(f"{otra} es anterior a {self.__mi_fecha}")
                elif otra > self.__mi_fecha:
                    print(f"{otra} es posterior a {self.__mi_fecha}")
                else:
                    print("Las fechas son iguales.")
                print("Diferencia en días:", self.__mi_fecha.dias_entre(otra))
            else:
                print("Fecha inválida.")
        else:
            print("Primero debes introducir una fecha.")

    def mostrar_formato_largo(self):
        if self.__mi_fecha:
            print("Fecha en formato largo:", self.__mi_fecha.formato_largo())
        else:
            print("Primero debes introducir una fecha.")

    def terminar(self):
        print("¡Programa terminado!")
        exit()

    def cargar_opciones(self):
        self.añadir_opcion("Introducir una fecha", self.introducir_fecha)
        self.añadir_opcion("Añadir días", self.añadir_dias)
        self.añadir_opcion("Añadir meses", self.añadir_meses)
        self.añadir_opcion("Añadir años", self.añadir_años)
        self.añadir_opcion("Comparar con otra fecha", self.comparar_fecha)
        self.añadir_opcion("Mostrar formato largo", self.mostrar_formato_largo)
        self.añadir_opcion("Terminar", self.terminar)


# Ejecución
if __name__ == "__main__":
    menu = Menu()
    menu.cargar_opciones()
    menu.mostrar()
