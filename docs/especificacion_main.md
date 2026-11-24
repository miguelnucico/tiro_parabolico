# Especificación de main.py

## 1. Objetivo
Programa principal de consola. Muestra un menú, crea los objetos y llama a sus métodos. No contiene fórmulas físicas.

## 2. Importaciones
`from proyectil import Proyectil` y `from registro import RegistroLanzamientos`

## 3. Objetos a crear
- Un solo objeto `registro = RegistroLanzamientos()` al inicio del programa.
- Un objeto `Proyectil` nuevo cada vez que el usuario elige la opción 1.

## 4. Menú
```
===== TIRO PARABÓLICO =====
1. Nuevo lanzamiento
2. Posición en un instante t
3. Ver historial
4. Mayor alcance
5. Salir
```

## 5. Secuencia de operaciones por opción
- **1. Nuevo lanzamiento:** pedir velocidad y ángulo (gravedad usa el valor por defecto), crear el Proyectil, agregarlo al registro y mostrar componentes, tiempo de vuelo, altura máxima y alcance con 2 decimales.
- **2. Posición en t:** si no hay lanzamientos, avisar. Si hay, mostrar el historial, pedir el número de lanzamiento y el tiempo t, y mostrar (x, y).
- **3. Ver historial:** si está vacío, avisar. Si no, recorrer el registro con un ciclo y mostrar para cada lanzamiento número, velocidad, ángulo y alcance.
- **4. Mayor alcance:** llamar a `mayor_alcance()`; si devuelve None, avisar que no hay lanzamientos; si no, mostrar sus datos.
- **5. Salir:** mostrar mensaje de despedida y terminar.

## 6. Validación de entradas
- Los números se piden con `input`, se convierten con `float` dentro de `try/except ValueError`.
- Si el texto no es un número, mostrar error y volver al menú sin cerrar el programa.
- Los errores `ValueError` lanzados por las clases se atrapan y se muestran como mensaje.
- Si la opción del menú no es de 1 a 5, mostrar "Opción no válida".

## 7. Condición de salida
El menú se repite con un ciclo `while` hasta que el usuario elige la opción 5.

## 8. Reglas que Copilot NO puede alterar
- `main.py` no contiene fórmulas; todo cálculo se hace llamando métodos de las clases.
- El programa no debe cerrarse por un error de captura.
- Los resultados se muestran con 2 decimales y con unidades.
