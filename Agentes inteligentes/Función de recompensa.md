
La función de recompensa es un concepto central en el [[Aprendizaje por refuerzo]]. Es una función que proporciona una retroalimentación numérica (la recompensa) a un agente inteligente basándose en las acciones que este realiza en diferentes estados.

La función de recompensa guía al agente en su proceso de aprendizaje. El objetivo de un agente de aprendizaje por refuerzo es aprender a realizar acciones que maximicen la suma total de las recompensas a lo largo del tiempo, es decir, que maximicen la recompensa acumulada.

En términos formales, una función de recompensa es una función R(s, a, s') que devuelve un número real que representa la recompensa inmediata recibida después de transitar del estado s al estado s' debido a la acción a.

**Uno de los principales objetivos de los algoritmos de aprendizaje por refuerzo es estimar de manera efectiva la función de recompensa óptima** y, por tanto, aprender cómo actuar para maximizar la recompensa acumulativa. Sin embargo, es importante destacar que no todos los algoritmos de aprendizaje por refuerzo estiman directamente la función de recompensa. En su lugar, a menudo estiman funciones de valor, que representan el valor esperado a largo plazo de estar en un estado o de tomar una acción en un estado.

Aquí hay dos conceptos relacionados importantes:

- **Función de valor de estado**: Denotada como **V(s)**, es la recompensa total esperada a partir de un estado s, dado que el agente sigue una política específica. [[Función de valor de estado (V)]]
  
- **Función de valor de acción**: También conocida como función **Q**, denotada como Q(s, a), es la recompensa total esperada después de tomar una acción a en un estado s, dado que el agente sigue una política específica después de esa acción. [[Función de valor de acción (Q)]]

Estas funciones de valor son lo que los algoritmos como [[Q-learning]] y [[SARSA]] intentan estimar. Una vez que estas funciones de valor se estiman con precisión, pueden usarse para determinar la política óptima seleccionando la acción que maximiza el valor en cada estado.
