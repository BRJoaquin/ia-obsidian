RSS es el acrónimo de Residual Sum of Squares (suma de los cuadrados de los residuos) en machine learning, y es una medida comúnmente usada para evaluar la eficacia de un modelo de regresión.

Un residuo es simplemente la diferencia entre el valor actual y el valor pronosticado por el modelo. En otras palabras, es la cantidad que el modelo se "equivoca" en cada predicción individual.

La RSS toma cada uno de estos residuos, los eleva al cuadrado y luego los suma todos juntos. Esto da una medida general de cuánto se está equivocando el modelo.

La RSS se calcula con la siguiente fórmula:

$$\Large
\begin{equation}
RSS = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\end{equation}
$$

Donde:

- $n$ es el número total de observaciones o puntos de datos
- $y_i$ es el valor real de la i-ésima observación
- $\hat{y}_i$ es el valor predicho por el modelo para la i-ésima observación

En esta fórmula, estamos sumando el cuadrado de las diferencias entre los valores reales y los predichos para todas las observaciones. Mientras menor sea el valor de RSS, mejor es el ajuste del modelo a los datos. Sin embargo, al igual que con cualquier métrica, no debe utilizarse sola para evaluar la eficacia de un modelo.