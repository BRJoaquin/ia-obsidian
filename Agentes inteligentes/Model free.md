Los algoritmos model-free en el aprendizaje por refuerzo son **métodos que no requieren un modelo del entorno para aprender.** Estos métodos **aprenden directamente de la interacción con el entorno**, sin intentar construir un modelo explícito de cómo funcionan las transiciones de estado y las recompensas.

A continuación, se detallan algunos ejemplos de algoritmos model-free:

- Métodos de Monte Carlo

Los [[Métodos Monte Carlo]] estiman el valor esperado de una función de valor mediante el muestreo de trayectorias de experiencias. No intentan modelar explícitamente las dinámicas del entorno.

- Temporal-Difference (TD) Learning

El aprendizaje de [[Métodos de Diferencias temporales]], como TD(0), SARSA y Q-Learning, combina las ideas de los métodos de Monte Carlo y el aprendizaje basado en diferencias para aprender directamente de la experiencia sin un modelo del entorno.

- Policy Gradient Methods

Los métodos de [[Gradiente de Política]], como REINFORCE y Actor-Critic, mejoran la política directamente a través de gradientes de políticas sin necesidad de un modelo del entorno.

- Deep Q-Networks (DQN)

DQN es un algoritmo que combina Q-Learning con redes neuronales profundas para aprender una política óptima directamente de la experiencia cruda sin un modelo del entorno.

- Proximal Policy Optimization (PPO)

PPO es un algoritmo de aprendizaje por refuerzo basado en políticas que mejora las políticas directamente sin la necesidad de un modelo del entorno.

**En general, los algoritmos model-free son más flexibles y más fácilmente aplicables a una amplia gama de problemas de aprendizaje por refuerzo porque no necesitan un modelo preciso del entorno. Sin embargo, pueden ser menos eficientes que los algoritmos model-based porque no utilizan la información sobre las dinámicas del entorno para guiar el aprendizaje.**
