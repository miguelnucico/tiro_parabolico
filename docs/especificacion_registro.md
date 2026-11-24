# Especificación de la clase RegistroLanzamientos

Archivo de la clase: `registro.py`

## 1. Identificación
- **Nombre:** RegistroLanzamientos
- **Objetivo:** guardar y consultar los lanzamientos hechos durante la ejecución.
- **Responsabilidad:** administrar la lista de objetos Proyectil. No hace cálculos físicos (los pide a Proyectil) ni muestra menús.

## 2. Atributos
| Nombre | Tipo | Significado | Valor inicial |
|---|---|---|---|
| lanzamientos | list | Lista de objetos Proyectil registrados | Lista vacía [] |

## 3. Constructor `__init__(self)`
- No recibe datos.
- Inicializa `self.lanzamientos` como una lista vacía.

## 4. Métodos
| Método | Objetivo | Entradas | Atributos usados | Algoritmo | Resultado |
|---|---|---|---|---|---|
| agregar(proyectil) | Guardar un lanzamiento | Un objeto Proyectil | lanzamientos | Verificar con `isinstance` que sea Proyectil y agregarlo con `append` | Ninguno |
| cantidad() | Saber cuántos hay | Ninguna | lanzamientos | Devolver `len` de la lista | int |
| obtener(indice) | Recuperar un lanzamiento | Número de lanzamiento (1, 2, 3…) | lanzamientos | Devolver el elemento en la posición indice − 1 | Objeto Proyectil |
| mayor_alcance() | Encontrar el mejor lanzamiento | Ninguna | lanzamientos | Recorrer la lista con un ciclo y comparar `alcance()` de cada uno | Objeto Proyectil o None si la lista está vacía |

**Validaciones:**
- `agregar` rechaza (lanza `TypeError`) todo lo que no sea un Proyectil.
- `obtener` lanza `ValueError` si el índice está fuera de rango.
- `mayor_alcance` no debe fallar con la lista vacía: devuelve None.

## 5. Reglas que Copilot NO puede alterar
- Debe usar una lista de Python para guardar los lanzamientos.
- `mayor_alcance` debe usar un ciclo explícito (`for`), no `max()`, para practicar ciclos.
- No debe copiar las fórmulas de Proyectil; debe llamar a sus métodos.
- No usa `print` ni `input`.

## 6. Ejemplo de uso esperado
Tras agregar Proyectil(20, 30) y Proyectil(30, 45), `cantidad()` es 2 y `mayor_alcance()` devuelve el de 30 m/s y 45°.
