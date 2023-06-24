
Los métodos action-value, también conocidos como métodos de valor de acción, son una categoría de algoritmos en el  [[Aprendizaje por refuerzo]] que estiman el valor de cada [[Acción]] que un [[Agente]] puede tomar en cada estado. El valor de una acción es la recompensa total esperada a largo plazo que un agente puede obtener tomando esa acción en un estado particular, y luego siguiendo una política determinada.

Estos métodos se utilizan para resolver problemas de decisión secuencial, donde un agente tiene que tomar una serie de decisiones con el objetivo de maximizar su recompensa total. Los métodos action-value forman la base de muchos algoritmos de aprendizaje por refuerzo, incluyendo:

- [[Q-learning]]
- [[SARSA]] (State-Action-Reward-State-Action)
- [[Deep Q-Networks (DQN)]]

Cada uno de estos algoritmos tiene sus propias ventajas y desventajas, y se utilizan en diferentes tipos de problemas. En las siguientes secciones, discutiremos cada uno de estos métodos en detalle.


## Q-Learning

El Q-learning es un método action-value que se utiliza para encontrar una política óptima en un [[Proceso de decisión de Markov (MDP)]]. Este método utiliza una función de valor de acción Q que le permite al agente aprender a tomar decisiones óptimas sin requerir un modelo del entorno. Uno de los aspectos clave del Q-learning es que es un método "fuera de la política", lo que significa que puede aprender la política óptima independientemente de la política que está siguiendo el agente.

## SARSA (State-Action-Reward-State-Action)

SARSA es un algoritmo de control on-policy para el aprendizaje por refuerzo. A diferencia del Q-learning, SARSA es un método "en la política", lo que significa que el agente aprende el valor de la política que está siguiendo actualmente. Una característica importante de SARSA es que tiene en cuenta tanto el estado y la acción actuales (S, A) como el siguiente estado y la siguiente acción (S', A') en su actualización.

## Deep Q-Networks (DQN)

Las redes profundas de Q (DQN) son una extensión del Q-learning que utiliza redes neuronales profundas para aproximar la función de valor de acción Q. Las DQN pueden manejar entornos con un gran número de estados que serían inmanejables para los métodos de tabla Q tradicionales. DQN fue el algoritmo que DeepMind utilizó para alcanzar el rendimiento humano en una amplia gama de juegos de Atari solo a partir de la entrada de píxeles en bruto.
