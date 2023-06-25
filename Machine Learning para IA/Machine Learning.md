En términos sencillos, el machine learning (aprendizaje automático) es un proceso en el que una computadora aprende a realizar tareas o tomar decisiones basándose en datos y experiencias previas, sin tener que ser programada explícitamente para hacerlo.

Una definición más formal sería: el aprendizaje automático es una rama de la inteligencia artificial que se centra en el desarrollo de algoritmos y modelos matemáticos que permiten a las máquinas mejorar su desempeño en una tarea específica a través de la exposición a datos y la identificación de patrones en ellos.

![[Pasted image 20230416182840.png]]
![[clasificacion-de-machine-learning.webp]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/KytW151dpqU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Algunos conceptos básicos

1.  **Datos de entrenamiento**: Conjunto de datos utilizado para enseñar a un modelo de aprendizaje automático a reconocer patrones y realizar predicciones. Estos datos incluyen ejemplos de entradas y las respuestas esperadas.

2.  **Algoritmo**: Es el proceso o conjunto de reglas matemáticas que un modelo de aprendizaje automático utiliza para aprender de los datos de entrenamiento y ajustar sus parámetros.

3.  [[Entrenamiento]]: Proceso mediante el cual un modelo de aprendizaje automático ajusta sus parámetros internos para mejorar su capacidad de realizar predicciones a partir de los datos de entrenamiento.

4.  [[Validación]]: Proceso de evaluar el rendimiento de un modelo de aprendizaje automático utilizando un conjunto de datos separado de los datos de entrenamiento. La validación ayuda a detectar si el modelo está sobreajustado o si generaliza bien a nuevos datos.

5.  [[Sobreajuste (Overfitting)]]: Situación en la que un modelo de aprendizaje automático se ajusta demasiado a los datos de entrenamiento y no generaliza bien a nuevos ejemplos.

6.  [[Subajuste (Underfitting)]]: Situación en la que un modelo de aprendizaje automático no captura la estructura subyacente de los datos de entrenamiento y tiene un rendimiento deficiente tanto en el conjunto de entrenamiento como en el de validación.

7.  [[Función de pérdida]]: Medida cuantitativa de cuán lejos están las predicciones del modelo de los resultados reales. El objetivo del entrenamiento es minimizar esta función.

8.  [[Gradiente descendente]]: Método de optimización utilizado para minimizar la función de pérdida ajustando iterativamente los parámetros del modelo en función del gradiente (derivada) de la función de pérdida.

9.  [[Aprendizaje supervisado]]: Tipo de aprendizaje automático en el que el modelo se entrena con datos etiquetados, es decir, con ejemplos de entradas y las salidas correspondientes. Ejemplos de tareas de aprendizaje supervisado incluyen clasificación y regresión.
   
10. Aprendizaje pasivo: El modelo se entrena con un conjunto fijo de datos de entrenamiento etiquetados que se proporcionan de antemano. El modelo no tiene control sobre la selección de los ejemplos de entrenamiento, sino que simplemente aprende a partir de los datos que se le proporcionan.

11. Aprendizaje activo: el modelo tiene un papel activo en la selección de los ejemplos de entrenamiento. En lugar de recibir un conjunto fijo de datos de entrenamiento, el modelo puede solicitar que se etiqueten nuevos datos seleccionados por él mismo. El modelo utiliza la información obtenida a partir de estos nuevos datos etiquetados para mejorar su rendimiento en la tarea de aprendizaje.

12.  [[Aprendizaje no supervisado]]: Tipo de aprendizaje automático en el que el modelo se entrena con datos no etiquetados, es decir, solo con ejemplos de entradas sin las salidas correspondientes. El objetivo es encontrar estructuras o patrones ocultos en los datos. Ejemplos de tareas de aprendizaje no supervisado incluyen agrupamiento (clustering) y reducción de dimensionalidad.

13.  [[Aprendizaje por refuerzo]]: Tipo de aprendizaje automático en el que un agente aprende a tomar decisiones a través de interacciones con su entorno. El agente recibe retroalimentación en forma de recompensas o castigos y busca maximizar la recompensa acumulada a lo largo del tiempo.

14.  [[Clasificación]]: Tarea de aprendizaje supervisado en la que un modelo predice a qué categoría pertenece una entrada dada. Por ejemplo, clasificar correos electrónicos como spam o no spam.

15.  [[Regresión lineal]]: Tarea de aprendizaje supervisado en la que un modelo predice un valor continuo a partir de una entrada dada. Por ejemplo, predecir el precio de una casa basado en sus características.

16.  [[Clustering]]): Tarea de aprendizaje no supervisado en la que un modelo divide un conjunto de datos en grupos o clústeres basados en la similitud entre los ejemplos.

17.  [[Reducción de dimensionalidad]]: Tarea de aprendizaje no supervisado en la que un modelo reduce la cantidad de variables (dimensiones) en un conjunto de datos, manteniendo la mayor cantidad de información posible. Ejemplos de técnicas de reducción de dimensionalidad incluyen PCA (Análisis de componentes principales) y t-SNE.

18.  [[Validación cruzada (Cross-validation)]]: Técnica utilizada para evaluar el rendimiento de un modelo de aprendizaje automático dividiendo el conjunto de datos en subconjuntos y realizando múltiples iteraciones de entrenamiento y validación.

19.  **Redes neuronales artificiales**: Familia de modelos de aprendizaje automático inspirados en la estructura y funcionamiento del cerebro humano. Consisten en capas de nodos o neuronas interconectadas que procesan información y aprenden a realizar tareas complejas. vease [[Redes Neuronales Artificiales]]

20.  **Deep learning (Aprendizaje profundo)**: Subcampo del aprendizaje automático que se centra en el uso de redes neuronales artificiales con múltiples capas ocultas. Estos modelos son capaces de aprender representaciones jerárquicas de los datos y han demostrado un gran éxito en tareas como el procesamiento del lenguaje natural y la visión por computadora. [[Deep Learning]]

21.  [[Hiperparámetros]]: Parámetros de un modelo de aprendizaje automático que no se aprenden durante el entrenamiento, sino que se ajustan manualmente o mediante técnicas de optimización. Ejemplos de hiperparámetros incluyen la tasa de aprendizaje, la cantidad de capas en una red neuronal y el número de árboles en un bosque aleatorio.

22.  [[Regularización]]: Técnica utilizada para reducir el sobreajuste en modelos de aprendizaje automático, añadiendo un término de penalización a la función de pérdida que favorece modelos más simples. Ejemplos de técnicas de regularización incluyen L1 y L2 (Lasso y Ridge).