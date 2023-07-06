
previo: [[Aprendizaje y Planificación]]

![[Pasted image 20230706105923.png]]

Dyna-Q es un algoritmo de aprendizaje por refuerzo que integra la planificación, la actuación y el aprendizaje para mejorar la política de un agente. El algoritmo combina las experiencias directas del agente con las experiencias simuladas generadas por un modelo interno del entorno para actualizar las estimaciones de valor de las acciones y mejorar la política del agente. 

Dyna-Q sigue un enfoque model-based y on-policy. Utiliza un modelo del entorno para generar transiciones simuladas, y aprende la política basándose en las acciones que el agente realmente selecciona. En cada paso, Dyna-Q actualiza su modelo y su función de valor en base a la última transición real, y luego realiza varias actualizaciones de la función de valor en base a transiciones simuladas generadas a partir del modelo.

> Q-learning es un algoritmo off-policy porque actualiza su función Q en base a la acción de máximo valor Q en el próximo estado, sin importar qué acción el agente realmente tomó bajo su política de comportamiento. En otras palabras, Q-learning aprende la política óptima independientemente de cómo el agente está explorando el entorno.
> Por otro lado, Dyna-Q es un algoritmo on-policy porque, aunque maximiza la función Q, sus actualizaciones de la función Q se basan en la política que realmente sigue el agente. Además, durante la fase de planificación, Dyna-Q utiliza su modelo para simular transiciones y actualizar su función Q, y estas simulaciones se basan en las acciones que el agente tomaría según su política actual.

Este algoritmo muestra el ciclo de realimentación entre la planificación, la actuación y el aprendizaje en Dyna-Q. El agente actúa en el entorno y aprende tanto del modelo como de las estimaciones de valor. Luego utiliza estas estimaciones para planificar, generando experiencias simuladas y actualizando las estimaciones de valor en base a estas experiencias simuladas.

En términos de desafíos, Dyna-Q comparte los mismos problemas que el marco general de Dyna, incluyendo la necesidad de un modelo del entorno y la potencial ineficiencia en entornos con grandes espacios de estado-acción. Sin embargo, puede ser una herramienta eficaz en entornos donde el modelo es preciso y el espacio de estado-acción es manejable.