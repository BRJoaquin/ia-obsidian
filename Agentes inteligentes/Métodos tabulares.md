
Los **métodos tabulares** son técnicas utilizadas en el aprendizaje por refuerzo donde se mantiene una **tabla** para representar la función de valor o la política.

En los métodos tabulares, se mantiene una tabla para cada función de valor (V o Q) o política. Cada entrada en la tabla da el valor o la política para un estado (o par estado-acción).

Por ejemplo, para un problema con 10 estados y 2 acciones posibles por estado, podríamos tener una tabla Q con 10 filas y 2 columnas. Cada entrada en la tabla sería el valor Q para el par estado-acción correspondiente.

# Actualización de las Tablas

Las tablas se actualizan a medida que el agente interactúa con el entorno. Por ejemplo, en el método de Q-learning, uno de los métodos tabulares más conocidos, la tabla Q se actualiza utilizando la ecuación de Bellman para Q:

$Q(s, a) = Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$

donde $s$ es el estado actual, $a$ es la acción tomada, $r$ es la recompensa recibida, $s'$ es el nuevo estado, $a'$ son todas las acciones posibles en el estado $s'$, $\alpha$ es la tasa de aprendizaje y $\gamma$ es el factor de descuento.

# Limitaciones de los Métodos Tabulares

Los métodos tabulares son simples y pueden ser muy efectivos, pero tienen limitaciones. En particular, **solo funcionan para problemas con un número pequeño y discreto de estados y acciones**. Para problemas con espacios de estado o acción grandes, continuos o de alta dimensión, se necesitan técnicas más sofisticadas, como [[Métodos de aproximación de la función de valor]] o las [[Redes Neuronales Artificiales]].
