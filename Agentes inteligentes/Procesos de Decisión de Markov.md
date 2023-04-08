Un Proceso de Decisión de Markov (MDP, por sus siglas en inglés) es un modelo matemático que describe cómo un [[Agente]] toma decisiones en un [[Entorno]] incierto y dinámico. En términos simples, un MDP es como un juego en el que un jugador (el agente) interactúa con un mundo que cambia y debe tomar decisiones para lograr un objetivo, como ganar puntos o completar una tarea.

El MDP se compone de cuatro elementos principales:

1.  Estados: son las diferentes situaciones o configuraciones en las que puede encontrarse el agente dentro del entorno. Véase [[Estado]]
2.  Acciones: son las posibles decisiones o movimientos que el agente puede realizar en cada estado. Véase [[Acción]]
3.  Transiciones: son las probabilidades de pasar de un estado a otro, dada una acción específica. Véase [[Transición]]
4.  Recompensas: son los puntos o beneficios que el agente recibe al realizar acciones en el entorno. Véase [[Recompensa]]

El agente toma decisiones basándose en su conocimiento actual del entorno y las recompensas asociadas a las acciones. El objetivo del agente es encontrar una política óptima ([[Política#Política optima]]), que es una estrategia para seleccionar acciones en cada estado de manera que maximice el valor total de las recompensas a lo largo del tiempo.

Un aspecto clave de los MDP es que tienen **la propiedad de Markov**, lo que significa que **el estado actual del entorno contiene toda la información necesaria para decidir la acción óptima**, sin importar cómo llegamos a ese estado. En otras palabras, el pasado no importa y sólo necesitamos considerar el estado presente para tomar decisiones.

> [!quote]
> Thus MDPs involve delayed reward and the need to tradeoff immediate and delayed reward.

![[Pasted image 20230408171531.png]]

La notación comúnmente utilizada para representar el conjunto de estados, acciones y recompensas en un problema de aprendizaje por refuerzo es la siguiente:

1.  Estados: El conjunto de todos los posibles estados se denota como $\mathcal{S}$. Cada estado individual dentro de este conjunto se representa como $s$, donde $s \in \mathcal{S}$.

2.  Acciones: El conjunto de todas las posibles acciones se denota como $\mathcal{A}$. Cada acción individual dentro de este conjunto se representa como $a$, donde $a \in \mathcal{A}$.

3.  Recompensas: El conjunto de todas las posibles recompensas se denota como $\mathcal{R}$. Cada recompensa individual dentro de este conjunto se representa como $r$, donde $r \in \mathcal{R}$.
   
> En particular, $\mathcal{R}$ es un conjunto finito de números reales.

En algunos casos, el conjunto de acciones disponibles puede variar según el estado en el que se encuentre el agente. En tales situaciones, se utiliza la notación $\mathcal{A}(s)$ para representar el conjunto de acciones disponibles en el estado $s$.

# Probabilidad condicional

$$p(s', r|s, a) = \text{Pr}({S_t = s', R_t = r | S_{t-1} = s, A_{t-1} = a})$$Representa la probabilidad conjunta de transición y recompensa en un Proceso de Decisión de Markov (MDP). Vamos a desglosar esta notación:

-   $s$: el estado actual en el tiempo $t-1$.
-   $a$: la acción tomada por el agente en el tiempo $t-1$.
-   $s'$: el estado siguiente en el tiempo $t$.
-   $r$: la recompensa recibida al pasar de $s$ a $s'$ tomando la acción $a$.

La expresión $p(s', r|s, a)$ representa la probabilidad de que el agente, estando en el estado $s$ y tomando la acción $a$, llegue al estado siguiente $s'$ y reciba una recompensa $r$. Esta probabilidad se calcula condicionalmente, dadas las variables de estado y acción en el tiempo $t-1$. La notación $\text{Pr}{S_t = s', R_t = r | S_{t-1} = s, A_{t-1} = a}$ es simplemente otra forma de escribir esta [[Probabilidad condicional]].

Esta notación es importante en el estudio de MDP, ya que captura tanto la dinámica del entorno (cómo los estados cambian en función de las acciones tomadas) como la estructura de recompensa (qué recompensas se reciben como resultado de tomar ciertas acciones en ciertos estados). Estos dos aspectos son cruciales para que el agente aprenda a tomar decisiones óptimas y maximizar su recompensa acumulada a lo largo del tiempo.

# 