El aprendizaje por refuerzo es un tipo de inteligencia artificial donde un [[Agente]] (como un programa de computadora o un robot) aprende a tomar decisiones en un [[Entorno]]
al interactuar con él y recibir [[Recompensa]] o castigos según la calidad de sus [[Acción]]. El objetivo del agente es maximizar las recompensas a lo largo del tiempo, lo que le permite mejorar su comportamiento y tomar decisiones cada vez más efectivas en situaciones similares.

# Características

En el aprendizaje por refuerzo, los enfoques pueden categorizarse en varias dimensiones. A continuación, se enumeran algunas de las categorías más importantes:

1. **Model-free vs Model-based:** En los métodos [[Model free]], el agente no tiene un modelo del entorno y aprende directamente a partir de la experiencia. En los métodos [[Model based]], el agente tiene un modelo del entorno que utiliza para simular experiencias y aprender de ellas.

2. **Online vs Offline:** En el aprendizaje online, el agente aprende mientras interactúa con el entorno en tiempo real. En el aprendizaje offline, el agente aprende a partir de un conjunto de experiencias previamente recolectadas.
   
	- **Aprendizaje Online:** En el aprendizaje online, el agente aprende directamente de las interacciones con el entorno. A medida que el agente interactúa con el entorno, recopila nuevas experiencias (transiciones de estado, acción, recompensa) y las usa para actualizar sus estimaciones de la función de valor o la política. En el contexto de los modelos, un agente puede construir un modelo a partir de sus experiencias online y luego usar este modelo para la planificación.

	- **Aprendizaje Offline:** En el aprendizaje offline, el agente aprende a partir de un conjunto de datos de experiencias previamente recopiladas, no directamente de sus interacciones actuales con el entorno. El conjunto de datos podría haber sido recopilado por el propio agente en interacciones anteriores con el entorno, o por otros agentes. Los modelos pueden ser particularmente útiles en el aprendizaje offline, ya que permiten al agente realizar "inferencia de trayectoria", es decir, aprender sobre secuencias de estados y acciones que no aparecen explícitamente en el conjunto de datos.


3. **On-policy vs Off-policy:** En los métodos [[On-Policy]], el agente aprende el valor de la política que está siguiendo actualmente. En los métodos [[Off-policy]], el agente aprende el valor de una política diferente a la que está siguiendo.

4. **Tabular vs Function Approximation:** En los métodos tabulares, el agente mantiene una tabla separada de valores para cada estado o par estado-acción. En los métodos de aproximación de funciones, el agente utiliza una función parametrizada para aproximar los valores de estado o estado-acción (ver [[Métodos de aproximación de la función de valor]]).

5. **Single-agent vs Multi-agent:** En los entornos de un solo agente, un único agente aprende a optimizar su comportamiento. En los entornos multiagente, varios agentes aprenden simultáneamente, y la política óptima para un agente puede depender del comportamiento de los otros agentes.

6. **Deterministic vs Stochastic:** En los entornos deterministas, la transición de estado y la función de recompensa son fijas y deterministas. En los entornos estocásticos, las transiciones de estado y las recompensas tienen alguna cantidad de aleatoriedad.

Estas categorías no son mutuamente excluyentes y, de hecho, un método de aprendizaje por refuerzo puede caer en varias categorías. Por ejemplo, un método puede ser model-free, online, off-policy y usar aproximación de funciones.

Existen muchas otras formas de categorizar los enfoques en el aprendizaje por refuerzo. Algunas de las más importantes incluyen:

1. **Temporal-Difference (TD) Learning vs Monte Carlo (MC) Methods:** En los [[Métodos de Diferencias temporales]], el agente actualiza sus estimaciones de la función de valor en cada paso, mientras que en los [[Métodos Monte Carlo]], el agente espera hasta el final de un episodio para actualizar sus estimaciones.

2. **Value-Based vs Policy-Based:** En los métodos basados en valor, el agente busca aprender la función de valor óptima y deriva una política a partir de ella. En los métodos basados en políticas, el agente busca aprender directamente la política óptima (ver [[Gradiente de Política]]).

