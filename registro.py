"""Clase RegistroLanzamientos: guarda y consulta los lanzamientos realizados.

Responsabilidad: administrar la lista de objetos Proyectil. No hace cálculos
físicos (los pide a Proyectil) ni muestra menús.
"""

from proyectil import Proyectil


class RegistroLanzamientos:
    def __init__(self):
        """Inicializa la lista de lanzamientos vacía."""
        self.lanzamientos = []

    def agregar(self, proyectil):
        """Guarda un objeto Proyectil en la lista."""
        if not isinstance(proyectil, Proyectil):
            raise TypeError("Solo se pueden agregar objetos de la clase Proyectil.")
        self.lanzamientos.append(proyectil)

    def cantidad(self):
        """Devuelve cuántos lanzamientos hay registrados."""
        return len(self.lanzamientos)

    def obtener(self, indice):
        """Devuelve el lanzamiento número 'indice' (se cuenta desde 1)."""
        if indice < 1 or indice > len(self.lanzamientos):
            raise ValueError("Número de lanzamiento fuera de rango.")
        return self.lanzamientos[indice - 1]

    def mayor_alcance(self):
        """Devuelve el Proyectil de mayor alcance, o None si no hay lanzamientos."""
        if len(self.lanzamientos) == 0:
            return None
        mejor = self.lanzamientos[0]
        for proyectil in self.lanzamientos:
            if proyectil.alcance() > mejor.alcance():
                mejor = proyectil
        return mejor
