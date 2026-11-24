# 02. Pruebas y validación

Las pruebas se ejecutan desde el menú de `main.py`. Capturas de pantalla en `evidencias/` (ver nombres al final).

## Resumen
| ID | Tipo | Estado |
|---|---|---|
| P1 | Caso original | Aprobado |
| P2 | Caso normal adicional | Aprobado |
| P3 | Caso límite | Aprobado |
| P4 | Entradas inválidas | Aprobado |
| P5 | Mayor alcance (funcionalidad) | Aprobado |
| P6 | Posición en un instante t | Aprobado |
| P7 | Menú sin lanzamientos y opción inválida | Aprobado |

---

## P1. Caso original
- **Objetivo:** comprobar que la aplicación reproduce el ejercicio resuelto en la libreta.
- **Entradas:** opción 1, velocidad = 20 m/s, ángulo = 30°
- **Resultado esperado:** vx = 17.32 m/s, vy = 10.00 m/s, t = 2.04 s, h = 5.10 m, alcance = 35.31 m
- **Resultado obtenido:** vx = 17.32 m/s, vy = 10.00 m/s, t = 2.04 s, h = 5.10 m, alcance = 35.31 m
- **Estado:** Aprobado
- **Observaciones:** coincide con el procedimiento de `01_analisis_problema.md`.

## P2. Caso normal adicional
- **Objetivo:** verificar otro lanzamiento con datos válidos.
- **Entradas:** opción 1, velocidad = 30 m/s, ángulo = 45°
- **Resultado esperado:** vx = vy = 21.21 m/s, t = 4.32 s, h = 22.94 m, alcance = 91.74 m (verificado con v0²·sen 2θ / g = 900/9.81)
- **Resultado obtenido:** vx = 21.21 m/s, vy = 21.21 m/s, t = 4.32 s, h = 22.94 m, alcance = 91.74 m
- **Estado:** Aprobado
- **Observaciones:** a 45° el alcance es el máximo posible para esa velocidad.

## P3. Caso límite permitido
- **Objetivo:** probar el ángulo máximo permitido (90°, lanzamiento vertical).
- **Entradas:** opción 1, velocidad = 20 m/s, ángulo = 90°
- **Resultado esperado:** vx = 0.00 m/s, vy = 20.00 m/s, t = 4.08 s, h = 20.39 m, alcance = 0.00 m
- **Resultado obtenido:** vx = 0.00 m/s, vy = 20.00 m/s, t = 4.08 s, h = 20.39 m, alcance = 0.00 m
- **Estado:** Aprobado
- **Observaciones:** internamente el alcance es 5e-15 por la precisión de los decimales de la computadora; con 2 decimales se muestra 0.00.

## P4. Entradas inválidas
- **Objetivo:** comprobar que la aplicación rechaza datos incorrectos sin cerrarse.
- **Entradas (tres intentos en la opción 1):** (a) velocidad = −5, ángulo = 30; (b) velocidad = 20, ángulo = 120; (c) velocidad = "abc"
- **Resultado esperado:** (a) mensaje de velocidad inválida; (b) mensaje de ángulo inválido; (c) mensaje de que debe ser un número. Siempre regresa al menú.
- **Resultado obtenido:** (a) "Error: La velocidad inicial debe ser mayor que 0."; (b) "Error: El ángulo debe ser mayor que 0 y menor o igual a 90 grados."; (c) "Error: debes escribir un número."
- **Estado:** Aprobado
- **Observaciones:** no se registró ningún lanzamiento con datos inválidos.

## P5. Mayor alcance
- **Objetivo:** verificar la funcionalidad que recorre la lista con un ciclo.
- **Entradas:** tras registrar P1, P2 y P3, opción 4
- **Resultado esperado:** lanzamiento de 30 m/s y 45° con alcance 91.74 m
- **Resultado obtenido:** "Mayor alcance: 91.74 m (v0 = 30.00 m/s, ángulo = 45.00°)"
- **Estado:** Aprobado
- **Observaciones:** también se comprobó el historial (opción 3) con los 3 lanzamientos.

## P6. Posición en un instante t
- **Objetivo:** comprobar la posición en el tiempo.
- **Entradas:** opción 2, lanzamiento 1 (20 m/s, 30°), t = 1 s
- **Resultado esperado:** x = 17.32 m, y = 5.095 m (10·1 − ½·9.81·1²)
- **Resultado obtenido:** x = 17.32 m, y = 5.09 m
- **Estado:** Aprobado
- **Observaciones:** el valor exacto es 5.095; la computadora lo guarda como 5.09499… y al redondear a 2 decimales muestra 5.09.

## P7. Sin lanzamientos y opción inválida
- **Objetivo:** probar que el menú se comporta bien al iniciar vacío.
- **Entradas:** (a) opción 4 al iniciar; (b) opción 9
- **Resultado esperado:** (a) aviso de que no hay lanzamientos; (b) "Opción no válida."
- **Resultado obtenido:** (a) "Aún no hay lanzamientos registrados."; (b) "Opción no válida."
- **Estado:** Aprobado
- **Observaciones:** `mayor_alcance()` devuelve None con la lista vacía y no falla.

---

## Capturas
- `evidencias/menu_principal.png`
- `evidencias/caso_original.png`
- `evidencias/pruebas_adicionales.png`
