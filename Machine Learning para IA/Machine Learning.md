El **Machine Learning** o **Aprendizaje Automático** es una rama de la Inteligencia Artificial (IA) que se centra en la creación de modelos y algoritmos que pueden aprender de y hacer predicciones o decisiones basadas en los datos. En lugar de ser programados explícitamente para realizar una tarea específica, estos modelos son entrenados usando grandes cantidades de datos y algoritmos que les permiten mejorar su rendimiento con el tiempo.

Dentro del Aprendizaje Automático, hay tres componentes clave que necesitamos entender:

1. **Tarea (T)**: Es el objetivo específico o la tarea que el sistema de aprendizaje automático está diseñado para realizar. Ejemplos de tareas incluyen la clasificación (por ejemplo, determinar si un correo electrónico es spam o no), la regresión (por ejemplo, predecir el precio de una casa basándose en características como el tamaño y la ubicación), el agrupamiento (por ejemplo, segmentar a los clientes en diferentes grupos según su comportamiento de compra) y la detección de anomalías (por ejemplo, encontrar transacciones fraudulentas en tarjetas de crédito).

2. **Métrica de desempeño (P)**: Es la manera de medir qué tan bien un modelo de aprendizaje automático está realizando su tarea. Hay varias métricas de desempeño que pueden ser usadas, dependiendo de la tarea. Algunos ejemplos incluyen la precisión, la exhaustividad, la puntuación F1 (para tareas de clasificación), el error cuadrático medio (para tareas de regresión), y la puntuación de silueta (para tareas de agrupamiento).

3. **Tipo de experiencia (E)**: Es la forma en que el modelo aprende de los datos. Esto puede incluir el aprendizaje supervisado (donde el modelo aprende de un conjunto de datos etiquetados), el aprendizaje no supervisado (donde el modelo aprende de un conjunto de datos no etiquetados), y el aprendizaje por refuerzo (donde el modelo aprende a través de la experimentación y la retroalimentación en forma de recompensas y castigos).

Por lo tanto, el proceso de aprendizaje automático implica elegir una tarea específica, definir una métrica de desempeño y proporcionar la experiencia adecuada para que el modelo pueda aprender y mejorar.


![[Pasted image 20230416182840.png]]


# Tipos de Aprendizaje en Machine Learning

Existen diversas formas de categorizar los tipos de aprendizaje en el Machine Learning, a continuación se detallan algunas de ellas:

1. **Según los tipos de respuestas**:

   - **Clasificación**: La tarea consiste en predecir una categoría o clase. Por ejemplo, clasificar correos electrónicos en 'spam' o 'no spam'.
   - **Regresión**: La tarea es predecir un valor numérico continuo. Por ejemplo, predecir el precio de una casa en función de sus características.

2. **Exactitud de las respuestas**:

   - **Exacto**: Se espera que el modelo proporcione una respuesta precisa y correcta.
   - **Inexacto**: El modelo puede proporcionar una respuesta aproximada y aún así ser considerado útil.

3. **Según enfoque estadístico**:

   - **Distribución**: Los modelos pueden asumir una distribución particular de los datos (por ejemplo, normal).
   - **Función de pérdida**: Esta es una medida de qué tan mal el modelo predice el resultado. Diferentes tipos de tareas pueden requerir diferentes funciones de pérdida. vease [[Función de pérdida]]
   - **Error empírico**: Este es el error que el modelo comete en el conjunto de entrenamiento. vease [[Error empírico]]
   - **Generalización/Inferencia**: Se refiere a la capacidad del modelo de funcionar bien en datos nuevos, no vistos durante el entrenamiento. [[Generalización (inferencia)]]

4. **Según la propiedad de los datos disponibles y pregunta a responder**:

   - **Supervisado**: El modelo aprende de un conjunto de datos etiquetado (es decir, cada ejemplo de entrenamiento tiene una salida objetivo asociada). vease [[Aprendizaje supervisado]]
   - **No supervisado**: El modelo aprende de un conjunto de datos no etiquetado (es decir, no hay salidas objetivo). vease [[Aprendizaje no supervisado]]

5. **Según participantes y roles**:

   - **Activo**: El modelo puede solicitar etiquetas para ejemplos específicos.
   - **Pasivo**: El modelo aprende de las etiquetas que se le proporcionan sin influencia sobre qué ejemplos se etiquetan.
   - **Refuerzo**: El modelo aprende a través de la retroalimentación en términos de recompensas y castigos. vease [[Aprendizaje por refuerzo]]

6. **Según cuándo ocurre el aprendizaje**:

   - **Online**: El modelo se entrena y actualiza a medida que llegan nuevos datos.
   - **Offline**: El modelo se entrena con un conjunto de datos fijo y luego se utiliza sin cambios.
   - **Combinado**: Combinación de los dos enfoques anteriores, por ejemplo, entrenamiento offline inicial seguido de refinamiento online.


# Video 

<iframe width="560" height="315" src="https://www.youtube.com/embed/KytW151dpqU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



![[Pasted image 20230707124515.png]]