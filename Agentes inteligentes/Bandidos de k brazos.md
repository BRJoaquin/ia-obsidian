El problema de los bandidos de k brazos (k-armed bandit problem, en inglés) es un problema clásico en el campo del aprendizaje por refuerzo y la teoría de la toma de decisiones. El nombre proviene de la analogía con una máquina tragamonedas (también conocida como "bandido de un brazo"), pero en este caso, la máquina tiene k brazos en lugar de uno solo.

El problema se describe de la siguiente manera: se tiene una máquina con k palancas (brazos) para jalar. Cada vez que se jala una palanca, se obtiene una recompensa aleatoria de una distribución específica para esa palanca. Las distribuciones de recompensa son diferentes para cada brazo y son desconocidas por el agente. El objetivo es encontrar una estrategia para jalar las palancas de manera que se maximice la recompensa acumulada en un número determinado de intentos.

Este problema ilustra el dilema fundamental de la exploración versus la explotación en el aprendizaje por refuerzo:

-   [[Exploración]]: El agente debe jalar diferentes palancas para obtener información sobre las distribuciones de recompensa y descubrir cuál es la mejor opción.
-   [[Explotación]]: Una vez que el agente tiene alguna información, debe jalar la palanca que cree que proporcionará la mayor recompensa en función de lo que ha aprendido.

El desafío en el problema de los bandidos de k brazos es equilibrar la exploración y la explotación de manera eficiente. Si el agente explora demasiado, pierde oportunidades de obtener recompensas más altas de las palancas que ya ha identificado como buenas. Por otro lado, si el agente explota demasiado pronto, puede perderse mejores opciones que aún no ha descubierto.

Hay varias estrategias y algoritmos para abordar el problema de los bandidos de k brazos, como la regla ε-greedy, la regla de confianza superior (UCB) y el algoritmo de muestreo de Thompson, entre otros. Cada uno de estos enfoques aborda el equilibrio entre exploración y explotación de diferentes maneras, y su rendimiento puede variar según el problema específico y las características de las distribuciones de recompensa.

> En el caso teórico, es posible que los brazos ofrezcan recompensas positivas en promedio, lo que permitiría ganar a lo largo del tiempo si el agente selecciona correctamente las palancas. La clave en este problema teórico es cómo el agente aprende a tomar decisiones óptimas, equilibrando la exploración y la explotación para maximizar sus ganancias.

> El problema de los K brazos es un problema no asociativo, es decir el agente no necesita aprender a asociar diferentes situaciones o estados del entorno con acciones específicas. En otras palabras, el agente no necesita aprender una política que mapee los estados a las acciones, como en el caso de problemas de aprendizaje por refuerzo más generales.


# Funcion valor

La función de valor se refiere a la función de valor de acción, ya que no hay estados distintos en este problema y sólo se consideran las acciones (brazos). La función de valor de acción para un bandido multi-brazo, denotada como $Q(a)$, estima el valor esperado de la recompensa al seleccionar una acción específica (tirar de un brazo particular).

$$
Q(a) = \mathbb{E}[R_t | A_t = a]
$$
> Donde:
> 1. `$Q(a)$`: Esta es la función de valor de acción que estima el valor esperado de la recompensa al seleccionar una acción específica, en este caso, la acción `$a$` (tirar del brazo `$a$` en el bandido multi-brazo).
> 2. `$\mathbb{E}$`: Este es el símbolo matemático que representa la esperanza matemática o el valor esperado. Se utiliza para calcular el promedio ponderado de una variable aleatoria en función de sus probabilidades.
> 3. `$R_t$`: Esta es la recompensa que el agente recibe en el tiempo `$t$` después de realizar una acción. Es una variable aleatoria que representa la recompensa que se obtiene al seleccionar una acción específica. Su valor puede variar dependiendo de la distribución de recompensas asociada con la acción.
> 4. `$A_t$`: Esta es la acción que el agente selecciona en el tiempo `$t$`. En el contexto del problema de los k-bandidos, `$A_t$` representa el brazo que el agente elige tirar en el paso `$t$`.
> 5. `$a$`: Es una acción específica en el conjunto de acciones disponibles. En el problema de los k-bandidos, corresponde a un brazo particular del bandido multi-brazo.
> 6. El símbolo `|` indica que estamos calculando el valor esperado de la recompensa `$R_t$` condicionado al hecho de que el agente ha seleccionado la acción `$a$` en el tiempo `$t$` (es decir, `$A_t = a$`). En otras palabras, estamos calculando el valor esperado de la recompensa cuando se elige la acción `$a$` y se conoce la información sobre la acción seleccionada.
> 
> Entonces, la fórmula �(�)=�[��∣��=�]Q(a)=E[Rt​∣At​=a] nos dice que la función de valor de acción �(�)Q(a) es igual al valor esperado de la recompensa ��Rt​, dado que el agente seleccionó la acción �a (tiró del brazo �a) en el tiempo �t.
