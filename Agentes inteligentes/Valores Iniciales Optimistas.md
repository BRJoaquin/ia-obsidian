Los valores iniciales optimistas son **valores iniciales de los estimados de valor de acción que son más altos de lo que se espera que sean los verdaderos valores de acción**. La idea detrás de los valores iniciales optimistas es que se fomentará una mayor exploración en el aprendizaje por refuerzo, ya que los estimados de valor de acción serán inicialmente muy optimistas y el agente de aprendizaje buscará descubrir si hay valores de acción aún mayores.

Los valores iniciales optimistas pueden ser útiles en situaciones donde se sabe que las recompensas son altas, ya que ayudarán al agente de aprendizaje a descubrir rápidamente las acciones que generan las recompensas más altas. Sin embargo, si se desconoce el rango de recompensas, los valores iniciales optimistas pueden ser perjudiciales ya que pueden llevar a la convergencia prematura en una acción subóptima.

## Valor inicial

Elegir el valor inicial para los estimados de valor de acción puede ser una tarea difícil, ya que estos valores pueden influir significativamente en el comportamiento del algoritmo de aprendizaje por refuerzo. A continuación, se presentan algunas consideraciones generales para seleccionar los valores iniciales:

1.  Conocimiento previo: si se tiene algún conocimiento previo sobre el dominio de la tarea, este conocimiento puede usarse para establecer los valores iniciales. Por ejemplo, si se sabe que ciertas acciones tienen una alta probabilidad de recompensa, se pueden establecer valores iniciales optimistas para estas acciones.

2.  Exploración: los valores iniciales optimistas pueden ser útiles para fomentar la exploración en el aprendizaje por refuerzo. Estos valores iniciales deben ser lo suficientemente altos como para fomentar la exploración, pero no tan altos como para ser completamente irreales.

3.  Valor medio: si no se tiene ningún conocimiento previo sobre el dominio de la tarea, se puede establecer el valor inicial en el valor medio de las recompensas posibles.

4.  Prueba y error: en algunos casos, la mejor manera de seleccionar valores iniciales es a través de la experimentación y la prueba y error. Se pueden probar diferentes valores iniciales y observar cómo afectan el comportamiento del algoritmo de aprendizaje por refuerzo.


En resumen, la elección del valor inicial para los estimados de valor de acción puede depender del conocimiento previo, la necesidad de fomentar la exploración, el valor medio de las recompensas posibles o la experimentación y la prueba y error.