El aprendizaje por refuerzo es un tipo de inteligencia artificial donde un [[Agente]] (como un programa de computadora o un robot) aprende a tomar decisiones en un [[Entorno]]
al interactuar con él y recibir [[Recompensa]] o castigos según la calidad de sus [[Accion]]. El objetivo del agente es maximizar las recompensas a lo largo del tiempo, lo que le permite mejorar su comportamiento y tomar decisiones cada vez más efectivas en situaciones similares.


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

