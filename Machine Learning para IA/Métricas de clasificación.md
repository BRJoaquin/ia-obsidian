![[Pasted image 20230708161217.png]]

En problemas de clasificación, existen varias métricas que nos permiten evaluar el rendimiento de un modelo:

1. **Exactitud (Accuracy)**: Es la proporción de predicciones correctas. Se calcula como el número de predicciones correctas dividido por el número total de predicciones.

   $$\text{Accuracy} = \frac{\text{Número de predicciones correctas}}{\text{Número total de predicciones}}$$

2. **Precisión (Precision)**: Es la proporción de predicciones positivas que son realmente positivas. En otras palabras, es la proporción de verdaderos positivos (TP) entre todos los que fueron clasificados como positivos (TP + FP). vease [[Precisión]]

   $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
> ¿Cuan creıble soy cuando digo “positivo”?

3. **Recall (Sensibilidad | Recuperacion)**: Es la proporción de verdaderos positivos que se identificaron correctamente. Es la proporción de verdaderos positivos (TP) entre todos los que son realmente positivos (TP + FN). vease [[Recall]]

   $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
> ¿Cuantos “positivos” logre detectar?

4. **F1-Score**: Es una medida que combina precisión y recall en una sola métrica. Es la media armónica de precisión y recall, y su valor estará más cerca del valor más pequeño entre precisión y recall. vease [[F1-score]]

   $$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

5. **AUC-ROC**: El área bajo la curva de la característica operativa del receptor (AUC-ROC) es una métrica que nos permite evaluar el rendimiento de un clasificador binario. La curva ROC es un gráfico que muestra el rendimiento de un modelo de clasificación en todos los niveles de umbral de clasificación. vease [[AUC-ROC]]

Además de estas métricas, la **matriz de confusión** es una herramienta útil que nos permite visualizar el rendimiento de un algoritmo de clasificación. Nos muestra los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos. vease [[Matriz de confusión]]

# Ejemplos de métricas de clasificación

Para ejemplificar las métricas, consideremos el siguiente conjunto de predicciones para un problema de clasificación binaria:

- Verdaderos Positivos (TP): 100
- Falsos Positivos (FP): 20
- Verdaderos Negativos (TN): 50
- Falsos Negativos (FN): 30

1. **Exactitud (Accuracy)**: Es la proporción de predicciones correctas (TP+TN) entre el total de predicciones.

   $$\text{Accuracy} = \frac{100+50}{100+20+50+30} = 0.75$$

   La exactitud de nuestro modelo es 0.75, o 75%.

2. **Precisión (Precision)**: Es la proporción de verdaderos positivos entre todas las predicciones positivas.

   $$\text{Precision} = \frac{100}{100+20} = 0.83$$

   La precisión de nuestro modelo es 0.83, o 83%.

3. **Recall (Sensibilidad)**: Es la proporción de verdaderos positivos entre todos los valores que son realmente positivos.

   $$\text{Recall} = \frac{100}{100+30} = 0.77$$

   La sensibilidad de nuestro modelo es 0.77, o 77%.

4. **F1-Score**: Es la media armónica de precisión y recall.

   $$F1 = 2 \times \frac{0.83 \times 0.77}{0.83 + 0.77} = 0.80$$

   El F1-Score de nuestro modelo es 0.80, o 80%.

El AUC-ROC es más complicado de calcular a partir de valores específicos ya que requiere cambiar los umbrales de decisión y medir la tasa de verdaderos positivos y la tasa de falsos positivos.

# Importancia

En la elección de la métrica de evaluación adecuada, se debe tener en cuenta el objetivo de la aplicación y el coste de los errores de clasificación. Dependiendo de la aplicación, diferentes errores tendrán diferentes costes. Aquí algunos ejemplos:

1. **Detección de cáncer**: En este caso, queremos minimizar el número de falsos negativos (FN), ya que no detectar un caso de cáncer puede tener graves consecuencias. Por lo tanto, querríamos maximizar el `Recall` (Sensibilidad), que es la proporción de verdaderos positivos entre todos los valores que son realmente positivos. Un modelo con un alto recall asegura que la mayoría de los pacientes con cáncer serán correctamente identificados, aunque a costa de una mayor cantidad de falsos positivos (personas saludables incorrectamente identificadas como enfermas).

2. **Detectar si un correo electrónico es spam**: En este caso, podríamos estar más interesados en minimizar el número de falsos positivos (FP), ya que clasificar un correo electrónico legítimo como spam podría hacer que el destinatario se pierda información importante. Aquí querríamos maximizar la `Precisión`, que es la proporción de verdaderos positivos entre todas las predicciones positivas. Un modelo con alta precisión asegura que la mayoría de los correos identificados como spam realmente lo sean, aunque a costa de no marcar algunos correos spam (falsos negativos).

3. **Recomendaciones de películas**: En un sistema de recomendación, podríamos estar interesados en una combinación de alta precisión y recall, ya que tanto recomendar malas películas (FP) como no recomendar buenas películas (FN) podrían afectar la experiencia del usuario. Aquí podríamos utilizar la métrica `F1-Score`, que combina precisión y recall.

4. **Clasificación de fraude en transacciones bancarias**: En este caso, tanto los falsos positivos (transacciones legítimas marcadas como fraudulentas) como los falsos negativos (transacciones fraudulentas no detectadas) pueden tener un alto costo. Aquí, la elección de la métrica dependerá de cuál de estos errores se considere más costoso.

La elección de la métrica de evaluación debe hacerse teniendo en cuenta el contexto de la aplicación y los costos asociados a los diferentes tipos de errores.

# Otras métricas

## Metricas para problemas desbalanceados

Los problemas de clasificación desbalanceados son aquellos en los que el número de observaciones en una clase es significativamente menor que las observaciones en otras clases. En este caso, usar una métrica de precisión simple puede ser engañoso. Aquí hay algunas métricas recomendadas:

1. **Balanced Accuracy:** Esta métrica se usa cuando los datos de entrenamiento son desbalanceados. Es la media aritmética de la sensibilidad (recall) y la especificidad. 

$$\text{Balanced Accuracy} = \frac{1}{2} (\frac{TP}{TP+FN} + \frac{TN}{TN+FP})$$

2. **Balanced Accuracy con Pesos:** Esta es una versión ponderada de la precisión equilibrada. Los pesos pueden ser proporcionales a la cantidad de ejemplos en cada clase.
   ![[Pasted image 20230708171127.png]]

## Métricas de clasificación multiclase

En problemas de clasificación multiclase, donde se tienen más de dos clases, hay algunas métricas importantes a considerar:

1. **Recall:** En el contexto de clasificación multiclase, el recall se puede calcular para cada clase y luego tomar la media para obtener el recall global. 

$$\text{Recall} = \frac{TP}{TP+FN}$$
![[Pasted image 20230708171218.png]]

2. **Macro Average Recall:** Esta es la media no ponderada de los recalls para cada clase.

$$\text{Macro Average Recall} = \frac{1}{n} \sum_{i=1}^{n} \text{Recall}_i$$
![[Pasted image 20230708171306.png]]

3. **Weighted Categorical Accuracy:** Esta es una versión ponderada de la precisión categórica. En esta métrica, la precisión de cada clase se calcula de forma independiente y luego se promedian, ponderando el promedio por el número de instancias verdaderas para cada clase. Esto ayuda a dar más importancia a las clases que son más prevalentes.
   
![[Pasted image 20230708171409.png]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/yEw9oDdJkT0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/eSo2wvx-gTc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>