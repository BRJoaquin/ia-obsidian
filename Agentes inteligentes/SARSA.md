# Diferencia entre TD(0) y SARSA

TD(0) y SARSA son ambos algoritmos de aprendizaje por refuerzo que utilizan la idea de Diferencias Temporales (TD Learning) para estimar los valores de las acciones y/o estados. Aunque son similares en muchos aspectos, también tienen algunas diferencias clave en términos de cómo actualizan estas estimaciones.

## TD(0)
El algoritmo TD(0) se utiliza principalmente para estimar la función de valor de estado, $V(s)$, que representa el valor esperado de estar en un estado particular `s` bajo una política específica. En TD(0), la actualización se realiza en cada paso de tiempo usando la recompensa inmediata y la estimación del valor del próximo estado. Aquí está la regla de actualización de TD(0):

$$V(S_t) = V(S_t) + \alpha[R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]$$

## SARSA
Por otro lado, SARSA (que significa State-Action-Reward-State-Action) es un algoritmo de control, lo que significa que se utiliza para encontrar la política óptima, no solo para estimar los valores de los estados. SARSA estima la función de valor de acción-estado, $Q(s, a)$, que representa el valor esperado de tomar una acción particular `a` en un estado particular `s`. La actualización en SARSA también se realiza en cada paso de tiempo, pero utilizando la recompensa inmediata y la estimación del valor de la próxima acción-estado:

$$Q(S_t, A_t) = Q(S_t, A_t) + \alpha[R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)]$$

Una diferencia clave es que SARSA es un algoritmo on-policy, lo que significa que la política que se está optimizando es la misma política que se usa para decidir las acciones durante el aprendizaje. En otras palabras, SARSA toma en cuenta la política actual del agente al hacer las actualizaciones.

En resumen, la diferencia principal entre TD(0) y SARSA es que TD(0) es un algoritmo de predicción que se utiliza para estimar la función de valor de estado bajo una política específica, mientras que SARSA es un algoritmo de control que se utiliza para encontrar la política óptima estimando la función de valor de acción-estado y teniendo en cuenta la política actual del agente durante el aprendizaje.
