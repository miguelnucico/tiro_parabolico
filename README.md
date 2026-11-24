# Tiro parabólico

Aplicación de consola en Python que calcula el movimiento de un proyectil lanzado desde el suelo.

Proyecto Integrador · Programación II

## Descripción
Dado una velocidad inicial y un ángulo, la aplicación calcula las componentes de la velocidad, el tiempo de vuelo, la altura máxima, el alcance y la posición del proyectil en cualquier instante. Guarda los lanzamientos en un historial y permite consultar el de mayor alcance.

## Asignatura original
Problema estudiado en: [Fisica 1 , tercer semestre].

## Objetivo
Aplicar variables, operaciones, decisiones, ciclos, listas, funciones, clases, atributos, constructores, métodos y objetos para resolver en Python un problema ya trabajado en otra asignatura.

## Funcionalidades
- Registrar lanzamientos con validación de datos.
- Calcular componentes, tiempo de vuelo, altura máxima y alcance.
- Calcular la posición (x, y) en un instante t.
- Ver el historial de lanzamientos.
- Consultar el lanzamiento de mayor alcance.

## Clases
- **Proyectil** (`proyectil.py`): valida los datos y realiza los cálculos físicos.
- **RegistroLanzamientos** (`registro.py`): guarda los lanzamientos en una lista y los consulta.
- **main.py**: menú de consola que crea los objetos y llama a sus métodos.

## Requisitos
- Python 3.8 o superior
- Sin librerías externas (solo `math`)

## Instalación
```bash
git clone URL_DEL_REPOSITORIO
cd tiro_parabolico
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

## Ejecución
```bash
python main.py
```

## Ejemplo (ejercicio original)
Opción 1, velocidad = 20 m/s, ángulo = 30°:
```
vx = 17.32 m/s
vy = 10.00 m/s
Tiempo de vuelo = 2.04 s
Altura máxima = 5.10 m
Alcance = 35.31 m
```

## Pruebas
Los casos de prueba están en [`docs/02_pruebas.md`](docs/02_pruebas.md). El análisis del problema, las especificaciones y la reflexión sobre Copilot están en la carpeta [`docs/`](docs/). Las evidencias están en [`evidencias/`](evidencias/).

## Estructura
```
tiro_parabolico/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── proyectil.py
├── registro.py
├── docs/
│   ├── 01_analisis_problema.md
│   ├── especificacion_proyectil.md
│   ├── especificacion_registro.md
│   ├── especificacion_main.md
│   ├── 02_pruebas.md
│   └── 03_uso_copilot.md
└── evidencias/
```
