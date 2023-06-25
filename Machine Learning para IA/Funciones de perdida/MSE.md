El MSE, o Mean Squared Error (Error Cuadrático Medio en español), es una medida de error muy utilizada en machine learning, especialmente en problemas de [[Regresión]].

El MSE mide la media de los cuadrados de los errores. Los "errores" son las diferencias entre los valores pronosticados por el modelo y los valores reales. Cuadrar cada diferencia tiene dos propósitos principales:

1. Hacer que cada término sea positivo: dado que estamos sumando todos estos términos, no queremos que los errores positivos y negativos se cancelen entre sí.

2. Ponderar más los errores grandes: al elevar al cuadrado cada término, se da más peso a los errores grandes.

El MSE se calcula de la siguiente manera:

$$\Large
\begin{equation}
MSE = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2
\end{equation}
$$

Donde:

- "n" es el número total de observaciones (o puntos de datos)
- "actual" es el valor real
- "predicción" es el valor que el modelo ha predicho

En resumen, el MSE es una métrica que nos da una idea general de la magnitud de error de nuestro modelo. Cuanto menor sea el MSE, mejor será el modelo. Sin embargo, debido a que eleva al cuadrado los errores, puede dar una imagen engañosamente grave si hay errores muy grandes. Es por eso que siempre es útil considerar otras métricas de error también.