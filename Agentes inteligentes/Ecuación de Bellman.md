
La ecuación de Bellman, nombrada en honor a Richard Bellman, es una ecuación fundamental en el aprendizaje por refuerzo. **Proporciona una relación recursiva entre el valor de un estado y los valores de sus estados sucesores.** 

Existen dos formas principales de la ecuación de Bellman: una para la función de valor de estado y otra para la función de valor de acción.

# Ecuación de Bellman para la función de valor de estado

La ecuación de Bellman para la función de valor de estado se puede expresar como:

$$
V^\pi(s) = \sum_{a \in A} \pi(a|s) \sum_{s', r} p(s', r|s, a) [r + \gamma V^\pi(s')]
$$

Esta ecuación dice que el valor esperado del estado actual $s$ bajo la política $\pi$ es la suma esperada de las recompensas inmediatas más el valor esperado de los estados siguientes, donde la expectativa está tomada sobre todas las posibles acciones, recompensas y estados siguientes.

# Ecuación de Bellman para la función de valor de acción

La ecuación de Bellman para la función de valor de acción es similar, pero incorpora una suma adicional sobre todas las acciones siguientes:

$$
Q^\pi(s, a) = \sum_{s', r} p(s', r|s, a) [r + \gamma \sum_{a' \in A} \pi(a'|s') Q^\pi(s', a')]
$$

**Estas ecuaciones son fundamentales para muchos algoritmos en el aprendizaje por refuerzo, ya que proporcionan una forma de "actualizar" los valores de los estados o las acciones a medida que el agente interactúa con su entorno y adquiere más información.**

# Ecuación de Bellman óptima

Hay una variante adicional de la ecuación de Bellman que es fundamental para la búsqueda de la política óptima, conocida como la ecuación de Bellman óptima. En lugar de considerar el valor esperado de las acciones bajo una política específica, la ecuación de Bellman óptima considera el valor máximo que se puede obtener al seleccionar la mejor acción. 

La ecuación de Bellman óptima para la función de valor de estado es:

$$
V^*(s) = \max_{a \in A} \sum_{s', r} p(s', r|s, a) [r + \gamma V^*(s')]
$$

Y la ecuación de Bellman óptima para la función de valor de acción es:

$$
Q^*(s, a) = \sum_{s', r} p(s', r|s, a) [r + \gamma \max_{a' \in A} Q^*(s', a')]
$$

> Para un problema especifico, resolver explıcitamente las ecuaciones de optimalidad de Bellman nos permitirıa encontrar una polıtica optima. 
> Sin embargo, **esta estrategia rara vez es factible**, porque se apoya en tres suposiciones improbables en la practica: 
> (1) conocemos con precisión las dinámicas del ambiente; 
> (2) tenemos suficientes recursos computacionales; 
> (3) el problema cumple con la propiedad de Markov. 
> 
> Por ejemplo, el backgammon cumple (1) y (3), pero no (2). Entonces, tardarıamos miles de anos en computar v∗ y q∗. **En consecuencia, necesitamos resolver en forma aproximada estas ecuaciones, para estimar v∗ y q∗.**

Estas ecuaciones son la base de algoritmos como la [[Iteración de Valor (value iteration)]] y la [[Iteración de Política (policy iteration)]], así como el [[Q-learning]] y los métodos de [[Aprendizaje Profundo por Refuerzo]].

Es importante entender que la ecuación de Bellman es fundamentalmente una ecuación de consistencia que define la relación que debe existir entre el valor de un estado (o un par estado-acción) y el valor de sus sucesores. No es una ecuación que uno resolvería numéricamente para obtener los valores de estado (aunque existen métodos para hacer precisamente eso, como la iteración de valor, que básicamente resuelve la ecuación de Bellman).

Ahora bien, podrías preguntarte, ¿por qué es útil la ecuación de Bellman? Bueno, hay varias razones:

- **Proporciona una relación recursiva para los valores de los estados**: Esto significa que si conocemos los valores de los estados sucesores, podemos calcular el valor del estado actual. Esta propiedad es clave para los algoritmos como la iteración de valor y la iteración de política, que utilizan la ecuación de Bellman para actualizar iterativamente los valores de los estados hasta que converjan al valor verdadero.

- **Permite calcular la política óptima**: Si conocemos la función de valor óptima, podemos usar la ecuación de Bellman para calcular la política óptima simplemente seleccionando en cada estado la acción que maximiza la suma de la recompensa inmediata y el valor del estado sucesor. Esta es la base del algoritmo de iteración de política.

- **Proporciona un objetivo de aprendizaje para los algoritmos de aprendizaje por refuerzo**: En los algoritmos como el Q-learning y los métodos de Aprendizaje Profundo por Refuerzo, la ecuación de Bellman proporciona un objetivo de aprendizaje. Específicamente, estos algoritmos tratan de minimizar la "diferencia temporal" o "error de Bellman", que es la diferencia entre el valor actual de un estado (o par estado-acción) y el valor que se obtendría aplicando la ecuación de Bellman.

Así que en resumen, la ecuación de Bellman es realmente una pieza fundamental en el aprendizaje por refuerzo, y entenderla bien es crucial para entender cómo funcionan los algoritmos en esta área.
