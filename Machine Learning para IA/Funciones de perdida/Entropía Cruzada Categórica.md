La **Entropía Cruzada Categórica** (cross entropy loss) es una [[Función de pérdida]] que se utiliza comúnmente en problemas de [[Clasificación]] multiclase. Esta función de pérdida es adecuada para problemas de clasificación donde cada entrada puede pertenecer a una sola categoría.

La Entropía Cruzada Categórica mide la similitud entre dos distribuciones de probabilidad: la distribución de probabilidad verdadera (la cual es one-hot en problemas de clasificación) y la distribución de probabilidad predicha por el modelo.

En forma de ecuación, la Entropía Cruzada Categórica se puede expresar como:

$$\Large
H(y, \hat{y}) = - \sum_{i} y_{i} \log(\hat{y}_{i})
$$

donde $y$ es el vector de etiquetas verdaderas en codificación one-hot, $\hat{y}$ es el vector de predicciones del modelo y $i$ recorre todas las clases.

Por ejemplo, si tenemos tres clases y para una entrada específica la etiqueta verdadera es la clase 2 (representada por el vector one-hot [0, 1, 0]), y el modelo predice las probabilidades [0.1, 0.6, 0.3] para cada clase, entonces la Entropía Cruzada Categórica sería:

$$
H(y, \hat{y}) = - (0 * \log(0.1) + 1 * \log(0.6) + 0 * \log(0.3)) = - \log(0.6)
$$

Un valor de Entropía Cruzada Categórica más bajo significa que las predicciones del modelo están más cerca de las etiquetas verdaderas.

