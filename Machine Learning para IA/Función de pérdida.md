Una función de pérdida, también conocida como función de costo o de error, es una función matemática que mide la diferencia entre las predicciones realizadas por un modelo de aprendizaje automático y los valores reales o etiquetas del conjunto de datos. El objetivo del proceso de entrenamiento es minimizar la pérdida, lo que significa ajustar los parámetros del modelo para que las predicciones se acerquen lo más posible a los valores reales.

> En el contexto del aprendizaje automático, $y_i$ y $ŷ_i$ $representan$ lo siguiente:
> -   **$y_i$**: Es la etiqueta o valor real de la variable objetivo para el ejemplo $i$ en el conjunto de datos. En un problema de [[Clasificación]] $y_i$ sería la clase real a la que pertenece el ejemplo $i$, mientras que en un problema de [[Regresión]], $y_i$ sería el valor numérico real asociado con el ejemplo $i$.
> -   **$ŷ_i$**: Es la predicción del modelo para el ejemplo $i$ en el conjunto de datos. Este valor es la salida del modelo de aprendizaje automático cuando se le proporciona el ejemplo $i$ como entrada. En un problema de clasificación, $ŷ_i$ sería la clase predicha por el modelo para el ejemplo $i$, mientras que en un problema de regresión, $ŷ_i$ sería el valor numérico predicho por el modelo para el ejemplo $i$.
>
> La diferencia entre $y_i$ y $ŷ_i$ se utiliza en las funciones de pérdida para evaluar el rendimiento de un modelo de aprendizaje automático.

La elección de la función de pérdida adecuada depende del tipo de problema y del objetivo específico. Algunas funciones de pérdida comunes incluyen:

1.  **Error cuadrático medio (MSE)**: Es una función de pérdida comúnmente utilizada para problemas de regresión. Mide la suma de las diferencias al cuadrado entre las predicciones del modelo y los valores reales. Un valor menor de MSE indica un mejor ajuste del modelo a los datos. vease [[MSE]]

$$\Large
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

Donde $y_i$ es el valor real, $ŷ_i$ es la predicción del modelo y $n$ es el número de ejemplos.

2.  **Entropía cruzada (Cross-Entropy Loss)**: Es una función de pérdida ampliamente utilizada para problemas de clasificación, especialmente en clasificación binaria y multiclase. Mide la discrepancia entre la distribución de probabilidad predicha por el modelo y la distribución real de las etiquetas. La entropía cruzada es menor cuando las predicciones del modelo se acercan a las etiquetas reales.

Para la clasificación binaria: 
$$\Large
	\text{CE} = - \sum_{i=1}^n \left( y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right)
$$

Para la clasificación multiclase: 

$$\Large
\text{CE} = - \sum_{i=1}^n \sum_{j=1}^c y_{ij} \log(\hat{y}_{ij})
$$
Donde $y_{ij}$ es la etiqueta real y $ŷ_{ij}$ es la probabilidad predicha para la clase $j$ en el ejemplo $i$.

3.  **Función de pérdida hinge (Hinge Loss)**: Se utiliza principalmente en máquinas de vectores de soporte (SVM) para problemas de clasificación. La función de pérdida hinge mide el margen entre las predicciones del modelo y las etiquetas reales y busca maximizar este margen.

$$\Large
\text{Hinge Loss} = \max(0, 1 - y_i \hat{y}_i)
$$
Donde $y_i$ es la etiqueta real (-1 o 1) y $ŷ_i$ es la predicción del modelo.

4. **La función de pérdida 0-1**: también conocida como pérdida de clasificación errónea, es una función de pérdida utilizada en problemas de [[Clasificación]]. Esta función de pérdida asigna un valor de 1 cuando la predicción del modelo es incorrecta y un valor de 0 cuando la predicción es correcta.
   
5.  **RSS (Residual Sum of Squares)**: La suma de los cuadrados de los residuos es una medida de la discrepancia entre los valores predichos por el modelo y los valores reales. Es la suma de las diferencias al cuadrado entre las predicciones del modelo y los valores reales.   vease 
   $$\Large RSS = Σ(y_i - ŷ_i)^2$$donde $y_i$ es el valor real, $ŷ_i$ es la predicción del modelo y la suma se realiza sobre todos los ejemplos en el conjunto de datos.
   
6. **RMSE (Root Mean Squared Error)**: El error cuadrático medio es otra medida de la discrepancia entre las predicciones del modelo y los valores reales. Es la raíz cuadrada del promedio de las diferencias al cuadrado entre las predicciones del modelo y los valores reales.
$$\Large RMSE = sqrt((1/n) * Σ(y_i - ŷ_i)^2)$$donde $y_i$ es el valor real, $ŷ_i$ es la predicción del modelo, $n$ es el número de ejemplos en el conjunto de datos y la suma se realiza sobre todos los ejemplos.

El RMSE es una medida de error más interpretable que el RSS, ya que está en la misma escala que los valores de la variable objetivo.

7. **MAE (Mean Absolute Error)**: El error absoluto medio es otra medida de la discrepancia entre las predicciones del modelo y los valores reales. Es el promedio de las diferencias absolutas entre las predicciones del modelo y los valores reales.
$$\Large MAE = (1/n) * Σ|y_i - ŷ_i| $$
donde $y_i$ es el valor real, $ŷ_i$ es la predicción del modelo, $n$ es el número de ejemplos en el conjunto de datos y la suma se realiza sobre todos los ejemplos.

El $MAE$ es menos sensible a los valores atípicos que el $RMSE$, ya que no eleva al cuadrado las diferencias antes de calcular el promedio.

Estas son solo algunas funciones de pérdida comunes, y hay muchas otras que se utilizan en diferentes situaciones y para diferentes tipos de modelos. La elección de la función de pérdida adecuada es esencial para garantizar que el modelo aprenda a hacer predicciones precisas y que el proceso de optimización se realice de manera efectiva.

![[Pasted image 20230509113811.png]]


