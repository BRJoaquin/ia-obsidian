
UCB son las siglas de "Upper Confidence Bound" (Límite Superior de Confianza, en español). Es un algoritmo utilizado en el aprendizaje por refuerzo para equilibrar la explotación de las acciones con la exploración de nuevas acciones. 

En UCB, se utiliza una función de selección de acción que toma en cuenta tanto la estimación actual de la recompensa de una acción ($Q_t(a)$) como la incertidumbre asociada con esa estimación ($\sqrt{\frac{c\ln t}{N_t(a)}}$). 

$$A_t = \arg\max_a \left(Q_t(a) + c\sqrt{\frac{\ln t}{N_t(a)}}\right)$$

La C es un parámetro que determina el grado de exploración versus explotación en el algoritmo UCB. A medida que aumenta el valor de C, el algoritmo se vuelve más exploratorio, ya que aumenta la bonificación para las acciones menos seleccionadas. Por otro lado, a medida que disminuye el valor de C, el algoritmo se vuelve más explotador, ya que se da más peso a las estimaciones de recompensa existentes en lugar de la bonificación por selección infrecuente de acciones. El valor óptimo de C depende del problema específico que se está abordando y puede ser determinado experimentalmente.

El valor óptimo de C para el algoritmo UCB no tiene una solución única, ya que depende del problema específico y de la cantidad de datos disponibles. Sin embargo, se han propuesto algunas heurísticas y enfoques para elegir un valor adecuado de C.

Una de las formas más comunes de elegir C es mediante la utilización de la [[Desigualdad de Hoeffding]], que proporciona una cota superior para la probabilidad de que la estimación de la recompensa de una acción difiera significativamente de su verdadero valor. El valor de C se puede elegir de tal manera que la bonificación por incertidumbre sea menor que esta cota superior.

Otra forma de elegir C es mediante la optimización empírica, es decir, probando diferentes valores de C y eligiendo el que mejor funciona para un problema específico. En general, se recomienda comenzar con un valor bajo de C y aumentarlo gradualmente a medida que se recopilan más datos y se reduce la incertidumbre en las estimaciones de la recompensa.

En resumen, elegir el valor óptimo de C para el algoritmo UCB es un proceso empírico y depende de la naturaleza del problema y de la cantidad de datos disponibles.

