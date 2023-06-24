
La programación dinámica es una técnica utilizada para resolver problemas de optimización que tienen una estructura de subproblemas superpuestos. En el contexto del aprendizaje por refuerzo, la programación dinámica se utiliza para resolver [[Procesos de Decisión de Markov]] **cuando se tiene una descripción completa del ambiente**. Los algoritmos de programación dinámica hacen uso de la [[Ecuación de Bellman]] para iterativamente mejorar la [[Función de valor]] o la [[Política]].

Aquí te presento algunos de los algoritmos de programación dinámica más utilizados:

1. **Iteración de Valor (Value Iteration)**: Este algoritmo resuelve un MDP encontrando primero la función de valor óptima. Se inicia con una función de valor arbitraria y se mejora iterativamente utilizando la ecuación de Bellman hasta que converge a la función de valor óptima. Finalmente, se extrae la política óptima de la función de valor óptima. vease [[Iteración de Valor (value iteration)]]

2. **Iteración de Política (Policy Iteration)**: Este algoritmo comienza con una política arbitraria y luego alterna entre dos pasos: evaluación de la política (calculando la función de valor para la política actual) y mejora de la política (haciendo que la política sea "codiciosa" con respecto a la función de valor actual). Este proceso se repite hasta que la política converge a la política óptima. vease [[Iteración de Política (policy iteration)]]

