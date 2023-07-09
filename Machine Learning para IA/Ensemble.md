Los métodos de conjunto, o "Ensemble methods", son técnicas que crean múltiples modelos y luego los combinan para producir resultados mejorados. Este enfoque aprovecha la "sabiduría de la multitud", en el sentido de que a menudo se obtiene un mejor resultado al combinar las respuestas de varios modelos diferentes en lugar de elegir un solo modelo.

![[Pasted image 20230708183543.png]]

# Por que usar ensamble?

- **Varianza estadística:** La varianza estadística se refiere a la variabilidad en las estimaciones de los parámetros de un modelo debido a la aleatoriedad en la muestra de datos de entrenamiento. En otras palabras, si entrenamos el mismo modelo con diferentes muestras de datos, obtendremos diferentes resultados simplemente debido a la aleatoriedad en las muestras. Al combinar múltiples hipótesis mediante técnicas de conjunto, podemos promediar estos resultados y reducir esta variabilidad. Esto generalmente hace que las predicciones sean más estables y precisas. Esto es especialmente cierto en el caso de algoritmos con alta varianza como los árboles de decisión, donde pequeños cambios en los datos pueden resultar en modelos muy diferentes. Aquí, los métodos de conjunto como el Bagging pueden ser muy efectivos.

- **Varianza computacional:** La varianza computacional se refiere a la variabilidad en los resultados debido a la aleatoriedad en el algoritmo de aprendizaje. Algunos algoritmos de aprendizaje automático, como el k-means o los algoritmos basados en gradiente estocástico, tienen un componente aleatorio y pueden llegar a soluciones diferentes dependiendo de su inicialización. Al combinar múltiples hipótesis, podemos reducir la sensibilidad de nuestro modelo final a estas fluctuaciones aleatorias y obtener un modelo más robusto.

- **Sesgo inductivo (o de representación):** El sesgo inductivo se refiere a las suposiciones que un algoritmo de aprendizaje automático hace sobre el problema. Cada algoritmo de aprendizaje tiene su propio sesgo inductivo que lo guía a preferir ciertas soluciones sobre otras. Por ejemplo, un árbol de decisión prefiere soluciones que pueden expresarse como una serie de decisiones basadas en características individuales, mientras que un modelo lineal prefiere soluciones que son combinaciones lineales de características. Al combinar múltiples hipótesis, podemos potencialmente capturar diferentes aspectos del problema y superar las limitaciones de un único sesgo inductivo. Los métodos de conjunto como el Boosting o el Stacking son particularmente útiles en este sentido.
  
![[Pasted image 20230708184428.png]]

# Combinación de hipótesis 

## Regresión

![[Pasted image 20230708184845.png]]

En algunos algoritmos de aprendizaje automático, se utilizan múltiples modelos o hipótesis y las predicciones de cada uno se combinan de alguna manera para obtener una predicción final. Un método común de combinación de hipótesis es el promedio simple, donde las predicciones de cada modelo se suman y se dividen por el número de modelos. Esta es una forma de conjunto que puede reducir la varianza y mejorar la precisión de la predicción.

![[Pasted image 20230708184955.png]]

Otro método de combinación de hipótesis es la suma pesada, donde cada modelo tiene un peso asociado que refleja su importancia relativa o su rendimiento en el conjunto de entrenamiento. Los modelos que tienen un mejor rendimiento tendrán un peso más alto y tendrán una mayor influencia en la predicción final.

![[Pasted image 20230708184855.png]]

Cuando las hipótesis son independientes, es menos probable que cometan los mismos errores en los mismos datos. Por lo tanto, la combinación de hipótesis independientes puede resultar en un rendimiento superior al de cualquier hipótesis individual. Este es el principio subyacente de muchos métodos de ensamblaje, como Bagging y Random Forests.

![[Pasted image 20230708185024.png]]

Si los sesgos de las hipótesis individuales son pequeños, entonces la combinación de hipótesis a través de promedios o sumas ponderadas puede reducir aún más el sesgo. Sin embargo, si los sesgos son grandes, la combinación de hipótesis puede no ser capaz de superar este sesgo y el rendimiento puede seguir siendo bajo.

