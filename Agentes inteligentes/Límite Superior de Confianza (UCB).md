
UCB son las siglas de "Upper Confidence Bound" (Límite Superior de Confianza, en español). Es un algoritmo utilizado en el aprendizaje por refuerzo para equilibrar la explotación de las acciones con la exploración de nuevas acciones. 

En UCB, se utiliza una función de selección de acción que toma en cuenta tanto la estimación actual de la recompensa de una acción ($Q_t(a)$) como la incertidumbre asociada con esa estimación ($\sqrt{\frac{c\ln t}{N_t(a)}}$). 

$$\Huge A_t = \arg\max_a \left(Q_t(a) + c\sqrt{\frac{\ln t}{N_t(a)}}\right)$$

La C es un parámetro que determina el grado de exploración versus explotación en el algoritmo UCB. A medida que aumenta el valor de C, el algoritmo se vuelve más exploratorio, ya que aumenta la bonificación para las acciones menos seleccionadas. Por otro lado, a medida que disminuye el valor de C, el algoritmo se vuelve más explotador, ya que se da más peso a las estimaciones de recompensa existentes en lugar de la bonificación por selección infrecuente de acciones. El valor óptimo de C depende del problema específico que se está abordando y puede ser determinado experimentalmente.

El valor óptimo de C para el algoritmo UCB no tiene una solución única, ya que depende del problema específico y de la cantidad de datos disponibles. Sin embargo, se han propuesto algunas heurísticas y enfoques para elegir un valor adecuado de C.

Una de las formas más comunes de elegir C es mediante la utilización de la [[Desigualdad de Hoeffding]], que proporciona una cota superior para la probabilidad de que la estimación de la recompensa de una acción difiera significativamente de su verdadero valor. El valor de C se puede elegir de tal manera que la bonificación por incertidumbre sea menor que esta cota superior.

Otra forma de elegir C es mediante la optimización empírica, es decir, probando diferentes valores de C y eligiendo el que mejor funciona para un problema específico. En general, se recomienda comenzar con un valor bajo de C y aumentarlo gradualmente a medida que se recopilan más datos y se reduce la incertidumbre en las estimaciones de la recompensa.

En resumen, elegir el valor óptimo de C para el algoritmo UCB es un proceso empírico y depende de la naturaleza del problema y de la cantidad de datos disponibles.

# Explicación

La ecuación del UCB, que incluye el término $\sqrt{\frac{\ln t}{N_t(a)}}$, se basa en la idea de que a medida que un agente toma más decisiones y recibe más recompensas, se vuelve más seguro sobre cuáles son las mejores acciones a tomar. Por lo tanto, el término $\sqrt{\frac{\ln t}{N_t(a)}}$ tiene en cuenta la cantidad de veces que una acción ha sido seleccionada, y cuanto más se ha seleccionado, menor es la contribución de este término a la selección de la acción.

Por otro lado, el término $\ln t$ crece muy lentamente a medida que aumenta el número de pasos $t$, lo que significa que con el tiempo se tiene en cuenta cada vez menos la exploración y se da más importancia a la explotación. Esto tiene sentido, ya que a medida que se toman más decisiones, se tiene más información sobre qué acciones tienen mayores recompensas y se debe explotar esta información para maximizar las ganancias a largo plazo.

En resumen, el término $\sqrt{\frac{\ln t}{N_t(a)}}$ es una forma de equilibrar la exploración y la explotación a medida que el agente recibe más información y se vuelve más seguro en su elección de acciones.

## Problemas no estacionarios

El UCB es un algoritmo de selección de acciones que funciona bien en problemas estacionarios ([[Recompensa#Estacionaria]]), pero puede tener dificultades en problemas no estacionarios. Esto se debe a que la incertidumbre asociada a cada acción puede cambiar a lo largo del tiempo en un problema no estacionario, y el UCB no tiene en cuenta estos cambios.

En problemas no estacionarios ([[Recompensa#No Estacionaria]]), puede ser útil utilizar métodos que den mayor importancia a los datos más recientes. Por ejemplo, una posibilidad es utilizar un promedio ponderado de los valores de recompensa, en el que los datos más recientes tienen un peso mayor. Otro enfoque es utilizar un parámetro de tasa de aprendizaje que disminuye con el tiempo, de modo que los cambios en la estimación de los valores de recompensa sean cada vez menores.

En general, el UCB puede funcionar bien en problemas no estacionarios si se utiliza en combinación con otros métodos que tengan en cuenta la evolución de la incertidumbre a lo largo del tiempo.