
En este capítulo, Sutton y Barto abordan el tema de cómo los agentes pueden aprender mientras planean, y cómo el aprendizaje y la planificación pueden interactuar de manera beneficiosa. 

# Modelos y Planificación

## Modelo

En el contexto del aprendizaje por refuerzo, un modelo se utiliza para imitar el comportamiento del [[Entorno]]. Los agentes que usan un modelo para guiar su aprendizaje y tomar decisiones se conocen como agentes basados en modelos ([[Model based]]). **El proceso de usar un modelo para determinar cómo actuar se conoce como planificación**. 

Hay dos tipos principales de modelos: 

1. **Modelos de muestra:** Generan una muestra representativa del siguiente estado y la recompensa dada una acción y un estado.
   
   > Un ejemplo de modelo de muestra podría ser un agente de aprendizaje por refuerzo jugando a un juego de mesa como el ajedrez. En cada turno, el agente podría usar un modelo de muestra para generar un conjunto representativo de posibles movimientos (acciones) y sus consecuencias (siguientes estados y recompensas). Esto podría basarse en las reglas del juego y en la experiencia pasada del agente jugando al ajedrez

2. **Modelos de distribución:** Generan todas las posibles transiciones junto con su probabilidad. 
   
   > Un ejemplo de modelo de distribución podría ser un agente de aprendizaje por refuerzo que opera en un entorno de comercio de acciones. El agente podría tener un modelo de distribución que, dado un estado (por ejemplo, los precios de las acciones actuales) y una acción (por ejemplo, comprar o vender una acción), genera todas las posibles transiciones (por ejemplo, todos los posibles nuevos precios de las acciones y las recompensas asociadas), junto con sus probabilidades.

Los modelos de distribución son más completos y permiten una planificación más precisa, pero también son más costosos de generar y utilizar. 

![[Pasted image 20230706093057.png]]

![[Pasted image 20230706094945.png]]

## Planificación

![[Pasted image 20230706095013.png]]

Una vez que se tiene un modelo, se pueden utilizar varias técnicas de planificación, incluyendo:

- **Planificación por estado:** En este enfoque, el agente selecciona un estado y una acción, usa el modelo para determinar la recompensa y el siguiente estado, y luego realiza una actualización de los valores de estado-acción como en Q-learning o SARSA. 
  
  > Un ejemplo de planificación por estado podría ser un agente de aprendizaje por refuerzo jugando al ajedrez. En cada turno, el agente podría seleccionar un estado (una configuración del tablero de ajedrez) y una acción (un movimiento), usar su modelo para determinar la recompensa y el siguiente estado, y luego actualizar sus valores de estado-acción en consecuencia.
  
- **Planificación con simulación de trayectorias:** En este enfoque, el agente simula una trayectoria completa desde un estado inicial hasta un estado terminal, y luego realiza actualizaciones de valor a lo largo de esta trayectoria.
  
  > Un ejemplo de planificación con simulación de trayectorias podría ser un agente de aprendizaje por refuerzo que juega a un videojuego como Pac-Man. El agente podría comenzar en un estado inicial (la configuración inicial del laberinto y la posición de Pac-Man), simular una trayectoria completa hasta un estado terminal (por ejemplo, Pac-Man siendo capturado por un fantasma), y luego actualizar sus valores de estado-acción a lo largo de esta trayectoria.
  
-  **Planificación basada en prioridad:** En este enfoque, se dan prioridad a los estados y acciones para las actualizaciones basadas en alguna medida de "interés" o "urgencia". Por ejemplo, se podrían priorizar las actualizaciones para los estados y acciones que han experimentado los mayores cambios de valor recientemente.
  
  > Un ejemplo de planificación basada en prioridad podría ser un agente de aprendizaje por refuerzo que juega al ajedrez. El agente podría priorizar la actualización de los estados y acciones que han experimentado los mayores cambios de valor recientemente, con la idea de que estos son los movimientos más "interesantes" o "urgentes" para aprender.


## Aprendizaje (learning)

![[Pasted image 20230706100054.png]]

**Learning (Aprendiendo):** El "learning" se refiere a cómo el agente actualiza su conocimiento o su modelo del entorno en base a las observaciones y recompensas que recibe de sus acciones. En el caso de Dyna, esto implicaría actualizar la función de valor del agente y/o su modelo interno del entorno. El aprendizaje puede incluir tanto la actualización de la función de valor del agente directamente con base en las recompensas que recibe (como en Q-learning), como la actualización del modelo interno del entorno del agente, que luego puede usarse para la simulación y la planificación.

# Dyna

![[Pasted image 20230706105531.png]]

Dyna es un marco de trabajo integrado que **combina la planificación, la actuación y el aprendizaje** para resolver problemas de aprendizaje por refuerzo. Se basa en la idea de que un agente puede beneficiarse de la combinación de experiencias directas y simuladas para mejorar su política de acciones. 

![[Pasted image 20230706100803.png]]


La **planificación** en Dyna se refiere a la utilización de un modelo interno del entorno para simular experiencias. Esto puede implicar la generación de transiciones simuladas (estado, acción, recompensa, estado siguiente) utilizando el modelo interno, y luego la actualización de las estimaciones de valor en base a estas transiciones simuladas. Las transiciones simuladas permiten al agente experimentar una variedad de posibles resultados sin tener que realizar acciones reales en el entorno. **Esto puede permitir una mejora más rápida de la política del agente, ya que puede "pensar en el futuro" y anticipar los resultados de las acciones antes de tomarlas**.


