# Especificación de la clase Proyectil

Archivo de la clase: `proyectil.py`

## 1. Identificación
- **Nombre:** Proyectil
- **Objetivo:** representar un lanzamiento de tiro parabólico desde el suelo.
- **Responsabilidad:** validar los datos del lanzamiento y realizar todos los cálculos físicos. No imprime menús ni guarda historial.

## 2. Atributos
| Nombre | Tipo | Significado | Valor inicial |
|---|---|---|---|
| velocidad_inicial | float | Rapidez de lanzamiento (m/s) | El que recibe el constructor |
| angulo | float | Ángulo de lanzamiento en grados | El que recibe el constructor |
| gravedad | float | Aceleración de la gravedad (m/s²) | 9.81 si no se indica |

## 3. Constructor `__init__(self, velocidad_inicial, angulo, gravedad=9.81)`
- Recibe velocidad, ángulo y gravedad (opcional).
- Valida los datos antes de guardarlos.
- Si algún dato es inválido, lanza `ValueError` con un mensaje claro.
- Si son válidos, los guarda en `self.velocidad_inicial`, `self.angulo` y `self.gravedad`.

## 4. Métodos
| Método | Objetivo | Entradas | Atributos usados | Algoritmo | Resultado |
|---|---|---|---|---|---|
| componentes() | Obtener vx y vy | Ninguna | velocidad_inicial, angulo | Convertir el ángulo a radianes con `math.radians`. vx = v0·cos(θ); vy = v0·sen(θ) | Tupla (vx, vy) en m/s |
| tiempo_vuelo() | Tiempo hasta volver al suelo | Ninguna | gravedad, usa componentes() | t = 2·vy / g | float en s |
| altura_maxima() | Altura máxima alcanzada | Ninguna | gravedad, usa componentes() | h = vy² / (2·g) | float en m |
| alcance() | Distancia horizontal total | Ninguna | usa componentes() y tiempo_vuelo() | x = vx · t_vuelo | float en m |
| posicion(t) | Posición en un instante t | t (float, segundos) | gravedad, usa componentes() | x = vx·t ; y = vy·t − ½·g·t² | Tupla (x, y) en m |

**Validaciones:**
- `velocidad_inicial` debe ser mayor que 0.
- `angulo` debe cumplir 0 < ángulo ≤ 90.
- `gravedad` debe ser mayor que 0.
- En `posicion(t)`: t debe ser mayor o igual a 0 y menor o igual al tiempo de vuelo; si no, lanza `ValueError`.

## 5. Reglas que Copilot NO puede alterar
- Las fórmulas deben ser exactamente las de esta especificación.
- El ángulo se recibe en grados y se convierte a radianes dentro de la clase.
- Los métodos de cálculo devuelven valores, no usan `print` ni `input`.
- No redondear dentro de los cálculos; el redondeo solo se hace al mostrar resultados.
- Solo se puede usar el módulo `math`, sin librerías externas.
- Los nombres de atributos y métodos deben ser los de esta especificación.

## 6. Ejemplo de uso esperado
Proyectil(20, 30) debe dar: componentes() ≈ (17.32, 10.0), tiempo_vuelo() ≈ 2.04, altura_maxima() ≈ 5.10, alcance() ≈ 35.31.
