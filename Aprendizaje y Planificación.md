
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

## Planificacion

Una vez que se tiene un modelo, se pueden utilizar varias técnicas de planificación, incluyendo:

- **Planificación por estado:** En este enfoque, el agente selecciona un estado y una acción, usa el modelo para determinar la recompensa y el siguiente estado, y luego realiza una actualización de los valores de estado-acción como en Q-learning o SARSA. 
  
  > Un ejemplo de planificación por estado podría ser un agente de aprendizaje por refuerzo jugando al ajedrez. En cada turno, el agente podría seleccionar un estado (una configuración del tablero de ajedrez) y una acción (un movimiento), usar su modelo para determinar la recompensa y el siguiente estado, y luego actualizar sus valores de estado-acción en consecuencia.
  
- **Planificación con simulación de trayectorias:** En este enfoque, el agente simula una trayectoria completa desde un estado inicial hasta un estado terminal, y luego realiza actualizaciones de valor a lo largo de esta trayectoria.
  
  > Un ejemplo de planificación con simulación de trayectorias podría ser un agente de aprendizaje por refuerzo que juega a un videojuego como Pac-Man. El agente podría comenzar en un estado inicial (la configuración inicial del laberinto y la posición de Pac-Man), simular una trayectoria completa hasta un estado terminal (por ejemplo, Pac-Man siendo capturado por un fantasma), y luego actualizar sus valores de estado-acción a lo largo de esta trayectoria.
  
-  **Planificación basada en prioridad:** En este enfoque, se dan prioridad a los estados y acciones para las actualizaciones basadas en alguna medida de "interés" o "urgencia". Por ejemplo, se podrían priorizar las actualizaciones para los estados y acciones que han experimentado los mayores cambios de valor recientemente.
  
  > Un ejemplo de planificación basada en prioridad podría ser un agente de aprendizaje por refuerzo que juega al ajedrez. El agente podría priorizar la actualización de los estados y acciones que han experimentado los mayores cambios de valor recientemente, con la idea de que estos son los movimientos más "interesantes" o "urgentes" para aprender.

# Dinámica de Planificación

La dinámica de planificación es el proceso de cómo las actualizaciones de los valores de estado-acción (o estado) se propagan a través de la función de valor. Esto generalmente se realiza a través de un proceso iterativo, donde los valores se actualizan en función de los valores actuales y las recompensas esperadas del modelo.

Este proceso puede verse como una propagación de información a través del espacio de estados y acciones. A medida que se obtiene nueva información, ya sea a través de la interacción directa con el entorno (aprendizaje) o a través de simulaciones del modelo (planificación), esta información se propaga a través de las actualizaciones de valor.

Uno de los desafíos clave en la dinámica de la planificación es decidir en qué orden se deben actualizar los estados y las acciones. Existen diferentes enfoques para esto, incluyendo:

- **Planificación aleatoria:** En este enfoque, los estados y las acciones se seleccionan al azar para las actualizaciones. 
- **Planificación con búsqueda en profundidad:** En este enfoque, se realiza una búsqueda completa desde un estado inicial hasta un estado terminal, actualizando todos los estados y acciones a lo largo del camino. 
- **Planificación basada en prioridad:** En este enfoque, se dan prioridad a los estados y acciones para las actualizaciones basadas en alguna medida de "interés" o "urgencia". Por ejemplo, se podrían priorizar las actualizaciones para los estados y acciones que han experimentado los mayores cambios de valor recientemente.

La planificación puede ser costosa computacionalmente, especialmente en problemas con espacios de estado y acción muy grandes. Por lo tanto, es importante equilibrar el costo de la planificación con sus beneficio.

### 8.2.1 Retroceso completo

El retroceso completo es un enfoque de planificación en el que se actualizan todos los estados y acciones que llevan al estado y acción actual. Esto es eficiente en términos de la cantidad de actualizaciones de valor necesarias para propagar un cambio de valor a través del espacio de estado-acción, pero puede ser costoso en términos de la cantidad de cálculos necesarios.

### 8.2.2 Retroceso basado en la muestra

El retroceso basado en la muestra es un enfoque de planificación en el que se actualiza un solo estado y acción que lleva al estado y acción actual. Este enfoque es menos costoso computacionalmente que el retroceso completo, pero puede requerir más actualizaciones de valor para propagar un cambio de valor a través del espacio de estado-acción. 

### 8.2.3 Retroceso basado en la heurística

El retroceso basado en la heurística es un enfoque de planificación en el que se seleccionan estados y acciones para actualizar en función de una heurística. La heurística podría basarse, por ejemplo, en la magnitud de los cambios de valor recientes, la frecuencia con la que se ha visitado un estado o acción, o la "distancia" desde el estado y acción actual hasta el estado y acción que se está considerando para la actualización.

En resumen, el capítulo 8 de Sutton y Barto se centra en cómo los agentes pueden usar modelos para mejorar su aprendizaje y toma de decisiones. Los modelos pueden ser de muestra o de distribución, y se pueden usar para planificación. La planificación puede ser por estado o con simulación de trayectorias, y puede seguir una dinámica que involucra la propagación de actualizaciones de valor a través del espacio de estado-acción. Los enfoques para la dinámica de la planificación incluyen la planificación aleatoria, la planificación con búsqueda en profundidad y la planificación basada en prioridad. El retroceso también juega un papel importante en la planificación, y puede ser completo, basado en la muestra o basado en la heurística.
