# Teoricas de Programación Avanzada

En los siguientes items, se desarrollan las preguntas acerca de la Tarea de Programación Avanzada uno.

## Preguntas y Respuestas

### 1. ¿Qué es un paradigma de programación?
Un paradigma de programación es un estilo o enfoque para resolver problemas y estructurar el código mediante el cual se puede desarrollar una solución en un lenguaje de programación. Los paradigmas comunes incluyen:

- **Programación Imperativa**: Define los pasos a seguir para lograr un resultado.
- **Programación Orientada a Objetos (POO)**: Se basa en la ejecución del código mediante una colección de objetos que trabajan juntos, combinando datos y funciones.
- **Programación Funcional**: Utiliza funciones matemáticas y promueve la inmutabilidad.
- **Programación Lógica**: Establece reglas y hechos para llegar a una conclusión.

### 2. ¿En qué se basa la Programación Orientada a Objetos?
La Programación Orientada a Objetos (POO) trata sobre la creación de objetos que modelan entidades del mundo real o conceptos abstractos. Los pilares de la POO son:

- **Encapsulamiento**: Oculta los detalles internos de los objetos.
- **Herencia**: Reutilización de código a través de la relación entre clases.
- **Polimorfismo**: Capacidad de tratar objetos de diferentes clases mediante la misma interfaz.
- **Abstracción**: Simplificación de conceptos complejos en representaciones más básicas.

### 3. ¿Cuál es la diferencia entre recursividad e iteración?
- **Recursividad**: Una función que se llama a sí misma para resolver instancias menores o más pequeñas de un problema. Ejemplo: cálculo de factoriales o búsqueda en árboles.
- **Iteración**: Técnica de programación que repite un bloque de código con un bucle varias veces, de modo que el bloque de código se ejecuta repetidamente según una condición dada.

Ambos métodos pueden tener diferentes complejidades en términos de la notación Big O. La recursividad puede ser más costosa si no se optimiza, aunque generalmente la iteración es más fácil de analizar.

### 4. Diferencia de rendimiento entre O(1) y O(n)
- **O(1)**: Complejidad constante, lo que significa que el tiempo de ejecución es el mismo sin importar el tamaño de la entrada. Ejemplo: acceso a un elemento de un array por su índice.
- **O(n)**: Complejidad lineal, donde el tiempo de ejecución crece proporcionalmente al tamaño de la entrada. Ejemplo: recorrer una lista de elementos.

O(1) es mucho más eficiente que O(n), especialmente cuando el tamaño de la entrada crece.

### 5. ¿Cómo se calcula el orden en un programa que funciona por etapas?
En un programa que funciona por etapas, la complejidad temporal se calcula analizando cada etapa por separado y sumando las complejidades. Sin embargo, en notación Big O, solo se considera el término dominante. Por ejemplo:

- Si una etapa es O(n) y otra es O(n²), la complejidad total es O(n²) ya que domina a O(n).

### 6. ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?
La complejidad temporal de un algoritmo recursivo se determina utilizando relaciones de recurrencia. Estas describen el tiempo que toma ejecutar una función recursiva en términos del tiempo que toman sus llamadas recursivas.

Ejemplo: En una recurrencia como \( T(n) = 2T(n/2) + O(n) \), que aparece en el algoritmo **merge sort**, la complejidad temporal resultante es O(n log n).

# Como Obtener Los Resultados

### Solución del problema de los caminos en la PCB

Se presentan dos métodos para contar la cantidad de caminos posibles entre dos puntos, \( A \) y \( B \), en una PCB representada como una grilla de tamaño \( N \times M \).

El punto \( A \) se encuentra en la esquina superior izquierda y el punto \( B \) en la esquina inferior derecha. Las restricciones del problema indican que solo se pueden hacer movimientos hacia la derecha o hacia abajo, sin retroceder ni moverse en diagonal.

He programado una clase llamada `Caminos`, que recibe los tamaños de la grilla \( N \) y \( M \), e implementa dos enfoques para resolver el problema:

### 1. Enfoque combinatorio:
Este enfoque calcula la cantidad de caminos posibles entre \( A \) y \( B \) utilizando el principio combinatorio. El problema se reduce a contar cuántos movimientos hacia abajo y hacia la derecha se necesitan para llegar a \( B \) desde \( A \), sin retroceder.

Matemáticamente, el número de caminos es:

\[
C(N+M, M) = \frac{(N + M)!}{N! M!}
\]

Este cálculo se optimiza utilizando bucles para reducir el número de operaciones, considerando \( N \) movimientos hacia abajo y \( M \) movimientos hacia la derecha.

### 2. Enfoque dinámico:
Este método utiliza programación dinámica. Se construye una matriz de \( (N+1) \times (M+1) \), donde cada celda \( (i, j) \) almacena la cantidad de caminos que se pueden tomar para llegar a esa posición desde \( A \).

Cada celda puede alcanzarse desde la celda de arriba \( (i-1, j) \) o desde la celda a la izquierda \( (i, j-1) \), sumando los valores de estas celdas. El valor final en la celda \( (N, M) \) contendrá el número total de caminos posibles.

### 3. Medición del tiempo de ejecución:
Ambos métodos utilizan un decorador `medir_tiempo` para medir el tiempo de ejecución, lo que permite comparar la eficiencia de los algoritmos para diferentes tamaños de grilla. El decorador registra el tiempo de inicio y finalización de la función, calculando el tiempo total de ejecución.

### 4. Comparación gráfica de los tiempos de ejecución:
Para visualizar la diferencia en los tiempos de ejecución de ambos métodos, se creó el script `gen_graf.py`, que genera gráficos comparativos utilizando `matplotlib`. Este script ejecuta ambos métodos para distintos tamaños de grillas, desde \( 5 \times 5 \) hasta \( 1000 \times 1000 \), y luego grafica los tiempos obtenidos.

Los tiempos de ejecución se almacenan y se representan gráficamente, y el gráfico final se guarda como `execution_times.svg`.