El **actuar** en Dyna se refiere a la selección y realización de acciones en el entorno basándose en la política actual. La política se deriva generalmente de las estimaciones de valor actuales del agente, que pueden haber sido aprendidas tanto de experiencias directas como simuladas. Actuar en el entorno permite al agente obtener experiencias directas, que proporcionan información valiosa y a menudo necesaria para mejorar tanto el modelo del entorno como las estimaciones de valor.

El **aprendizaje** en Dyna se refiere a cómo el agente actualiza su conocimiento basándose en las experiencias que obtiene, tanto directas como simuladas. Esto puede implicar el aprendizaje de un modelo del entorno, que se utiliza para la planificación, y el aprendizaje de las estimaciones de valor, que se utilizan para la selección de acciones. El aprendizaje del modelo implica la actualización de las transiciones del modelo en función de las experiencias directas del agente. El aprendizaje de las estimaciones de valor puede implicar la actualización de las estimaciones en función de las recompensas recibidas y las estimaciones de valor del estado siguiente, tanto para las experiencias directas como las simuladas.

Un aspecto central del enfoque Dyna es el bucle de realimentación entre la planificación, la actuación y el aprendizaje. El agente actúa en el entorno y aprende de las experiencias directas, lo que actualiza tanto el modelo del entorno como las estimaciones de valor. El agente también planifica utilizando el modelo del entorno para generar experiencias simuladas, de las cuales también aprende, actualizando las estimaciones de valor. Estas mejoras en las estimaciones de valor luego informan la política del agente, que influye en las acciones futuras que el agente seleccionará.

En resumen, Dyna es un enfoque de aprendizaje por refuerzo que combina planificación, actuación y aprendizaje en un marco integrado. Utiliza un modelo del entorno para simular experiencias, aprende de las experiencias directas y simuladas para mejorar las estimaciones de valor y la política, y utiliza esta política para actuar en el entorno. Este ciclo de retroalimentación continua permite al agente mejorar continuamente su política y su rendimiento en el entorno.

![[Pasted image 20230706105952.png]]

## Desafíos

Uno de los principales desafíos de Dyna es que requiere un modelo del entorno para la planificación. En muchos casos, este modelo no está disponible o es muy costoso de aprender. Además, si el entorno cambia con el tiempo (es no estacionario), el modelo puede volverse obsoleto, lo que puede afectar negativamente la planificación. Dyna también puede enfrentar problemas cuando el espacio de estado-acción es muy grande, ya que el tiempo y los recursos requeridos para la simulación y la actualización de valores pueden ser prohibitivos.

## Cuando usarlo

Dyna puede ser particularmente útil en entornos donde el agente puede beneficiarse de la "imaginación" o la simulación de acciones antes de realizarlas. Si el agente puede aprender un modelo preciso del entorno, y si el espacio de estado-acción es manejable, entonces Dyna puede permitir una mejora más rápida de la política que mediante la experiencia directa solamente. Además, Dyna puede ser beneficioso en entornos donde el agente puede realizar muchas simulaciones en cada paso de tiempo real.

> Importante: si el costo de ejecutar una acción en el entorno real es caro, quizás nos conviene simularlo


# Dyna-Q

![[Pasted image 20230706105923.png]]

Dyna-Q es un algoritmo de aprendizaje por refuerzo que integra la planificación, la actuación y el aprendizaje para mejorar la política de un agente. El algoritmo combina las experiencias directas del agente con las experiencias simuladas generadas por un modelo interno del entorno para actualizar las estimaciones de valor de las acciones y mejorar la política del agente. 

Dyna-Q sigue un enfoque model-based y on-policy. Utiliza un modelo del entorno para generar transiciones simuladas, y aprende la política basándose en las acciones que el agente realmente selecciona. En cada paso, Dyna-Q actualiza su modelo y su función de valor en base a la última transición real, y luego realiza varias actualizaciones de la función de valor en base a transiciones simuladas generadas a partir del modelo.

> Q-learning es un algoritmo off-policy porque actualiza su función Q en base a la acción de máximo valor Q en el próximo estado, sin importar qué acción el agente realmente tomó bajo su política de comportamiento. En otras palabras, Q-learning aprende la política óptima independientemente de cómo el agente está explorando el entorno.
> Por otro lado, Dyna-Q es un algoritmo on-policy porque, aunque maximiza la función Q, sus actualizaciones de la función Q se basan en la política que realmente sigue el agente. Además, durante la fase de planificación, Dyna-Q utiliza su modelo para simular transiciones y actualizar su función Q, y estas simulaciones se basan en las acciones que el agente tomaría según su política actual.

Este algoritmo muestra el ciclo de realimentación entre la planificación, la actuación y el aprendizaje en Dyna-Q. El agente actúa en el entorno y aprende tanto del modelo como de las estimaciones de valor. Luego utiliza estas estimaciones para planificar, generando experiencias simuladas y actualizando las estimaciones de valor en base a estas experiencias simuladas.

En términos de desafíos, Dyna-Q comparte los mismos problemas que el marco general de Dyna, incluyendo la necesidad de un modelo del entorno y la potencial ineficiencia en entornos con grandes espacios de estado-acción. Sin embargo, puede ser una herramienta eficaz en entornos donde el modelo es preciso y el espacio de estado-acción es manejable.




<iframe width="560" height="315" src="https://www.youtube.com/embed/ItMutbeOHtc?start=2894" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>