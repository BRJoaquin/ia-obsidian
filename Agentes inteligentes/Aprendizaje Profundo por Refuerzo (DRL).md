El Aprendizaje por Refuerzo Profundo (DRL, por sus siglas en inglés) es una combinación del [[Aprendizaje por refuerzo]] (RL) y el [[Deep Learning]]. Utiliza redes neuronales profundas para representar las funciones de política o de valor que son necesarias para que un agente de RL tome decisiones. 

El RL es una rama del aprendizaje automático que se ocupa de cómo un agente puede aprender a tomar decisiones a partir de interacciones con su entorno. El agente toma acciones, recibe recompensas o castigos (refuerzos) y busca maximizar la suma de las recompensas a lo largo del tiempo. 

Las redes neuronales profundas, por otro lado, son una técnica de aprendizaje automático capaz de aprender representaciones de datos de alta dimensión. Son especialmente útiles para aprender a partir de datos no estructurados o de alta dimensión, como imágenes o texto.

La combinación de RL y aprendizaje profundo permite a los agentes de RL aprender a tomar decisiones en entornos de alta dimensión y/o no estructurados, lo que sería extremadamente difícil, si no imposible, utilizando RL tradicional.

## DRL vs DQN

[[Deep Q-Network (DQN)]] es un ejemplo de un algoritmo DRL. DQN es una forma de aprendizaje Q en la que se utiliza una red neuronal profunda para representar la función Q. Sin embargo, no todos los algoritmos DRL son DQN. 

Hay otros algoritmos DRL que utilizan redes neuronales profundas para representar la política directamente (en lugar de la función Q), como el gradiente de política profunda (DPG) y la política determinista profunda (DDPG). También hay algoritmos que utilizan redes neuronales profundas para modelar el entorno, como los modelos de mundo.

En resumen, DRL es una combinación de RL y aprendizaje profundo que permite a los agentes aprender a tomar decisiones en entornos de alta dimensión y/o no estructurados. DQN es un ejemplo de un algoritmo DRL, pero hay muchos otros.
