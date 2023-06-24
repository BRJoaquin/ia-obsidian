
En el [[Aprendizaje por refuerzo]], off-policy se refiere a métodos de aprendizaje que pueden aprender sobre la [[Política]] óptima independientemente de la política que el agente esté siguiendo actualmente. En otras palabras, estos métodos pueden aprender a partir de las experiencias pasadas o de las experiencias de otros agentes.

Por ejemplo, en el caso del algoritmo Q-learning, el agente puede aprender la política óptima mediante la exploración de diferentes acciones y estados, incluso si estas acciones y estados no forman parte de la política que está siguiendo actualmente. Esto permite que el agente aprenda de una gama más amplia de experiencias y, en teoría, puede ayudarlo a encontrar una política óptima más rápidamente.

Contrástese esto con los métodos "en política" (on-policy), como SARSA, donde el agente solo aprende a partir de las acciones que forman parte de su política actual.
