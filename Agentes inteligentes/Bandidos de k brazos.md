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

## Greedy & epsilon-greedy

Este capítulo compara los métodos de acción-valor greedy y ε-greedy en un conjunto de 2000 problemas de bandidos de k brazos (k = 10) generados aleatoriamente. Los valores de acción y las recompensas se seleccionaron utilizando distribuciones normales. Se realizaron 1000 pasos de tiempo para cada problema y se repitió el proceso en 2000 ejecuciones independientes para obtener el comportamiento promedio del algoritmo de aprendizaje.

![[Pasted image 20230408133224.png]]

La Figura 2.2 compara un método greedy con dos métodos ε-greedy (ε = 0.01 y ε = 0.1). El método greedy mostró una mejora inicial más rápida, pero luego se estancó en un nivel inferior en comparación con los métodos ε-greedy. La razón de este estancamiento es que el método greedy a menudo quedaba atrapado en acciones subóptimas. Por otro lado, los métodos ε-greedy continuaron explorando y mejoraron sus posibilidades de reconocer la acción óptima.

La ventaja de los métodos ε-greedy sobre los métodos greedy depende de la tarea. Si la varianza de la recompensa fuera mayor o si el problema fuera no estacionario (es decir, los valores verdaderos de las acciones cambian con el tiempo), los métodos ε-greedy tendrían un mejor rendimiento en comparación con el método greedy. En general, el aprendizaje por refuerzo requiere un equilibrio entre exploración y explotación, y el método ε-greedy es una forma de lograr ese equilibrio en diferentes escenarios.

### ¿Por qué el greedy en la figura 2.2 se queda estancado?

El enfoque greedy queda estancado en el promedio de recompensa debido a su falta de exploración y enfoque en la explotación. Al seleccionar siempre la acción con la recompensa más alta observada hasta ese momento, el método greedy tiende a explotar prematuramente la información limitada que ha adquirido en las primeras etapas.

Si el método greedy selecciona una acción subóptima con una recompensa inicial alta por casualidad, es probable que siga eligiendo esa acción en lugar de explorar otras. Debido a que el método greedy no dedica tiempo a explorar otras acciones, puede perderse la acción óptima si sus muestras iniciales resultaron ser bajas en comparación con las acciones subóptimas.

Esta falta de exploración lleva a que el método greedy quede atrapado en acciones subóptimas, lo que resulta en un estancamiento en el promedio de recompensa en lugar de alcanzar el máximo posible. Por otro lado, los métodos ε-greedy equilibran la exploración y la explotación, lo que les permite descubrir y aprovechar las acciones óptimas a lo largo del tiempo y alcanzar un rendimiento más cercano al óptimo.

> Cabe mencionar que este valor es específico para el conjunto de problemas de prueba utilizado en el estudio y no es una constante universal para todos los problemas de bandidos de k brazos. En otros problemas, el mejor promedio de recompensa posible podría ser diferente, dependiendo de las distribuciones de recompensa y las características del problema.

El estancamiento del método greedy en el porcentaje de acción óptima se debe a su falta de exploración y enfoque en la explotación. Al seleccionar siempre la acción con la recompensa más alta observada hasta ese momento, el método greedy tiende a explotar prematuramente la información limitada que ha adquirido en las primeras etapas.

Esta falta de exploración lleva a que el método greedy quede atrapado en acciones subóptimas y no encuentre la acción óptima en una proporción significativa de las tareas. Por lo tanto, el porcentaje de acción óptima para el método greedy se estanca en un nivel inferior al que podrían alcanzar los métodos ε-greedy, que equilibran la exploración y la explotación y continúan buscando la acción óptima durante todo el proceso de aprendizaje.

## Implementación incremental

La implementación incremental es una forma eficiente de actualizar estimaciones de valores de acción en algoritmos de aprendizaje por refuerzo. En lugar de re-calcular la media de todas las recompensas observadas, la implementación incremental utiliza una fórmula recursiva para actualizar la estimación en cada paso:

$$Q_{n+1}(a) = Q_n(a) + \frac{1}{n+1} [R_{n+1} - Q_n(a)]$$

Aquí, $Q_n(a)$ es la estimación del valor de acción $a$ después de $n$ observaciones, y $R_{n+1}$ es la recompensa observada en el paso $n+1$. Esta fórmula ajusta la estimación actual de $Q_n(a)$ en función de la diferencia entre la última recompensa observada y la estimación actual, ponderada por la fracción $\frac{1}{n+1}$. La implementación incremental es computacionalmente eficiente y evita el almacenamiento de todas las recompensas anteriores.

## Pseudo-código

1.  Inicializar, para cada $a = 1, \dots, k$:
    -   $Q(a) \leftarrow 0$
    -   $N(a) \leftarrow 0$
2.  Repetir:
    -   $$A \leftarrow \begin{cases} 
      \text{una acción al azar} & \text{con probabilidad } \epsilon \\ \underset{a}{\operatorname{argmax} Q(a)} & \text{con probabilidad } 1 - \epsilon \end{cases}$$
    -   $R \leftarrow \text{bandido}(A)$
    -   $N(A) \leftarrow N(A) + 1$
    -   $Q(A) \leftarrow Q(A) + \frac{1}{N(A)} [R - Q(A)]$

### Problemas no estacionarios

El problema de los k-bandidos como lo venimos planteando es un problema estacionario. Es decir su función de valor-acción no cambia con el tiempo (steps). Por lo cual vale la pena mencionar que ocurre en otros problemas no estacionarios que queramos 

