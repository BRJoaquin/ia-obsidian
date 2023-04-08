El problema de los bandidos de k brazos (k-armed bandit problem, en inglés) es un problema clásico en el campo del aprendizaje por refuerzo y la teoría de la toma de decisiones. El nombre proviene de la analogía con una máquina tragamonedas (también conocida como "bandido de un brazo"), pero en este caso, la máquina tiene k brazos en lugar de uno solo.

El problema se describe de la siguiente manera: se tiene una máquina con k palancas (brazos) para jalar. Cada vez que se jala una palanca, se obtiene una [[Recompensa]] aleatoria de una distribución específica para esa palanca. Las distribuciones de [[Recompensa]] son diferentes para cada brazo y son desconocidas por el agente. El objetivo es encontrar una estrategia para jalar las palancas de manera que se maximice la [[Recompensa]] acumulada en un número determinado de intentos.

Este problema ilustra el dilema fundamental de la exploración versus la explotación en el aprendizaje por refuerzo:

-   [[Exploración]]: El agente debe jalar diferentes palancas para obtener información sobre las distribuciones de [[Recompensa]] y descubrir cuál es la mejor opción.
-   [[Explotación]]: Una vez que el agente tiene alguna información, debe jalar la palanca que cree que proporcionará la mayor [[Recompensa]] en función de lo que ha aprendido.

El desafío en el problema de los bandidos de k brazos es equilibrar la exploración y la explotación de manera eficiente. Si el agente explora demasiado, pierde oportunidades de obtener [[Recompensa]]s más altas de las palancas que ya ha identificado como buenas. Por otro lado, si el agente explota demasiado pronto, puede perderse mejores opciones que aún no ha descubierto.

Hay varias estrategias y algoritmos para abordar el problema de los bandidos de k brazos, como la regla ε-greedy, la regla de confianza superior (UCB) y el algoritmo de muestreo de Thompson, entre otros. Cada uno de estos enfoques aborda el equilibrio entre exploración y explotación de diferentes maneras, y su rendimiento puede variar según el problema específico y las características de las distribuciones de [[Recompensa]].

> En el caso teórico, es posible que los brazos ofrezcan [[Recompensa]]s positivas en promedio, lo que permitiría ganar a lo largo del tiempo si el agente selecciona correctamente las palancas. La clave en este problema teórico es cómo el agente aprende a tomar decisiones óptimas, equilibrando la exploración y la explotación para maximizar sus ganancias.

> El problema de los K brazos es un problema no asociativo, es decir el agente no necesita aprender a asociar diferentes situaciones o estados del entorno con acciones específicas. En otras palabras, el agente no necesita aprender una [[Política]] que mapee los estados a las acciones, como en el caso de problemas de aprendizaje por refuerzo más generales.


# Funcion valor

La [[Función de valor]] se refiere a la función de valor de acción, ya que no hay estados distintos en este problema y sólo se consideran las acciones (brazos). La función de valor de acción para un bandido multi-brazo, denotada como $Q(a)$, estima el valor esperado de la [[Recompensa]] al seleccionar una acción específica (tirar de un brazo particular).

$$
Q(a) = \mathbb{E}[R_t | A_t = a]
$$
> Donde:
> 1. $Q(a)$: Esta es la función de valor de acción que estima el valor esperado de la [[Recompensa]] al seleccionar una acción específica, en este caso, la acción $a$ (tirar del brazo $a$ en el bandido multi-brazo).
> 2. $\mathbb{E}$: Este es el símbolo matemático que representa la esperanza matemática o el valor esperado. Se utiliza para calcular el promedio ponderado de una variable aleatoria en función de sus probabilidades.
> 3. $R_t$: Esta es la ￼￼Recompensa]] que el agente recibe en el tiempo $t$ después de realizar una acción. Es una variable aleatoria que representa la [[Recompensa]] que se obtiene al seleccionar una acción específica. Su valor puede variar dependiendo de la distribución de [[Recompensa]]s asociada con la acción.
> 4. $A_t$: Esta es la acción que el agente selecciona en el tiempo $t$. En el contexto del problema de los k-bandidos, $A_t$ representa el brazo que el agente elige tirar en el paso $t$.
> 5. $a$: Es una acción específica en el conjunto de acciones disponibles. En el problema de los k-bandidos, corresponde a un brazo particular del bandido multi-brazo.
> 6. El símbolo | indica que estamos calculando el valor esperado de la [[Recompensa]] $R_t$ condicionado al hecho de que el agente ha seleccionado la acción $a$ en el tiempo $t$ (es decir, $A_t = a$). En otras palabras, estamos calculando el valor esperado de la [[Recompensa]] cuando se elige la acción $a$ y se conoce la información sobre la acción seleccionada.
> 
> Entonces, la fórmula nos dice que la función de valor de acción $Q(a)$ es igual al valor esperado de la [[Recompensa]] $R_t​$, dado que el agente seleccionó la acción $a$ (tiró del brazo $a$) en el tiempo $t$.

## Valor optimo

En el contexto del problema de los k-bandidos, $q^*(a)$ representa el valor óptimo de la acción $a$, es decir, el valor esperado de la [[Recompensa]] si se selecciona la acción $a$ (tirar del brazo $a$) y **se conoce la verdadera distribución de** [[Recompensa]]s.

$$
q^*(a) = \mathbb{E}[R_t | A_t = a]
$$

