
La **Función de Pérdida de Entropía Cruzada**, también conocida como log loss, es una [[Función de pérdida]] utilizada en el [[Machine Learning]] cuando el objetivo es la [[Clasificación]]. Es especialmente útil para problemas de clasificación binaria y se usa comúnmente en [[Redes Neuronales Artificiales]] y [[Regresión logística]].

La entropía cruzada mide la disimilitud entre la distribución de probabilidad predicha por el modelo y la distribución de probabilidad real (las etiquetas verdaderas). En otras palabras, busca minimizar la diferencia entre las predicciones del modelo y los datos verdaderos.

La fórmula para la pérdida de entropía cruzada en clasificación binaria es:

$$\Large
L = -\frac{1}{N} \sum_{i=1}^{N} [y_i log(\hat{y}_i) + (1 - y_i) log(1 - \hat{y}_i)]
$$

donde:
- $N$ es el número de observaciones.
- $y_i$ es la etiqueta verdadera de la observación $i$.
- $\hat{y}_i$ es la probabilidad predicha de la clase positiva para la observación $i$.

El objetivo durante el entrenamiento es minimizar esta pérdida. Cuando la predicción del modelo se acerca a la etiqueta verdadera, la pérdida de entropía cruzada se acerca a cero.

La entropía cruzada es una medida de pérdida adecuada cuando queremos tener en cuenta la confianza del modelo en sus predicciones. Los errores de clasificación con alta confianza se penalizan más que los errores con baja confianza.

