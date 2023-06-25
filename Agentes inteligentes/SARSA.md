  
SARSA (State-Action-Reward-State-Action) es un algoritmo de [[Aprendizaje por refuerzo]] basado en métodos de [[Métodos de Diferencias temporales]]. Es un método de control [[On-Policy]], lo que significa que la misma [[Política]] (o conjunto de reglas que decide qué acciones tomar en cada estado) que se está mejorando también es la política que se utiliza para decidir qué acción tomar mientras se aprende.

El algoritmo SARSA se llama así porque los cinco componentes principales del algoritmo son:

- Estado actual (S)
- Acción tomada (A)
- Recompensa recibida (R)
- Estado siguiente (S')
- Acción siguiente (A')

En el aprendizaje por refuerzo, el objetivo es aprender una política óptima ([[Control]]) que maximice la suma de las recompensas a lo largo del tiempo. Para hacer esto, necesitamos aprender una función de valor que asigne a cada par estado-acción (s, a) un valor que representa la recompensa esperada a largo plazo por tomar la acción a en el estado s y luego seguir la política.

El algoritmo SARSA actualiza la función de valor Q(s, a) basándose en la diferencia temporal entre las recompensas estimadas en el estado actual y en el siguiente estado. Este proceso de actualización se puede representar de la siguiente manera:
$$\large
Q(s, a) <- Q(s, a) + α [R + γQ(s', a') - Q(s, a)]
$$
Donde:

- Q(s, a) es la estimación actual del valor del par estado-acción (s, a)
- R es la [[Recompensa]] recibida al pasar del estado s al estado s' al tomar la acción a.
- γ es el [[Factor de descuento]], que determina cuánto valoramos las recompensas futuras en comparación con las recompensas inmediatas.
- α es la [[Taza de aprendizaje]], que determina cuánto del error de la estimación (la diferencia temporal) utilizamos para actualizar el valor de Q(s, a).
- Q(s', a') es el valor de la siguiente acción-estado par que seguirá la política.

Las diferencias temporales en el contexto de SARSA representan la discrepancia entre las estimaciones de recompensa actual y las estimaciones futuras. Estas diferencias se utilizan para actualizar y, con suerte, mejorar la función de valor Q.


# SARSA vs Q-learning

Tanto Q-learning como SARSA son algoritmos de aprendizaje por refuerzo que utilizan técnicas de diferencias temporales para aprender una política que puede maximizar la recompensa acumulada a largo plazo en un entorno dado. Sin embargo, existen diferencias importantes entre estos dos algoritmos que pueden hacer que uno sea más adecuado que el otro dependiendo de la situación específica.

**Q-Learning** es un algoritmo de control **off-policy**. Esto significa que a**prende la política óptima independientemente de la política que el agente esté siguiendo actualmente**. Q-Learning siempre busca optimizar, asumiendo que siempre tomará la mejor acción posible a partir de la información actual. Esto puede ser útil en situaciones donde:

- Se quiere que el agente aprenda la política óptima sin importar su comportamiento actual.
- **El agente tiene la capacidad de explorar el entorno de manera segura sin riesgo de consecuencias perjudiciales.**
- La política utilizada para generar los datos de entrenamiento difiere de la política que el agente debería aprender.

**SARSA**, por otro lado, es un algoritmo de control on-policy. Aprende la política que el agente está siguiendo actualmente, lo que significa que la política de aprendizaje y la política de comportamiento son las mismas. SARSA toma en cuenta el hecho de que la política actual puede implicar cierto grado de exploración, y por lo tanto, puede ser más conservador. SARSA puede ser más adecuado cuando:

- Las acciones de exploración pueden tener consecuencias negativas significativas (por ejemplo, en un entorno donde los errores pueden ser costosos o peligrosos).
- La política que se está utilizando para seleccionar las acciones durante el aprendizaje es la que se quiere mejorar.
- Se desea que el agente se comporte de forma óptima teniendo en cuenta la necesidad de la exploración.

En general, la elección entre Q-learning y SARSA depende del problema específico, de las características del entorno y de la importancia de la exploración versus la explotación.