# **Navaja de Occam (Occam's razor)**

![[Pasted image 20230708185219.png]]

Este es un principio de solución de problemas que sugiere que, entre las explicaciones competidoras, la más simple es la mejor. En términos de aprendizaje automático, esto sugiere que los modelos más simples que explican bien los datos son preferibles a los modelos más complejos. Esto se basa en la idea de que los modelos más simples son menos propensos a sobreajustar los datos y, por lo tanto, es más probable que generalicen bien a nuevos datos. Sin embargo, es importante tener en cuenta que la simplicidad y la complejidad de un modelo deben evaluarse en relación con los datos y la tarea en cuestión.

## Clasificación

Los algoritmos de conjunto son técnicas para combinar las predicciones de varios modelos de aprendizaje automático. En el contexto de la clasificación, hay varias formas de combinar las predicciones:

1. **Voto Mayoritario**: En el voto mayoritario, cada clasificador en el conjunto vota por una clase y la clase con la mayoría de los votos es la predicción final.

   $$\Large \hat{y} = \arg \max_{k} \sum_{i=1}^{N} I(h_{i}(\textbf{x}) = k) $$

   donde $N$ es el número de clasificadores, $h_{i}(\textbf{x})$ es la predicción del i-ésimo clasificador, $I$ es la función indicadora que es 1 si su argumento es verdadero y 0 en caso contrario, y $\hat{y}$ es la predicción final.
![[Pasted image 20230708185813.png]]

2. **Voto Pesado**: En el voto pesado, cada voto se pondera de acuerdo con la importancia relativa del clasificador.

   $$\Large \hat{y} = \arg \max_{k} \sum_{i=1}^{N} w_{i} I(h_{i}(\textbf{x}) = k) $$

   donde $w_{i}$ es el peso del i-ésimo clasificador.
![[Pasted image 20230708185942.png]]

3. **Soft-Voting**: En el soft-voting, cada clasificador proporciona una probabilidad para cada clase, y estas probabilidades se promedian para obtener la predicción final.

   $$\Large \hat{y} = \arg \max_{k} \frac{1}{N} \sum_{i=1}^{N} p_{i,k} $$

   donde $p_{i,k}$ es la probabilidad predicha por el i-ésimo clasificador para la clase $k$.
![[Pasted image 20230708185958.png]]

# Tipos

Hay tres tipos principales de métodos de conjunto: Bagging, Boosting y Stacking.

1. **Bagging:** Bagging, que significa Bootstrap Aggregating, implica tomar muestras aleatorias con reemplazo del conjunto de datos y entrenar un modelo para cada muestra. Luego, los resultados de todos los modelos se combinan, generalmente mediante votación mayoritaria (para problemas de clasificación) o promedio (para problemas de regresión). El algoritmo más conocido de bagging es el "Random Forest", que agrega una capa de aleatoriedad adicional al seleccionar un subconjunto aleatorio de características en cada división. vease [[Bagging]]

2. **Boosting:** Boosting implica entrenar una serie de modelos, donde cada modelo posterior se enfoca en corregir los errores realizados por los modelos anteriores. Los modelos se ponderan en función de su rendimiento, y estos pesos se tienen en cuenta al combinar las respuestas de los modelos. Ejemplos de algoritmos de boosting incluyen AdaBoost, Gradient Boosting y XGBoost. vease [[Boosting]]
   
3. **Stacking:** Stacking es un enfoque más sofisticado donde se entrenan varios modelos diferentes, y luego se entrena un segundo nivel de modelos (llamados meta-modelos) que toman las predicciones de los primeros modelos como entradas y hacen una predicción final. Este enfoque puede combinar las fortalezas de varios modelos diferentes y a menudo produce resultados muy buenos. vease [[Stacking]]


# Lecturas

https://sebastianraschka.com/pdf/lecture-notes/stat451fs20/07-ensembles__notes.pdf



