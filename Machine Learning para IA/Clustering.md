El clustering, también conocido como agrupamiento, es una tarea de aprendizaje[[Aprendizaje no supervisado]] en la que el objetivo es dividir un conjunto de datos en grupos o clústeres basados en la similitud entre los ejemplos. A diferencia de la [[Clasificación]], donde se proporcionan etiquetas de clase durante el entrenamiento, en el clustering, el modelo debe descubrir por sí mismo la estructura subyacente y los patrones en los datos sin información previa sobre las categorías.

El clustering es útil en situaciones donde no se dispone de datos etiquetados, y se desea analizar, explorar o extraer conocimientos de los datos. Algunas aplicaciones comunes del clustering incluyen la segmentación de clientes, la detección de anomalías, la organización de documentos y la reducción de dimensionalidad.

Algunos algoritmos de clustering populares incluyen:

1.  **K-means**: Es un algoritmo iterativo que busca minimizar la suma de las distancias al cuadrado entre los puntos de datos y sus respectivos centroides de clúster. El algoritmo comienza asignando aleatoriamente K centroides y luego los actualiza iterativamente hasta alcanzar la convergencia. K-means es sensible a la elección inicial de los centroides y al valor de K.
    
2.  **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: Es un algoritmo de clustering basado en densidad que agrupa puntos de datos cercanos en clústeres y trata a los puntos menos densos como ruido. DBSCAN no requiere especificar el número de clústeres, pero necesita parámetros de radio y densidad mínima para determinar qué puntos de datos están conectados.
    
3.  **Agrupamiento jerárquico**: Es un enfoque que construye una jerarquía de clústeres, ya sea utilizando un enfoque ascendente (aglomerativo) o descendente (divisivo). El agrupamiento jerárquico aglomerativo comienza con cada punto de datos como un clúster individual y luego combina iterativamente los clústeres más cercanos hasta que todos los puntos de datos formen un único clúster.
    
4.  **Mixture Models y Expectation-Maximization (EM)**: Los modelos de mezcla, como la mezcla de Gaussianas, representan un conjunto de datos como una combinación de varias distribuciones de probabilidad. El algoritmo EM se utiliza para estimar los parámetros de los modelos de mezcla de manera iterativa, alternando entre la asignación de puntos de datos a componentes de la mezcla (paso E) y la actualización de los parámetros de la mezcla (paso M).
    

La elección del algoritmo de clustering adecuado depende de la naturaleza de los datos y los requisitos de la tarea. A menudo, es necesario experimentar con diferentes algoritmos y parámetros para obtener los resultados deseados.