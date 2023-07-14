El boosting es un método de aprendizaje automático que busca mejorar la precisión de las predicciones mediante la combinación de varias "hipótesis débiles" en una "hipótesis fuerte". Las hipótesis débiles se generan a través de una secuencia de modelos de aprendizaje que se entrenan en diferentes versiones de los datos de entrenamiento. Cada modelo se añade al conjunto con el objetivo de corregir los errores de predicción del conjunto actual.

![[Pasted image 20230708195107.png]]

La idea principal detrás del boosting es que, aunque cada uno de los modelos de aprendizaje puede ser débil por sí mismo (es decir, puede tener un rendimiento ligeramente mejor que el azar), la combinación de muchos de estos modelos débiles puede producir un modelo fuerte con un rendimiento mucho mejor. 

Los algoritmos de boosting funcionan de **manera iterativa**. En cada iteración, se añade un nuevo modelo al conjunto con el objetivo de corregir los errores de los modelos ya existentes. **Cada nuevo modelo se entrena de tal manera que se centra especialmente en los casos que fueron mal clasificados por los modelos anteriores**. Esto se logra al **ajustar los pesos** de las instancias de entrenamiento de tal manera que los casos mal clasificados en la iteración anterior se ponderan más en la iteración actual.

![[Pasted image 20230708195343.png]]
![[Pasted image 20230708195943.png]]
![[Pasted image 20230708200020.png]]

Existen varias variantes del boosting, entre las que se incluyen [[AdaBoost]], [[Gradient Boosting]] y XGBoost, cada una con sus propias particularidades y ajustes específicos.

Por ejemplo, AdaBoost (Adaptive Boosting) es un algoritmo de boosting que ajusta los pesos de las instancias de entrenamiento en cada iteración de tal manera que los casos mal clasificados por el modelo actual se ponderan más en el entrenamiento del próximo modelo. 

El Gradient Boosting, por otro lado, utiliza el descenso de gradiente para minimizar la pérdida residual (es decir, la diferencia entre las predicciones actuales y los valores reales). En cada iteración, se añade un nuevo modelo que busca minimizar esta pérdida residual.

Finalmente, XGBoost (Extreme Gradient Boosting) es una implementación optimizada del Gradient Boosting que está diseñada para ser más eficiente y flexible. XGBoost incorpora varias técnicas avanzadas, como la regularización para prevenir el sobreajuste, y el manejo inteligente de los valores faltantes.

Es importante destacar que, **aunque el boosting puede mejorar considerablemente la precisión de las predicciones, también puede llevar a un sobreajuste si se utiliza de manera inapropiada**. En particular, si se añaden demasiados modelos al conjunto (es decir, si se realizan demasiadas iteraciones), el conjunto puede acabar ajustándose demasiado a los datos de entrenamiento y generalizando mal a los datos nuevos. Por lo tanto, es crucial utilizar técnicas como la validación cruzada para ajustar el número de iteraciones y evitar el sobreajuste.

En resumen, el boosting es un poderoso enfoque de aprendizaje automático que puede mejorar significativamente la precisión de las predicciones al combinar múltiples hipótesis débiles en una hipótesis fuerte. Sin embargo, su uso debe ser manejado con cuidado para evitar el [[Sobreajuste (Overfitting)]].


# Lectura

https://towardsdatascience.com/boosting-algorithms-explained-d38f56ef3f30

<iframe width="560" height="315" src="https://www.youtube.com/embed/LxcGKNV5-p4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>