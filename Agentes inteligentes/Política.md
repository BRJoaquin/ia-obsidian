En el contexto del aprendizaje por refuerzo, una política (también conocida como estrategia) es un conjunto de reglas o una función que define cómo el agente toma decisiones y elige acciones en diferentes estados del entorno. La política puede ser determinista o estocástica.

-   Política determinista: En este caso, la política asigna una acción específica para cada estado del entorno. Dado un estado, la política determinista siempre producirá la misma acción.

-   Política estocástica: En este caso, la política asigna una probabilidad a cada acción en cada estado del entorno. Dado un estado, la política estocástica selecciona una acción según las probabilidades asignadas a las acciones para ese estado en particular.

El objetivo en el aprendizaje por refuerzo es aprender una política óptima que maximice la recompensa acumulada a lo largo del tiempo. A medida que el agente interactúa con el entorno y adquiere experiencia, ajusta su política para mejorar su capacidad para tomar decisiones y alcanzar sus objetivos.

> [!quote]
> A policy defines the learning agent’s way of behaving at a given time. Roughly speaking, a policy is a mapping from perceived states of the environment to actions to be taken when in those states. It corresponds to what in psychology would be called a set of stimulus–response rules or associations. In some cases the policy may be a simple function or lookup table, whereas in others it may involve extensive computation such as a search process. The policy is the core of a reinforcement learning agent in the sense that it alone is sucient to determine behavior. In general, policies may be stochastic, specifying probabilities for each action

