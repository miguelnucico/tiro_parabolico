"""Programa principal: menú de consola del tiro parabólico.

Aquí solo se crean objetos y se llaman sus métodos; las fórmulas viven en
la clase Proyectil.
"""

from proyectil import Proyectil
from registro import RegistroLanzamientos


def mostrar_menu():
    print("\n===== TIRO PARABÓLICO =====")
    print("1. Nuevo lanzamiento")
    print("2. Posición en un instante t")
    print("3. Ver historial")
    print("4. Mayor alcance")
    print("5. Salir")


def pedir_numero(mensaje):
    """Pide un número. Si el texto no es válido, avisa y devuelve None."""
    try:
        return float(input(mensaje))
    except ValueError:
        print("Error: debes escribir un número.")
        return None


def nuevo_lanzamiento(registro):
    velocidad = pedir_numero("Velocidad inicial (m/s): ")
    if velocidad is None:
        return
    angulo = pedir_numero("Ángulo (grados): ")
    if angulo is None:
        return

    try:
        proyectil = Proyectil(velocidad, angulo)
    except ValueError as error:
        print(f"Error: {error}")
        return

    registro.agregar(proyectil)
    vx, vy = proyectil.componentes()
    print(f"\nLanzamiento #{registro.cantidad()} registrado.")
    print(f"vx = {vx:.2f} m/s")
    print(f"vy = {vy:.2f} m/s")
    print(f"Tiempo de vuelo = {proyectil.tiempo_vuelo():.2f} s")
    print(f"Altura máxima = {proyectil.altura_maxima():.2f} m")
    print(f"Alcance = {proyectil.alcance():.2f} m")


def mostrar_historial(registro):
    if registro.cantidad() == 0:
        print("Aún no hay lanzamientos registrados.")
        return
    print("\n--- Historial de lanzamientos ---")
    for numero in range(1, registro.cantidad() + 1):
        p = registro.obtener(numero)
        print(f"#{numero}: v0 = {p.velocidad_inicial:.2f} m/s, "
              f"ángulo = {p.angulo:.2f}°, alcance = {p.alcance():.2f} m")


def posicion_en_tiempo(registro):
    if registro.cantidad() == 0:
        print("Aún no hay lanzamientos registrados.")
        return
    mostrar_historial(registro)
    numero = pedir_numero("Número de lanzamiento: ")
    if numero is None:
        return
    if numero != int(numero):
        print("Error: el número de lanzamiento debe ser entero.")
        return
    t = pedir_numero("Tiempo t (s): ")
    if t is None:
        return

    try:
        proyectil = registro.obtener(int(numero))
        x, y = proyectil.posicion(t)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"En t = {t:.2f} s: x = {x:.2f} m, y = {y:.2f} m")


def mostrar_mayor_alcance(registro):
    mejor = registro.mayor_alcance()
    if mejor is None:
        print("Aún no hay lanzamientos registrados.")
        return
    print(f"Mayor alcance: {mejor.alcance():.2f} m "
          f"(v0 = {mejor.velocidad_inicial:.2f} m/s, "
          f"ángulo = {mejor.angulo:.2f}°)")


def main():
    registro = RegistroLanzamientos()
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            nuevo_lanzamiento(registro)
        elif opcion == "2":
            posicion_en_tiempo(registro)
        elif opcion == "3":
            mostrar_historial(registro)
        elif opcion == "4":
            mostrar_mayor_alcance(registro)
        elif opcion == "5":
            print("Hasta luego.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
