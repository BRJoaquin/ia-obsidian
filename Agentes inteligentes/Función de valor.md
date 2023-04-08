> [!Quote]
Reinforcement learning is different from supervised learning, the kind of learning studied in most current research in the field of machine learning. Supervised learning is learning from a training set of labeled examples provided by a knowledgable external supervisor.

En el aprendizaje por refuerzo, la función de valor es una función que estima cuánto valor (recompensa acumulada) se espera obtener a partir de un estado específico o una combinación de estado y acción, siguiendo una política dada. La función de valor ayuda al agente a evaluar la calidad de los estados y a decidir qué acciones son más prometedoras para maximizar las recompensas a largo plazo.

Hay dos tipos principales de funciones de valor:

1.  Función de valor de estado (V(s)): Esta función estima el valor esperado de un estado s, asumiendo que el agente sigue una política específica. La función de valor de estado indica cuánta recompensa acumulada se espera obtener a largo plazo a partir de ese estado, tomando decisiones de acuerdo con la política.

2.  Función de valor de acción (Q(s, a)): Esta función estima el valor esperado de realizar una acción a en un estado s y, posteriormente, seguir una política específica. La función de valor de acción indica cuánta recompensa acumulada se espera obtener a largo plazo después de tomar una acción específica en un estado determinado y luego seguir la política.

> [!quote]
> Whereas the reward signal indicates what is good in an immediate sense, a value function specifies what is good in the long run. Roughly speaking, the value of a state is the total amount of reward an agent can expect to accumulate over the future, starting from that state. Whereas rewards determine the immediate, intrinsic desirability of environmental states, values indicate the long-term desirability of states after taking into account the states that are likely to follow and the rewards available in those states.


![[Pasted image 20230404203626.png]]

