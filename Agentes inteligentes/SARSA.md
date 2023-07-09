  
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

# Algoritmo 

![[Pasted image 20230625101600.png]]

# SARSA vs Q-learning

Tanto Q-learning como SARSA son algoritmos de aprendizaje por refuerzo que utilizan técnicas de diferencias temporales para aprender una política que puede maximizar la recompensa acumulada a largo plazo en un entorno dado. Sin embargo, existen diferencias importantes entre estos dos algoritmos que pueden hacer que uno sea más adecuado que el otro dependiendo de la situación específica.

**Q-Learning** es un algoritmo de control **off-policy**. Esto significa que a**prende la política óptima independientemente de la política que el agente esté siguiendo actualmente**. Q-Learning siempre busca optimizar, asumiendo que siempre tomará la mejor acción posible a partir de la información actual. Esto puede ser útil en situaciones donde:

- Se quiere que el agente aprenda la política óptima sin importar su comportamiento actual.
- **El agente tiene la capacidad de explorar el entorno de manera segura sin riesgo de consecuencias perjudiciales.**
- La política utilizada para generar los datos de entrenamiento difiere de la política que el agente debería aprender.

**SARSA**, por otro lado, es un algoritmo de control **on-policy**. Aprende la política que el agente está siguiendo actualmente, lo que significa que la política de aprendizaje y la política de comportamiento son las mismas. SARSA toma en cuenta el hecho de que la política actual puede implicar cierto grado de exploración, y por lo tanto, puede ser más conservador. SARSA puede ser más adecuado cuando:

- **Las acciones de exploración pueden tener consecuencias negativas significativas (por ejemplo, en un entorno donde los errores pueden ser costosos o peligrosos)**.
- La política que se está utilizando para seleccionar las acciones durante el aprendizaje es la que se quiere mejorar.
- Se desea que el agente se comporte de forma óptima teniendo en cuenta la necesidad de la exploración.

En general, la elección entre Q-learning y SARSA depende del problema específico, de las características del entorno y de la importancia de la exploración versus la explotación.

## Cliff Walking

![[Pasted image 20230625104944.png]]


El ejemplo del Cliff Walking es un problema clásico de aprendizaje por refuerzo que se usa a menudo para ilustrar las diferencias entre diferentes algoritmos de aprendizaje por refuerzo, incluyendo SARSA y Q-Learning.

### Descripción del Problema del Cliff Walking

Imagina un agente que necesita llegar desde un punto de inicio a un punto de destino en una cuadrícula. Hay un acantilado en el medio. Si el agente se cae al acantilado, recibe una gran penalización y se reinicia al punto de inicio.

- El punto de inicio está en la esquina inferior izquierda de la cuadrícula, y el punto de destino está en la esquina inferior derecha.
- El agente puede moverse en cuatro direcciones: arriba, abajo, izquierda y derecha.
- Cada movimiento recibe una recompensa de -1, excepto caer al acantilado, que recibe una recompensa de -100 y envía al agente de vuelta al inicio.
- El episodio termina cuando el agente alcanza el punto de destino.

## SARSA en el Problema del Cliff Walking

SARSA es un algoritmo on-policy, lo que significa que sigue y mejora la misma política que está siendo aprendida. En el problema del Cliff Walking, SARSA tiende a aprender una política que evita el borde del acantilado y toma un camino seguro y largo hacia el objetivo.

Esto es porque SARSA toma en consideración que está siguiendo una política ε-greedy durante el aprendizaje. **La política ε-greedy significa que hay una pequeña posibilidad de que el agente tome una acción aleatoria en lugar de la acción óptima.** Por lo tanto, el agente aprende a ser cauteloso con el acantilado porque sabe que podría caerse debido a la exploración aleatoria.

## Q-Learning en el Problema del Cliff Walking

Q-Learning, por otro lado, es un algoritmo off-policy. **Aprende la política óptima asumiendo que siempre tomará la mejor acción posible sin tener en cuenta la política que está siguiendo durante el aprendizaje**.

En el problema del Cliff Walking, Q-Learning **tiende a aprender la política que va por el camino más rápido y más peligroso al borde del acantilado**. Esto se debe a que Q-Learning asume que siempre tomará la mejor acción y no caerá al acantilado.

# Resumen

Aunque ambos algoritmos pueden aprender a resolver el problema, a menudo se observa que SARSA es más seguro pero más lento, mientras que Q-Learning es más rápido pero más arriesgado. **Esto es un reflejo de la diferencia entre los métodos on-policy y off-policy en el aprendizaje por refuerzo.**


<iframe width="560" height="315" src="https://www.youtube.com/embed/AJiG3ykOxmY?start=1308" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# N-step SARSA

vease: [[N-steps TD]]

N-step SARSA es una extensión del algoritmo SARSA original que considera una secuencia de n pasos en lugar de un solo paso para actualizar la función de valor de estado-acción Q(s, a). La idea es equilibrar entre el aprendizaje basado en un solo paso (como en SARSA y Q-Learning) y el aprendizaje basado en un episodio completo (como en el algoritmo de Monte Carlo).

![[Pasted image 20230625102623.png]]

En el algoritmo SARSA original, la actualización de la función de valor se basa en la recompensa inmediata y la estimación del siguiente valor de estado-acción. Sin embargo, en n-step SARSA, la actualización se basa en la suma de las recompensas de los próximos n pasos y la estimación del valor de estado-acción después de n pasos.

Por lo tanto, el algoritmo n-step SARSA sigue estos pasos:

![[Pasted image 20230625102639.png]]

La ventaja de n-step SARSA es que puede aprender más rápidamente que el SARSA original porque utiliza más información para cada actualización. Sin embargo, también puede ser más complicado de implementar debido a la necesidad de gestionar una secuencia de n pasos, y el rendimiento puede depender de la elección correcta de n.


# Video 

<iframe width="560" height="315" src="https://www.youtube.com/embed/AJiG3ykOxmY?start=929" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>