$q^*(a)$ es el valor de acción "verdadero" o "desconocido" que el agente intenta aprender o estimar a través de sus interacciones con el entorno. La función de valor de acción que el agente estima, $Q(a)$, es una aproximación de $q^*(a)$ basada en la experiencia del agente.

**El objetivo del agente es mejorar sus estimaciones de los valores de acción, $Q(a)$, de manera que se aproximen cada vez más a los valores óptimos verdaderos, $q^*(a)$. A medida que el agente explora y explota las acciones en el entorno, sus estimaciones de $Q(a)$ se actualizarán y, en teoría, convergerán a $q^*(a)$.**

# Acción greedy

En el instante $t$, llamamos acción **greedy** a una [[Acción]] a que tiene máximo valor estimado $Q_t(a)$. Y es el caso de la [[Explotación]].

> Observación: Puede haber mas de una acción greedy.


# Métodos Acción-Valor

Los métodos acción-valor estiman $Q_t(a)$ y usan esas estimaciones para seleccionar las acciones a ejecutar. La forma mas sencilla de computar la estimación $Q_t(a)$ es calcular el promedio de recompensas obtenidas al seguir la acción a:

$$Q_t(a) = \frac{\sum_{i=1}^{t-1} R_i \cdot \mathbb{I}(A_i=a)}{\sum_{i=1}^{t-1} \mathbb{I}(A_i=a)}$$
Donde:

-   $Q_t(a)$ es la estimación del valor de la acción $a$ en el tiempo $t$.
-   $R_i$ es la recompensa obtenida en el tiempo $i$.
-   $A_i$ es la acción tomada en el tiempo $i$.
-   $\mathbb{I}(A_i=a)$ es una función indicadora que toma el valor 1 si $A_i=a$, y 0 en caso contrario.
-   La primera suma es sobre todos los tiempos $i$ anteriores a $t$ en los que se tomó la acción $a$.
-   La segunda suma es sobre todos los tiempos $i$ anteriores a $t$ en los que se tomaron acciones.

> Observación: A medida que crece el denominador, $Q_t(a)$ converge a $q^∗(a)$, gracias a la [[Ley de los grandes números]].

> Observación 2: Si el división es 0 entonces $Q_t(a)$ es 0 también.


## Acción greedy

En este caso la acción greedy seria tomar aquella acción que tenga la mayor estimación $Q_t(a)$. Es decir:

$$A_t = \arg\max_a Q_t(a)$$
Donde:

-   $A_t$ es la acción seleccionada en el tiempo $t$.
-   $Q_t(a)$ es el valor estimado de la acción $a$ en el tiempo $t$.
-   $\arg\max_a$ se lee como "el valor de $a$ que maximiza".

En resumen, esta fórmula selecciona la acción $a$ que tiene el mayor valor estimado en el tiempo $t$ como la acción óptima en ese momento.

> En caso de haber mas de una max se puede desempatar de forma aleatoria.


## Épsilon-greedy ($\epsilon$-greedy)

> [!quote]
> Greedy action selection always exploits current knowledge to maximize immediate reward; it spends no time at all sampling apparently inferior actions to see if they might really be better. A simple alternative is to behave greedily most of the time, but every once in a while, say with small probability ", instead select randomly from among all the actions with equal probability, independently of the action-value estimates. We call methods using this near-greedy action selection rule "-greedy methods. An advantage of these methods is that, in the limit as the number of steps increases, every action will be sampled an infinite number of times, thus ensuring that all the $Q_t(a)$ converge to $q^*(a)$. This of course implies that the probability of selecting the optimal action converges to greater than 1 ", that is, to near certainty. These are just asymptotic guarantees, however, and say little about the practical effectiveness of the methods.

Vease: [[Epsilon-greedy]]

# The 10-armed Testbed

The 10-armed Testbed es un problema de prueba comúnmente utilizado para evaluar algoritmos de aprendizaje por refuerzo en el contexto del problema de los k brazos bandidos (multi-armed bandit problem).

![[Pasted image 20230408114224.png]]


1.  Para cada una de las 10 acciones posibles, se selecciona un valor verdadero (o valor óptimo) de forma aleatoria a partir de una distribución normal con media cero y varianza uno. Estos valores verdaderos son desconocidos para el algoritmo de aprendizaje.

> O sea, se elije el $q^*$ al azar para cada uno de los brazos, pero de tal forma que no se alejen mucho del valor 0. Aquellas que tengan un valor optimo menor a cero (2,6,7,8 y 10) son aquellas que a la larga pierdo dinero, mientras que las otras son las que gano dinero. Aquella con mayor valor optimo (3 en este caso) es aquella acción que tengo que encontrar para explotarla lo mas posible (maximizar mis ganancias).

2.  En cada intento, cuando se selecciona una acción, se obtiene una recompensa real a partir de una distribución normal con media igual al valor verdadero de la acción seleccionada y varianza igual a uno. Estas recompensas reales son desconocidas para el algoritmo de aprendizaje y son generadas de forma aleatoria.

> Al ser una [[Recompensa#Estocástica]], esta definida por una distribución normal (podría ser otra) para modelar el problema.

3.  El objetivo del algoritmo de aprendizaje es estimar los valores verdaderos de las 10 acciones a partir de las recompensas obtenidas en los intentos previos. El algoritmo debe equilibrar la exploración de acciones menos probables con la explotación de las acciones más prometedoras, para encontrar el valor verdadero más alto (valor óptimo) en el menor número de intentos posibles.

## Practica 

Llevamos a la practica este ambiente junto a múltiples estrategias / [[Política]]. Se pueden ver los detalles en [[Practico K bandidos armados]]