3. **Bootstrapping vs Non-Bootstrapping:** Bootstrapping implica actualizar las estimaciones de la función de valor basándose en otras estimaciones actuales de la función de valor (ver [[Bootstrapping]]. Los métodos de no bootstrapping, como Monte Carlo, sólo utilizan recompensas reales y no estimaciones para las actualizaciones.
   
4. **Ambiente Estacionario vs No Estacionario:** Un ambiente estacionario es aquel en el que la función de recompensa y la función de transición de estado no cambian con el tiempo. En un ambiente no estacionario, estas funciones pueden cambiar.
   
5. **Problemas de Control vs Problemas de Predicción/Estimación:** En los problemas de control, el objetivo es encontrar la mejor política. En los problemas de predicción, el objetivo es predecir las futuras recompensas bajo una política dada.


# Aprendizaje por refuerzo vs aprendizaje supervisado 

> [!quote]
> Reinforcement learning is different from supervised learning, the kind of learning studied in most current research in the field of machine learning. Supervised learning is learning from a training set of labeled examples provided by a knowledgable external supervisor.

![[machine_learning_mind_map_3.webp]]
El aprendizaje por refuerzo y el aprendizaje supervisado son dos enfoques diferentes en el campo de la inteligencia artificial y el aprendizaje automático. A continuación, se describen sus principales diferencias:

1.  Retroalimentación:

-   Aprendizaje supervisado: El algoritmo recibe un conjunto de datos etiquetado, que incluye entradas y las respuestas correctas (etiquetas) para cada entrada. El objetivo es aprender un modelo que pueda predecir las etiquetas correctas para nuevas entradas no vistas previamente.
  
-   Aprendizaje por refuerzo: El agente aprende a través de la interacción con el entorno y no tiene acceso a las respuestas correctas. En su lugar, recibe recompensas o castigos como retroalimentación, que le permite aprender cuáles acciones son beneficiosas y cuáles no.

2.  Tipo de problema:

-   Aprendizaje supervisado: Se utiliza generalmente para problemas de clasificación y regresión, donde el objetivo es predecir una etiqueta o valor para una entrada dada.
  
-   Aprendizaje por refuerzo: Se aplica a problemas de toma de decisiones secuenciales y optimización, donde el agente debe aprender una [[Política]] que le permita tomar decisiones óptimas en una secuencia de pasos o acciones.

3.  Evaluación del rendimiento:

-   Aprendizaje supervisado: El rendimiento del modelo se mide generalmente comparando las predicciones del modelo con las etiquetas reales en un conjunto de datos de prueba. Se utilizan métricas como precisión, sensibilidad, especificidad y error cuadrático medio.
-   Aprendizaje por refuerzo: El rendimiento del agente se evalúa en función de la cantidad total de recompensas acumuladas a lo largo del tiempo durante su interacción con el entorno.

4.  Generalización:

-   Aprendizaje supervisado: La generalización se basa en la calidad y cantidad de datos etiquetados disponibles y en cómo de bien el modelo pueda aprender a partir de ellos. Los modelos de aprendizaje supervisado pueden sufrir de sobreajuste si se entrenan demasiado en datos de entrenamiento ruidosos o limitados.
  
-   Aprendizaje por refuerzo: La generalización en el aprendizaje por refuerzo depende de la capacidad del agente para explorar y aprender de diferentes estados y situaciones en el entorno. El agente debe equilibrar la [[Exploración]] de nuevas acciones con la [[Explotación]] de las acciones conocidas para maximizar las recompensas.

# Exploracion vs Explotacion

> [!quote]
> One of the challenges that arise in reinforcement learning, and not in other kinds of learning, is the trade-off between exploration and exploitation. To obtain a lot of reward, a reinforcement learning agent must prefer actions that it has tried in the past and found to be effective in producing reward. But to discover such actions, it has to try actions that it has not selected before. The agent has to exploit what it has already experienced in order to obtain reward, but it also has to explore in order to make better action selections in the future. The dilemma is that neither exploration nor exploitation can be pursued exclusively without failing at the task.

# Elementos 

> [!quote]
> Beyond the agent and the environment, one can identify four main subelements of a reinforcement learning system: a policy, a reward signal, a value function, and, optionally, a model of the environment.

- ver [[Política]]
- ver [[Señal de recompensa]]
- ver [[Función de valor]]
- ver [[Modelo de ambiente]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/NFo9v_yKQXA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

