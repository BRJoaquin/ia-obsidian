  
SARSA (State-Action-Reward-State-Action) es un algoritmo de [[Aprendizaje por refuerzo]] basado en métodos de [[Métodos de Diferencias temporales]]. Es un método de control [[On-Policy]], lo que significa que la misma [[[Política]]] (o conjunto de reglas que decide qué acciones tomar en cada estado) que se está mejorando también es la política que se utiliza para decidir qué acción tomar mientras se aprende.

El algoritmo SARSA se llama así porque los cinco componentes principales del algoritmo son:

- Estado actual (S)
- Acción tomada (A)
- Recompensa recibida (R)
- Estado siguiente (S')
- Acción siguiente (A')

En el aprendizaje por refuerzo, el objetivo es aprender una política óptima que maximice la suma de las recompensas a lo largo del tiempo. Para hacer esto, necesitamos aprender una función de valor que asigne a cada par estado-acción (s, a) un valor que representa la recompensa esperada a largo plazo por tomar la acción a en el estado s y luego seguir la política.

El algoritmo SARSA actualiza la función de valor Q(s, a) basándose en la diferencia temporal entre las recompensas estimadas en el estado actual y en el siguiente estado. Este proceso de actualización se puede representar de la siguiente manera:

Q(s, a) <- Q(s, a) + α [R + γQ(s', a') - Q(s, a)]

Donde:

- Q(s, a) es la estimación actual del valor del par estado-acción (s, a)
- R es la recompensa recibida al pasar del estado s al estado s' al tomar la acción a.
- γ es el factor de descuento, que determina cuánto valoramos las recompensas futuras en comparación con las recompensas inmediatas.
- α es la tasa de aprendizaje, que determina cuánto del error de la estimación (la diferencia temporal) utilizamos para actualizar el valor de Q(s, a).
- Q(s', a') es el valor de la siguiente acción-estado par que seguirá la política.

Las diferencias temporales en el contexto de SARSA representan la discrepancia entre las estimaciones de recompensa actual y las estimaciones futuras. Estas diferencias se utilizan para actualizar y, con suerte, mejorar la función de valor Q.

A diferencia de otros métodos como Q-Learning (un método de control off-policy), SARSA toma una acción de acuerdo con la política actual en el estado siguiente (s') antes de realizar la actualización, lo que significa que la actualización tiene en cuenta la acción que realmente se llevará a cabo en el siguiente paso. Esto puede hacer que SARSA sea más seguro para usar en situaciones en las que tomar la acción óptima podría tener consecuencias peligrosas si la estimación de la función de valor es incorrecta.