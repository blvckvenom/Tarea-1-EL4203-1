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