> Para ilustrar un problema de k-bandidos no estacionario, considera un conjunto de 10 máquinas tragamonedas (k = 10) en un casino. Al principio, cada máquina tiene una distribución de recompensa diferente asociada con ella. A medida que pasa el tiempo, el casino decide cambiar las probabilidades de las máquinas para mantener a los jugadores interesados y ajustar sus ganancias. Estos cambios pueden ser graduales o repentinos, pero el resultado es que las distribuciones de recompensa de las máquinas cambian con el tiempo, y el algoritmo de aprendizaje por refuerzo debe adaptarse a estos cambios.

Para problemas no estacionarios (ver [[Recompensa#Estacionaria]]), las propiedades del entorno cambian con el tiempo. Para aplicar el algoritmo ε-greedy en tales problemas, es necesario adaptar el algoritmo para responder a estos cambios y actualizar las estimaciones de manera más sensible. Una forma de hacerlo es mediante el uso de un **promedio ponderado** en lugar de un promedio simple para actualizar las estimaciones de los valores de acción.

En lugar de usar la fórmula de actualización de la implementación incremental estándar:

$$Q_{n+1}(a) = Q_n(a) + \frac{1}{n+1} [R_{n+1} - Q_n(a)]$$

Usamos un promedio ponderado con un factor de descuento $\alpha$:

$$Q_{n+1}(a) = Q_n(a) + \alpha [R_{n+1} - Q_n(a)]$$

Aquí, $\alpha$ es un parámetro en el rango (0, 1] que determina qué tan rápido el agente olvida las recompensas pasadas y se adapta a los cambios en el entorno. Un valor de $\alpha$ más cercano a 1 hará que el agente se adapte más rápidamente a los cambios, pero también lo hará más sensible al ruido en las recompensas.

> Es importante que el agente siga explorando para adaptarse a los cambios en las recompensas. Los métodos de aprendizaje por refuerzo que son adecuados para problemas estacionarios, como el promedio simple, pueden no ser lo suficientemente sensibles a los cambios en un problema no estacionario.

## Valores iniciales optimistas

Vease: [[Valores Iniciales Optimistas]]

> [!quote]
> Initial action values can also be used as a simple way to encourage exploration. Suppose that instead of setting the initial action values to zero, as we did in the 10-armed testbed, we set them all to +5. Recall that the q⇤(a) in this problem are selected from a normal distribution with mean 0 and variance 1. An initial estimate of +5 is thus wildly optimistic. But this optimism encourages action-value methods to explore. Whichever actions are initially selected, the reward is less than the starting estimates; the learner switches to other actions, being “disappointed” with the rewards it is receiving. The result is that all actions are tried several times before the value estimates converge. The system does a fair amount of exploration even if greedy actions are selected all the time.


> La idea principal es fomentar la exploración inicial engañado con una estimación optimista. De esta manera explorara incluso habiendo usado la mejor acción varias veces.


![[Pasted image 20230408150213.png]]

El libro compara greedy con valores iniciales optimistas (+5) con un un $\epsilon$-greedy sin valores iniciales optimistas.

Dentro de las primeras ~100 steps vemos que performa peor el greedy pero es porque se fomenta mucho la exploración en etapas tempranas.

> [!warning]
> El uso de valores iniciales optimistas es una técnica sencilla que puede ser efectiva en problemas estacionarios, pero no es un enfoque útil para fomentar la exploración en general. Además, no es adecuado para problemas no estacionarios, ya que su impulso para la exploración es temporal. Si la tarea cambia, este método no puede ayudar.

![[Pasted image 20230408151355.png]]


## UCB

Vease: [[Límite Superior de Confianza (UCB)]]

En el caso de los k-brazos bandidos, el algoritmo UCB (Upper Confidence Bound) utiliza un término de bonificación para fomentar la exploración de las acciones menos seleccionadas. La selección de acciones se realiza mediante la fórmula:

$$A_t = argmax_{a} \bigg[Q_t(a) + c\sqrt{\frac{\ln t}{N_t(a)}}\bigg]$$

Donde $Q_t(a)$ es la estimación del valor de la acción a en el tiempo t, $N_t(a)$ es el número de veces que la acción a ha sido seleccionada hasta el tiempo t, y $c$ es un parámetro que controla la cantidad de exploración.

La fórmula utiliza un término de bonificación $c\sqrt{\frac{\ln t}{N_t(a)}}$ que se suma a la estimación $Q_t(a)$ para cada acción a. Este término refleja la incertidumbre en la estimación de la recompensa de la acción a y se hace más grande cuanto menos veces se ha seleccionado la acción. El parámetro $c$ controla la cantidad de exploración, ya que si se elige un valor más alto, se favorecerá la selección de acciones menos exploradas.

En el contexto de los k-brazos bandidos, el algoritmo UCB ha demostrado ser efectivo para equilibrar la exploración y la explotación de los brazos, permitiendo una convergencia rápida a la acción óptima. **Sin embargo, su rendimiento puede verse afectado en problemas no estacionario**s, donde la recompensa de los brazos puede cambiar con el tiempo.

![[Pasted image 20230408154654.png]]

Si la constante C en la fórmula de UCB es muy baja, el algoritmo UCB tenderá a explotar los brazos que han sido seleccionados con frecuencia en lugar de explorar otros brazos que no han sido seleccionados con tanta frecuencia. Esto puede llevar a una convergencia prematura a una suboptimalidad local.

> Puede parecer greedy

Por otro lado, si la constante C es muy alta, el algoritmo UCB se centrará demasiado en la exploración en lugar de explotar los brazos que ya han sido seleccionados con éxito. Esto puede llevar a un exceso de exploración y una convergencia lenta a la óptima.

Por lo tanto, es importante elegir cuidadosamente el valor de C para equilibrar la exploración y la explotación en un problema de aprendizaje por refuerzo. La elección de C dependerá de las características específicas del problema y puede requerir experimentación y ajuste.

## Comparación de metodos 

