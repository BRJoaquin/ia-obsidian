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
$$\Large p(s', r|s, a) = \text{Pr}({S_t = s', R_t = r | S_{t-1} = s, A_{t-1} = a})$$Representa la probabilidad conjunta de transición y recompensa en un Proceso de Decisión de Markov (MDP). Vamos a desglosar esta notación:

-   $s$: el estado actual en el tiempo $t-1$.
-   $a$: la acción tomada por el agente en el tiempo $t-1$.
-   $s'$: el estado siguiente en el tiempo $t$.
-   $r$: la recompensa recibida al pasar de $s$ a $s'$ tomando la acción $a$.

La expresión $p(s', r|s, a)$ representa la probabilidad de que el agente, estando en el estado $s$ y tomando la acción $a$, llegue al estado siguiente $s'$ y reciba una recompensa $r$. Esta probabilidad se calcula condicionalmente, dadas las variables de estado y acción en el tiempo $t-1$. La notación $\text{Pr}{S_t = s', R_t = r | S_{t-1} = s, A_{t-1} = a}$ es simplemente otra forma de escribir esta [[Probabilidad condicional]].

Esta notación es importante en el estudio de MDP, ya que captura tanto la dinámica del entorno (cómo los estados cambian en función de las acciones tomadas) como la estructura de recompensa (qué recompensas se reciben como resultado de tomar ciertas acciones en ciertos estados). Estos dos aspectos son cruciales para que el agente aprenda a tomar decisiones óptimas y maximizar su recompensa acumulada a lo largo del tiempo.

# Normalización

La expresión que has proporcionado es un requisito de normalización para las probabilidades de transición y recompensa en un Proceso de Decisión de Markov (MDP). La expresión establece que la suma de todas las probabilidades de transición y recompensa para cada estado y recompensa posibles debe ser igual a 1. A continuación, desgloso la expresión:

$$\Large\sum_{s' \in \mathcal{S}}\sum_{r \in \mathcal{R}}p(s', r|s, a) = 1$$
-   $\sum_{s' \in \mathcal{S}}$: esta es una suma sobre todos los estados posibles $s'$. Estamos sumando las probabilidades para cada estado siguiente $s'$.
-   $\sum_{r \in \mathcal{R}}$: esta es una suma sobre todas las recompensas posibles $r$. Estamos sumando las probabilidades para cada recompensa $r$.
-   $p(s', r|s, a)$: esto representa la probabilidad conjunta de transición y recompensa de estar en el estado $s$, tomar la acción $a$, llegar al estado siguiente $s'$ y recibir una recompensa $r$.

La expresión completa garantiza que las probabilidades de todas las combinaciones posibles de estados siguientes y recompensas sumen 1, dada una combinación específica de estado actual y acción. **Esta es una condición necesaria para que las probabilidades sean válidas y bien definidas en un MDP**.

# Otras probabilidades

## Probabilidades de transición de estados

Estas probabilidades describen cómo el entorno cambia de un estado a otro dada una acción específica. Se denotan como $p(s'|s, a)$, que representa la probabilidad de pasar del estado $s$ al estado $s'$ al realizar la acción $a$. Estas probabilidades son fundamentales en el MDP, ya que caracterizan la dinámica del entorno y cómo este responde a las acciones del agente.
$$\Large p(s'|s, a) = \text{Pr}({S_t = s' | S_{t-1} = s, A_{t-1} = a}) = \sum_{r \in \mathcal{R}}p(s', r|s, a)$$
> Básicamente, que probabilidad tengo que estando en el estado $s$ y haciendo la acción $a$ termine en $s'$

> [!question]
> **¿Que pasa si las transiciones son determinısticas?**
> En un problema determinístico, cada acción en un estado particular siempre llevará al agente al mismo estado siguiente. No hay incertidumbre en la transición. En este caso, las probabilidades de transición se vuelven 1 para el estado siguiente y 0 para todos los demás estados. La notación para esto sería:
> $$ p(s' | s, a) = \begin{cases} 1, & \text{si } s' \text{ es el estado siguiente determinado por } (s, a) \\ 0, & \text{en cualquier otro caso} \end{cases} $$

## Recompensas esperadas para pares estado-acción

Las recompensas esperadas para los pares estado-acción se denotan como 
$$\Large r(s, a) = \mathbb{E}[R_t | S_{t-1} = s, A_{t-1} = a] = \sum_{r \in \mathcal{R}}r\sum_{s' \in \mathcal{S}}p(s', r|s, a)$$Esta expresión representa la recompensa promedio que se espera recibir cuando se toma la acción $a$ estando en el estado $s$. Estos valores ayudan al agente a determinar qué acciones son preferibles en un estado dado para maximizar las recompensas a lo largo del tiempo.

> [!question]
> **¿Que pasa si las transiciones son determinısticas?**
> En un problema determinístico, la recompensa para un par estado-acción específico es siempre la misma, ya que no hay incertidumbre en la recompensa. Esto significa que la recompensa esperada para un par estado-acción es simplemente la recompensa fija asociada con ese par. La notación para esto sería:
> $$
r(s, a) = r_{fija}(s, a)
$$


# Episodios

Un episodio es una secuencia finita de interacciones entre un agente y su entorno. Un episodio comienza en un estado inicial y termina cuando el agente alcanza un estado terminal o se cumple cierta condición, como alcanzar un límite de tiempo o un número máximo de pasos. Los problemas de aprendizaje por refuerzo se pueden categorizar en dos tipos: episódicos y continuos. En los problemas episódicos, las interacciones ocurren en episodios **separados** y **discretos**, mientras que en los problemas **continuos**, las interacciones no tienen un punto final claro y pueden extenderse indefinidamente.



# Retorno

El retorno es una medida del **valor acumulado** de las recompensas que un agente recibe durante un **episodio**. El objetivo del agente en el aprendizaje por refuerzo es maximizar este retorno. En muchos casos, se utiliza un **factor de descuento**, denotado como $\gamma$, para darle más peso a las recompensas inmediatas en comparación con las recompensas futuras. El retorno en el tiempo $t$, denotado como $G_t$, se calcula como:

$$ \Large
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$
## En problemas continuos

En problemas continuos de aprendizaje por refuerzo, las interacciones entre el agente y el entorno no se dividen en episodios separados y discretos, sino que se extienden indefinidamente en el tiempo. En tales casos, el concepto de retorno también se aplica, pero se debe tener cuidado al elegir el factor de descuento $\gamma$.

El retorno en el tiempo $t$ en un problema continuo se calcula de manera similar al caso episódico:
$$\Large
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$


# Factor de descuento

El factor de descuento $\gamma$ (gamma) es un número entre 0 y 1. Si $\gamma = 0$, el agente solo considera las recompensas inmediatas y no tiene en cuenta las recompensas futuras. Si $\gamma = 1$, el agente considera todas las recompensas futuras por igual y busca maximizar el retorno total a lo largo del tiempo. **Valores intermedios de $\gamma$ permiten al agente equilibrar la importancia de las recompensas inmediatas y futuras.**
