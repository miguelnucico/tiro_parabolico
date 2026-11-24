"""Clase Proyectil: representa un lanzamiento de tiro parabólico desde el suelo.

Responsabilidad: validar los datos del lanzamiento y realizar los cálculos
físicos. No imprime menús ni guarda historial.
"""

import math


class Proyectil:
    def __init__(self, velocidad_inicial, angulo, gravedad=9.81):
        """Valida los datos y los guarda como atributos del objeto.

        velocidad_inicial: rapidez de lanzamiento en m/s (mayor que 0)
        angulo: ángulo de lanzamiento en grados (0 < angulo <= 90)
        gravedad: aceleración de la gravedad en m/s² (mayor que 0)
        """
        if velocidad_inicial <= 0:
            raise ValueError("La velocidad inicial debe ser mayor que 0.")
        if angulo <= 0 or angulo > 90:
            raise ValueError("El ángulo debe ser mayor que 0 y menor o igual a 90 grados.")
        if gravedad <= 0:
            raise ValueError("La gravedad debe ser mayor que 0.")

        self.velocidad_inicial = velocidad_inicial
        self.angulo = angulo
        self.gravedad = gravedad

    def componentes(self):
        """Devuelve (vx, vy) en m/s. El ángulo se convierte a radianes."""
        rad = math.radians(self.angulo)
        vx = self.velocidad_inicial * math.cos(rad)
        vy = self.velocidad_inicial * math.sin(rad)
        return vx, vy

    def tiempo_vuelo(self):
        """Tiempo en segundos hasta volver al suelo: t = 2*vy / g."""
        _, vy = self.componentes()
        return 2 * vy / self.gravedad

    def altura_maxima(self):
        """Altura máxima en metros: h = vy² / (2*g)."""
        _, vy = self.componentes()
        return vy ** 2 / (2 * self.gravedad)

    def alcance(self):
        """Distancia horizontal total en metros: x = vx * t_vuelo."""
        vx, _ = self.componentes()
        return vx * self.tiempo_vuelo()

    def posicion(self, t):
        """Devuelve (x, y) en metros en el instante t (segundos).

        x = vx*t ; y = vy*t - 1/2*g*t²
        """
        if t < 0 or t > self.tiempo_vuelo():
            raise ValueError("El tiempo debe estar entre 0 y el tiempo de vuelo.")
        vx, vy = self.componentes()
        x = vx * t
        y = vy * t - 0.5 * self.gravedad * t ** 2
        return x, y
