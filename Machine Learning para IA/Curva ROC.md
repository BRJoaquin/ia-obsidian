La Curva de Característica Operativa del Receptor (ROC, por sus siglas en inglés) es una herramienta gráfica utilizada para evaluar el rendimiento de un modelo de clasificación binaria. Esta curva se construye trazando la tasa de verdaderos positivos (TPR o Sensibilidad) en el eje vertical y la tasa de falsos positivos (FPR) en el eje horizontal.

![[Pasted image 20230708165816.png]]

Estas cuatro medidas son formas de evaluar la efectividad de un algoritmo de clasificación. Aquí están sus definiciones y relaciones con los otros scores:

- TPR (Tasa de Verdaderos Positivos o Sensibilidad): Es la proporción de verdaderos positivos que son identificados correctamente. Es decir, de todas las observaciones positivas, ¿cuántas se clasificaron correctamente?

$$
TPR = \frac{TP}{TP+FN}
$$

- FPR (Tasa de Falsos Positivos): Es la proporción de verdaderos negativos que se identifican incorrectamente como positivos. De todas las observaciones negativas, ¿cuántas se clasificaron incorrectamente como positivas?

$$
FPR = \frac{FP}{FP+TN}
$$

- FNR (Tasa de Falsos Negativos o Error de Tipo II): Es la proporción de verdaderos positivos que se clasifican incorrectamente como negativos. De todas las observaciones positivas, ¿cuántas se clasificaron incorrectamente como negativas?

$$
FNR = \frac{FN}{FN+TP} = 1 - TPR
$$

- TNR (Tasa de Verdaderos Negativos o Especificidad): Es la proporción de verdaderos negativos que se identifican correctamente. De todas las observaciones negativas, ¿cuántas se clasificaron correctamente?

$$
TNR = \frac{TN}{TN+FP} = 1 - FPR
$$


El objetivo de una curva ROC es mostrar cómo varía la relación entre las tasas de verdaderos positivos y falsos positivos cuando se cambia el umbral de clasificación.

En la curva ROC, un clasificador perfecto se ubicará en la esquina superior izquierda del gráfico, indicando una TPR de 1 y una FPR de 0. En contraste, un clasificador aleatorio se representará como una línea diagonal desde la esquina inferior izquierda hasta la esquina superior derecha.

Además de la curva en sí, a menudo se utiliza una medida llamada [[AUC-ROC]] para cuantificar el rendimiento del clasificador. Esta medida resume el rendimiento del clasificador a lo largo de todos los umbrales posibles, proporcionando una sola medida de efectividad del modelo. Un AUC de 1.0 indica un clasificador perfecto, mientras que un AUC de 0.5 sugiere un rendimiento no mejor que el azar.

![[Pasted image 20230708170017.png]]