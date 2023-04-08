
UCB son las siglas de "Upper Confidence Bound" (Límite Superior de Confianza, en español). Es un algoritmo utilizado en el aprendizaje por refuerzo para equilibrar la explotación de las acciones con la exploración de nuevas acciones. 

En UCB, se utiliza una función de selección de acción que toma en cuenta tanto la estimación actual de la recompensa de una acción ($Q_t(a)$) como la incertidumbre asociada con esa estimación ($\sqrt{\frac{c\ln t}{N_t(a)}}$). 

$$A_t = \arg\max_a \left(Q_t(a) + c\sqrt{\frac{\ln t}{N_t(a)}}\right)$$

La C es un parámetro que determina el grado de exploración versus explotación en el algoritmo UCB. A medida que aumenta el valor de C, el algoritmo se vuelve más exploratorio, ya que aumenta la bonificación para las acciones menos seleccionadas. Por otro lado, a medida que disminuye el valor de C, el algoritmo se vuelve más explotador, ya que se da más peso a las estimaciones de recompensa existentes en lugar de la bonificación por selección infrecuente de acciones. El valor óptimo de C depende del problema específico que se está abordando y puede ser determinado experimentalmente.

