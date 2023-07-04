
Bootstrapping, en el contexto de aprendizaje por refuerzo, se refiere al proceso de estimar el valor futuro de un estado en base a las estimaciones actuales.

En el caso de [[Q-learning]], la actualización del valor Q para un par estado-acción dado se realiza utilizando la recompensa inmediata más la estimación del valor Q del próximo estado y la mejor acción en ese estado. Por lo tanto, Q-Learning está haciendo una especie de "bootstrapping", porque está utilizando sus propias estimaciones (Q-values) para mejorar esas estimaciones. 

En cada paso del algoritmo [[SARSA]], se actualiza la estimación Q para el estado y acción actual basándose en la recompensa inmediata más la estimación Q del próximo estado y la acción que se va a tomar en ese estado (según la política actual). Esto es un ejemplo de bootstrapping, ya que se utiliza la propia estimación Q para actualizar dicha estimación.