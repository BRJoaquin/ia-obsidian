
La programación dinámica es una técnica utilizada para resolver problemas de optimización que tienen una estructura de subproblemas superpuestos. En el contexto del aprendizaje por refuerzo, la programación dinámica se utiliza para resolver [[Procesos de Decisión de Markov]] **cuando se tiene una descripción completa del ambiente**. Los algoritmos de programación dinámica hacen uso de la [[Ecuación de Bellman]] para iterativamente mejorar la [[Función de valor]] o la [[Política]].

Aquí te presento algunos de los algoritmos de programación dinámica más utilizados:

1. **Iteración de Valor (Value Iteration)**: Este algoritmo resuelve un MDP encontrando primero la función de valor óptima. Se inicia con una función de valor arbitraria y se mejora iterativamente utilizando la ecuación de Bellman hasta que converge a la función de valor óptima. Finalmente, se extrae la política óptima de la función de valor óptima. vease [[Iteración de Valor (value iteration)]]

2. **Iteración de Política (Policy Iteration)**: Este algoritmo comienza con una política arbitraria y luego alterna entre dos pasos: evaluación de la política (calculando la función de valor para la política actual) y mejora de la política (haciendo que la política sea "codiciosa" con respecto a la función de valor actual). Este proceso se repite hasta que la política converge a la política óptima. vease [[Iteración de Política (policy iteration)]]


# Ventajas y Desventajas

La elección entre Iteración de Valor (VI) e Iteración de Política (PI) depende de las características específicas del problema y de las limitaciones computacionales. A continuación, algunas ventajas y desventajas de cada método:

### Iteración de Valor

**Ventajas**:

- En general, es más sencillo de implementar. Solo necesita realizar un paso de actualización en cada iteración.

- Puede ser más eficiente si el número de acciones es mucho mayor que el número de estados, ya que no necesita realizar la evaluación completa de la política en cada iteración.

**Desventajas**:

- Puede requerir más iteraciones para converger que la Iteración de Política, ya que cada actualización solo cambia la función de valor en una pequeña cantidad.

- La política extraída solo está garantizada para ser óptima cuando la función de valor ha convergido completamente.

### Iteración de Política

**Ventajas**:

- Suele converger más rápidamente que la Iteración de Valor en términos del número de iteraciones principales (cada una compuesta por una evaluación completa de la política y una mejora de la política).

- La política mejora y es garantizada como óptima en cada iteración, incluso antes de la convergencia.

**Desventajas**:

- Cada iteración puede ser computacionalmente costosa porque requiere la resolución de un sistema de ecuaciones lineales durante la evaluación de la política.

- Si el número de acciones es mucho mayor que el número de estados, PI puede ser menos eficiente que VI.

**En resumen, si el costo computacional de la evaluación de la política es muy alto, o si se necesita una solución aproximada rápidamente, la Iteración de Valor puede ser más adecuada. Sin embargo, si la velocidad de convergencia es una prioridad y el costo computacional de la evaluación de la política es manejable, la Iteración de Política puede ser una mejor opción.**

Sí, efectivamente puedes pensar en la Iteración de Valor como un caso especial de la Iteración de Política donde la fase de Evaluación de la Política se trunca a una sola actualización. 

# Iteración de Valor como Caso Especial de Iteración de Política

La Iteración de Valor puede considerarse como un tipo de Iteración de Política Modificada, **donde el número de pasos de evaluación se limita a uno antes de cada mejora de la política**.

En la Iteración de Valor, solo se realiza una actualización de la función de valor (utilizando la ecuación de Bellman) antes de actuar codiciosamente con respecto a la función de valor actualizada para mejorar la política. Esto es en contraste con la Iteración de Política completa, donde se realiza una evaluación completa de la política (hasta que la función de valor converge) antes de cada mejora de la política.

Es importante mencionar que, aunque la Iteración de Valor puede verse como un caso especial de Iteración de Política, los dos algoritmos pueden tener diferentes propiedades de convergencia y eficiencia dependiendo del problema específico.

# Videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/3idKCA2IIEk?start=156" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
