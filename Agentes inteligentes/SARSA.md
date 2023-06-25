SARSA (State-Action-Reward-State-Action) es un algoritmo de aprendizaje por refuerzo que se basa en el uso de diferencias temporales (TD, por sus siglas en inglés) para actualizar los valores de la función de valor acción (Q-valor).

Las diferencias temporales son una técnica utilizada en el aprendizaje por refuerzo para actualizar los valores estimados de la función de valor de acuerdo con las recompensas reales obtenidas en el entorno. El concepto clave de las diferencias temporales es la idea de actualizar los valores estimados a medida que se experimenta y se recibe retroalimentación del entorno.

En el algoritmo SARSA, se utiliza una estrategia de aprendizaje on-policy, lo que significa que se aprende directamente a partir de la política actual utilizada para la toma de decisiones. A medida que el agente interactúa con el entorno, sigue una política específica y actualiza los valores de la función de valor acción según las diferencias temporales.

Aquí está el proceso general del algoritmo SARSA:

1. Inicializar la función de valor acción (Q-valor) con valores arbitrarios o aleatorios.
    
2. Observar el estado actual del entorno.
    
3. Seleccionar una acción utilizando una estrategia de selección de acción basada en la función de valor actual (por ejemplo, epsilon-greedy).
    
4. Tomar la acción y observar la recompensa y el próximo estado.
    
5. Seleccionar la próxima acción utilizando la misma estrategia de selección de acción basada en la función de valor actual.
    
6. Actualizar el valor de la función de valor acción utilizando la diferencia temporal SARSA:
    
    �(�,�)←�(�,�)+�⋅[�+�⋅�(�′,�′)−�(�,�)]Q(s,a)←Q(s,a)+α⋅[r+γ⋅Q(s′,a′)−Q(s,a)]
    
    Donde:
    
    - $Q(s, a)$ es el valor actualizado de la función de valor acción para el estado $s$ y la acción $a$.
    - $\alpha$ es la tasa de aprendizaje (learning rate) que controla la velocidad de actualización.
    - $r$ es la recompensa obtenida al tomar la acción $a$ en el estado $s$.
    - $\gamma$ es el factor de descuento que pondera la importancia de las recompensas futuras.
    - $s'$ es el próximo estado resultante después de tomar la acción $a$ en el estado $s$.
    - $a'$ es la próxima acción seleccionada en el próximo estado $s'$.
7. Repetir los pasos 2-6 hasta que se alcance un criterio de finalización.
    

En resumen, SARSA utiliza diferencias temporales para actualizar los valores de la función de valor acción basándose en las experiencias obtenidas al interactuar con el entorno utilizando una estrategia de aprendizaje on-policy. El algoritmo busca aprender una política óptima basada en la política actual y las recompensas observadas durante la interacción con el entorno.