Q-Learning es uno de los algoritmos más populares y fundamentales en el campo del [[Aprendizaje por refuerzo]]. Es un [[Métodos de Diferencias temporales]] que busca aprender la [[Función de valor]] de acción óptima, Q*, **sin requerir un modelo del entorno**. Q-Learning es un método "**off-policy**", lo que significa que busca aprender la política óptima **independientemente** de la política que sigue el agente para seleccionar las acciones.

# Concepto general

El objetivo de Q-Learning es aprender una política que maximice la suma total de las recompensas futuras([[Control]]. Para esto, define una función Q que asigna un par estado-acción a un número real, interpretado como el valor esperado de seguir una política fija después de ver algún estado y tomar una acción.

La función Q se actualiza de acuerdo con la siguiente regla:

$$\Large
Q(s,a) ← Q(s,a) + α [r + γ max_a' Q(s',a') - Q(s,a)]
$$

donde:
- `α` es la tasa de aprendizaje.
- `r` es la recompensa recibida después de tomar la acción `a` en el estado `s`.
- `γ` es el factor de descuento, que determina cuánto valoramos las recompensas futuras en comparación con las inmediatas.
-  $max_aQ(s',a')$ es el valor máximo posible en el siguiente estado `s'`.

# Algoritmo

![[Pasted image 20230625112411.png]]

# Por que es off-policy?

Esto se logra a través del uso de la función `max` en la actualización de los valores Q. El agente selecciona la acción con el valor Q más alto para la siguiente actualización, **independientemente** de la acción que eligió bajo su política actual.

Esto es diferente del aprendizaje on-policy, donde las actualizaciones de los valores Q dependen de las acciones seleccionadas por la política actual del agente.

En Q-Learning, la elección de la acción a tomar en un estado particular (la política que sigue el agente) puede ser una política ε-greedy o cualquier otra política. Por ejemplo, con ε-greedy, el agente normalmente elige la acción con el valor Q más alto, pero de vez en cuando (con una pequeña probabilidad ε), elige una acción aleatoria para explorar el entorno.

Sin embargo, cuando se actualiza el valor de Q en Q-Learning, **se hace de manera greedy** con respecto a la política futura. Independientemente de cómo se seleccionó la acción en el estado actual, la actualización del valor Q siempre considera la acción que maximizaría el valor Q en el siguiente estado. Es por eso que decimos que Q-Learning es un algoritmo off-policy, ya que la política de actualización de Q (greedy) puede ser diferente de la política de selección de acciones del agente (ε-greedy, por ejemplo).

# Ventajas y desventajas

El Q-Learning tiene varias ventajas. En primer lugar, es un método [[Model free]], lo que significa que no necesita un modelo preciso del entorno para aprender. En segundo lugar, es [[Off-policy]], lo que significa que puede aprender la política óptima mientras sigue otra política, **lo que lo hace muy flexible**.

Sin embargo, el Q-Learning también tiene desventajas. Por ejemplo, **puede ser muy lento para converger**, especialmente en entornos con muchos estados y acciones. Además, aunque teóricamente puede aprender la política óptima, en la **práctica a menudo necesita un número muy grande de episodios para hacerlo**.

Un desafío en el Q-learning es que la tabla Q puede volverse muy grande si hay muchos estados o acciones posibles, lo que puede dificultar el almacenamiento y la actualización de la tabla. Para manejar este problema, se pueden utilizar métodos de aproximación de funciones, como las redes neuronales, para representar la función Q. Esto se conoce como Q-learning profundo, que es la base de muchas técnicas modernas de aprendizaje por refuerzo, como el [[Deep Q-Network (DQN)]].

# Double Q-learning

Double Q-learning es una mejora del algoritmo de Q-learning estándar, que fue propuesto para abordar un problema de sobreestimación en Q-learning. En el Q-learning, se utilizan los valores Q estimados para seleccionar tanto la mejor acción como para calcular la recompensa estimada de esa acción. **Este procedimiento puede llevar a sobreestimaciones sistemáticas de los valores Q, lo que a su vez puede conducir a una política subóptima**.

El problema de sobreestimación en Q-learning se produce debido a la forma en que se actualizan los valores Q. En cada paso, el Q-learning estima la recompensa futura para una acción utilizando el máximo valor Q entre todas las acciones posibles en el próximo estado. Si las estimaciones de los valores Q tienen algún error, y en la práctica a menudo lo tienen, especialmente al principio del proceso de aprendizaje, tomar el máximo sobreestima sistemáticamente el verdadero valor Q. Esto puede llevar a una política subóptima porque el agente puede preferir acciones que tienen estimaciones de valor Q sobreestimadas.

El Double Q-learning intenta solucionar este problema al **desacoplar la selección de acciones de la estimación de la recompensa de la acción**. Para hacer esto, se utilizan dos redes de Q-learning independientes. **Una red se utiliza para determinar la mejor acción para un estado dado (esta es la acción que maximiza el valor Q estimado), y luego la otra red se utiliza para estimar la recompensa de tomar esa acción**. Al alternar entre las dos redes durante el proceso de aprendizaje, se puede reducir la sobreestimación de los valores Q.

Aquí está la fórmula de actualización para el Double Q-learning:

$$\large
Q1(s, a) = Q1(s, a) + α * [r + γ * Q2(s', argmax_a Q1(s', a)) - Q1(s, a)]
$$

Donde:

- Q1 y Q2 son las dos funciones de valor de acción (una para cada red Q-learning)
- s y a son el estado y la acción actuales
- s' es el estado después de tomar la acción a
- r es la recompensa recibida después de tomar la acción a
- argmax_a Q1(s', a) es la acción que maximiza el valor Q según la primera red para el estado s'
- α es la tasa de aprendizaje
- γ es el factor de descuento
  
> [!warning]
> Se van alternando es su actualización

De esta manera, la actualización de los valores Q está desacoplada, lo que puede resultar en una convergencia más estable y una política más óptima en comparación con el Q-learning estándar. La técnica de Double Q-learning ha demostrado ser eficaz en una variedad de tareas y es una de las técnicas utilizadas en el algoritmo de Deep Q-Networks (DQN) que logró un rendimiento superhumano en muchos juegos de Atari.


# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/AJiG3ykOxmY?start=1142" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>