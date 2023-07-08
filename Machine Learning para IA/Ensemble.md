Los métodos de conjunto, o "Ensemble methods", son técnicas que crean múltiples modelos y luego los combinan para producir resultados mejorados. Este enfoque aprovecha la "sabiduría de la multitud", en el sentido de que a menudo se obtiene un mejor resultado al combinar las respuestas de varios modelos diferentes en lugar de elegir un solo modelo.

![[Pasted image 20230708183543.png]]

# Por que usar ensamble?

- **Varianza estadística:** La varianza estadística se refiere a la variabilidad en las estimaciones de los parámetros de un modelo debido a la aleatoriedad en la muestra de datos de entrenamiento. En otras palabras, si entrenamos el mismo modelo con diferentes muestras de datos, obtendremos diferentes resultados simplemente debido a la aleatoriedad en las muestras. Al combinar múltiples hipótesis mediante técnicas de conjunto, podemos promediar estos resultados y reducir esta variabilidad. Esto generalmente hace que las predicciones sean más estables y precisas. Esto es especialmente cierto en el caso de algoritmos con alta varianza como los árboles de decisión, donde pequeños cambios en los datos pueden resultar en modelos muy diferentes. Aquí, los métodos de conjunto como el Bagging pueden ser muy efectivos.

- **Varianza computacional:** La varianza computacional se refiere a la variabilidad en los resultados debido a la aleatoriedad en el algoritmo de aprendizaje. Algunos algoritmos de aprendizaje automático, como el k-means o los algoritmos basados en gradiente estocástico, tienen un componente aleatorio y pueden llegar a soluciones diferentes dependiendo de su inicialización. Al combinar múltiples hipótesis, podemos reducir la sensibilidad de nuestro modelo final a estas fluctuaciones aleatorias y obtener un modelo más robusto.

- **Sesgo inductivo (o de representación):** El sesgo inductivo se refiere a las suposiciones que un algoritmo de aprendizaje automático hace sobre el problema. Cada algoritmo de aprendizaje tiene su propio sesgo inductivo que lo guía a preferir ciertas soluciones sobre otras. Por ejemplo, un árbol de decisión prefiere soluciones que pueden expresarse como una serie de decisiones basadas en características individuales, mientras que un modelo lineal prefiere soluciones que son combinaciones lineales de características. Al combinar múltiples hipótesis, podemos potencialmente capturar diferentes aspectos del problema y superar las limitaciones de un único sesgo inductivo. Los métodos de conjunto como el Boosting o el Stacking son particularmente útiles en este sentido.


# Tipos

Hay tres tipos principales de métodos de conjunto: Bagging, Boosting y Stacking.

1. **Bagging:** Bagging, que significa Bootstrap Aggregating, implica tomar muestras aleatorias con reemplazo del conjunto de datos y entrenar un modelo para cada muestra. Luego, los resultados de todos los modelos se combinan, generalmente mediante votación mayoritaria (para problemas de clasificación) o promedio (para problemas de regresión). El algoritmo más conocido de bagging es el "Random Forest", que agrega una capa de aleatoriedad adicional al seleccionar un subconjunto aleatorio de características en cada división.

2. **Boosting:** Boosting implica entrenar una serie de modelos, donde cada modelo posterior se enfoca en corregir los errores realizados por los modelos anteriores. Los modelos se ponderan en función de su rendimiento, y estos pesos se tienen en cuenta al combinar las respuestas de los modelos. Ejemplos de algoritmos de boosting incluyen AdaBoost, Gradient Boosting y XGBoost.
   
3. **Stacking:** Stacking es un enfoque más sofisticado donde se entrenan varios modelos diferentes, y luego se entrena un segundo nivel de modelos (llamados meta-modelos) que toman las predicciones de los primeros modelos como entradas y hacen una predicción final. Este enfoque puede combinar las fortalezas de varios modelos diferentes y a menudo produce resultados muy buenos.


**Bagging**

El bagging se basa en la idea de que la combinación de muchos modelos independientes puede reducir la varianza y mejorar el rendimiento. Cada modelo se entrena en un subconjunto bootstrap del conjunto de datos (una muestra aleatoria con reemplazo), y luego las predicciones de todos los modelos se combinan. El método más común para combinar las predicciones es simplemente tomar la moda (para la clasificación) o la media (para la regresión) de las predicciones.

Un ejemplo común de bagging es el bosque aleatorio. Un bosque aleatorio es un conjunto de árboles de decisión, cada uno de los cuales se entrena en un subconjunto bootstrap del conjunto de datos y solo se considera un subconjunto aleatorio de características en cada división.

**Boosting**

A diferencia del bagging, que se basa en la combinación de modelos independientes, el boosting se basa en la idea de construir una secuencia de modelos que se construyen de manera adaptativa para centrarse en las áreas donde los modelos anteriores han tenido un mal rendimiento. En cada etapa, se da más peso a los ejemplos que fueron clasificados erróneamente en las etapas anteriores, de modo que los modelos posteriores se centren más en ellos.

Hay varios algoritmos de boosting, pero uno común es AdaBoost. AdaBoost comienza entrenando un modelo débil (por ejemplo, un pequeño árbol de decisión) en los datos. Luego, aumenta los pesos de los ejemplos que el modelo clasificó incorrectamente y entrena un nuevo modelo en los datos ponderados. Este proceso se repite, cada vez ajustando los pesos de los ejemplos en función de las predicciones del último modelo. Finalmente, AdaBoost hace sus predicciones finales tomando un voto ponderado de las predicciones de todos los modelos.

**Stacking**

El stacking es un enfoque un poco más sofisticado para combinar múltiples modelos. En lugar de simplemente tomar una votación o promedio de las predicciones de los modelos, el stacking entrena un segundo nivel de modelos (llamados meta-modelos) para hacer la predicción final basándose en las predicciones de los modelos de primer nivel.

Los modelos de primer nivel se entrenan como de costumbre, pero luego, en lugar de hacer una predicción final, sus predicciones se utilizan como características para entrenar a los modelos de segundo nivel. Este enfoque permite que el modelo de conjunto tome en cuenta las interacciones entre las predicciones de los diferentes modelos, lo que puede llevar a un rendimiento mejorado.

Por último, vale la pena destacar que aunque los métodos de conjunto a menudo pueden mejorar el rendimiento, también vienen con un costo en términos de complejidad y tiempo de entrenamiento. Es importante sopesar estos costos con los beneficios potenciales al decidir si utilizar un método de conjunto.