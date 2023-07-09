Diferencias Temporales (TD Learning) es una combinación de [[Métodos Monte Carlo]] e [[Iteración de Valor (value iteration)]]. Al igual que la Iteración de Valor, los métodos de Diferencias Temporales **están basados en la actualización de las estimaciones basadas en otras estimaciones** ([[Bootstrapping]]. Al igual que en los métodos de Monte Carlo, **las diferencias temporales pueden aprender directamente de la experiencia sin requerir un modelo de medio ambiente**.

# Primer acercamiento

Los métodos de Diferencias Temporales utilizan la idea de que la estimación de un estado puede ser mejorada al considerar la estimación de los estados siguientes. En otras palabras, un **agente puede aprender de los estados que aún no ha visitado al considerar las recompensas y las estimaciones de los estados que sigue inmediatamente a los estados actuales**.

![[Pasted image 20230624190219.png]]

# Ventajas de Diferencias Temporales

Las Diferencias Temporales tienen varias ventajas sobre los métodos de Monte Carlo. La más obvia es que las diferencias temporales pueden aprender **en línea** (online) después de cada paso, mientras que Monte Carlo debe esperar hasta el final de un episodio. Esto es muy útil en situaciones donde los **episodios pueden ser muy largos o incluso infinitos**. 

**Aprendizaje en línea (Online Learning)** se refiere a un tipo de aprendizaje automático donde el modelo se entrena y se actualiza continuamente a medida que llegan nuevos datos. En el contexto del aprendizaje por refuerzo, "aprendizaje en línea" generalmente se refiere a la capacidad del agente de aprender y mejorar su política **mientras interactúa con el entorno**.

En otras palabras, en lugar de tener que esperar hasta el final de un episodio para actualizar la política o los valores de los estados (como en los métodos de Monte Carlo), los métodos de aprendizaje en línea pueden realizar actualizaciones después de cada paso de tiempo basándose en la última acción tomada, el estado actual, la recompensa recibida y el siguiente estado. **Esto puede ser beneficioso en situaciones donde los episodios son largos o incluso infinitos, o cuando el entorno puede cambiar con el tiempo (problemas no estacionarios)**.

Un ejemplo de un algoritmo de aprendizaje en línea en aprendizaje por refuerzo es TD(0), que es un método de diferencias temporales que realiza actualizaciones después de cada paso de tiempo utilizando la recompensa inmediata y la estimación de valor del estado siguiente.

# Algoritmos de Diferencias Temporales

Existen varios algoritmos de Diferencias Temporales. Algunos de los más conocidos son:

1. **TD(0)**: Este es el método más básico de Diferencias Temporales. TD(0) actualiza las estimaciones de valor después de cada paso de tiempo utilizando la recompensa inmediata y la estimación de valor del estado siguiente. vease [[TD(0)]]
2. **N-steps TD**. vease [[N-steps TD]]
3. **SARSA**: Este es un algoritmo de control (para aprender políticas) basado en Diferencias Temporales. SARSA es un acrónimo que representa los elementos utilizados en la actualización: estado (S), acción (A), recompensa (R), estado siguiente (S') y acción siguiente (A'). vease [[SARSA]]
4. **Q-Learning**: Al igual que SARSA, Q-Learning es un algoritmo de control basado en Diferencias Temporales, pero se diferencia en que utiliza la acción que maximiza el valor estimado para el estado siguiente, en lugar de la acción que la política actual sugeriría tomar. vease [[Q-learning]]

Recuerda que en los algoritmos de diferencias temporales, al igual que en los métodos de Monte Carlo, se puede usar el muestreo para seleccionar acciones, y se pueden usar políticas ε-soft para asegurar la exploración continua.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AJiG3ykOxmY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
