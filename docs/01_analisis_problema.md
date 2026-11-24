# 01. Análisis del problema

## 1. Nombre del problema y asignatura
- **Problema:** Tiro parabólico (movimiento de proyectiles)
- **Asignatura donde se estudió:** [Fisica 1 , tercer semestre]

## 2. Descripción, justificación y planteamiento original
**Descripción:** Un proyectil se lanza desde el suelo con una velocidad inicial y un ángulo. Bajo la acción de la gravedad describe una trayectoria parabólica. La aplicación calcula sus componentes de velocidad, tiempo de vuelo, altura máxima, alcance y posición en un instante dado.

**Justificación:** el problema tiene fórmulas, validaciones (velocidad y ángulo), varios resultados y permite guardar varios lanzamientos para compararlos.

**Planteamiento original:** Un proyectil se lanza desde el suelo con una velocidad inicial de 20 m/s y un ángulo de 30° sobre la horizontal. Considerando g = 9.81 m/s², calcular: (a) las componentes de la velocidad, (b) el tiempo de vuelo, (c) la altura máxima y (d) el alcance horizontal.

## 3. Entradas
| Nombre | Tipo | Restricciones | Significado |
|---|---|---|---|
| velocidad_inicial | float | mayor que 0 | Rapidez de lanzamiento (m/s) |
| angulo | float | mayor que 0 y menor o igual a 90 | Ángulo de lanzamiento (grados) |
| gravedad | float | mayor que 0, valor por defecto 9.81 | Aceleración de la gravedad (m/s²) |
| t | float | entre 0 y el tiempo de vuelo | Instante para calcular la posición (s) |

## 4. Procesos
- Convertir el ángulo de grados a radianes.
- vx = v0 · cos(θ)
- vy = v0 · sen(θ)
- t_vuelo = 2 · vy / g
- h_max = vy² / (2 · g)
- alcance = vx · t_vuelo
- Posición en el instante t: x = vx · t ; y = vy · t − ½ · g · t²

**Reglas y decisiones:**
- Si la velocidad es menor o igual a 0, se rechaza la entrada.
- Si el ángulo no está en (0, 90], se rechaza la entrada.
- Si t es negativo o mayor al tiempo de vuelo, se rechaza (el proyectil ya tocó el suelo).

## 5. Salidas esperadas
Componentes vx y vy (m/s), tiempo de vuelo (s), altura máxima (m), alcance (m), posición (x, y) en el instante t (m), historial de lanzamientos y lanzamiento de mayor alcance.

## 6. Ejemplo original resuelto
**Datos:** v0 = 20 m/s, θ = 30°, g = 9.81 m/s²

**Procedimiento:**
- vx = 20 · cos 30° = 17.32 m/s
- vy = 20 · sen 30° = 10 m/s
- t_vuelo = 2(10) / 9.81 = 2.04 s
- h_max = (10)² / (2 · 9.81) = 5.10 m
- alcance = 17.32 · 2.0387 = 35.31 m

**Verificación:** alcance = v0² · sen(2θ) / g = 400 · sen 60° / 9.81 = 35.31 m

**Resultado:** vx = 17.32 m/s, vy = 10 m/s, t = 2.04 s, h_max = 5.10 m, alcance = 35.31 m.

Evidencia: `evidencias/evidencia_original.png`

## 7. Alcance de la aplicación
- Menú de opciones en consola.
- Registrar un nuevo lanzamiento con validación de datos.
- Calcular y mostrar todos los resultados.
- Calcular la posición en un instante t.
- Guardar los lanzamientos en una lista y mostrar el historial.
- Mostrar el lanzamiento de mayor alcance.

## 8. Comprobación de requisitos
| Requisito | Cumple | Cómo |
|---|---|---|
| Trabajado en otra materia | Sí | [Materia de Física] |
| Entradas, procesos y salidas identificables | Sí | Secciones 3, 4 y 5 |
| Reglas, validaciones o decisiones | Sí | Validación de velocidad, ángulo y t |
| Viable en consola con Python | Sí | Menú con input/print |
| Al menos dos clases con responsabilidades distintas | Sí | Proyectil (cálculos) y RegistroLanzamientos (lista e historial) |
| Ejemplo original resuelto para validar | Sí | Sección 6 |
