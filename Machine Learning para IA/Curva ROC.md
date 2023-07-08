La Curva de Característica Operativa del Receptor (ROC, por sus siglas en inglés) es una herramienta gráfica utilizada para evaluar el rendimiento de un modelo de clasificación binaria. Esta curva se construye trazando la tasa de verdaderos positivos (TPR o Sensibilidad) en el eje vertical y la tasa de falsos positivos (FPR) en el eje horizontal.

La TPR y la FPR se calculan como sigue:

- TPR = TP / (TP + FN)
- FPR = FP / (FP + TN)

Donde:
TP = Verdaderos Positivos,
FN = Falsos Negativos,
FP = Falsos Positivos, y
TN = Verdaderos Negativos.

El objetivo de una curva ROC es mostrar cómo varía la relación entre las tasas de verdaderos positivos y falsos positivos cuando se cambia el umbral de clasificación.

En la curva ROC, un clasificador perfecto se ubicará en la esquina superior izquierda del gráfico, indicando una TPR de 1 y una FPR de 0. En contraste, un clasificador aleatorio se representará como una línea diagonal desde la esquina inferior izquierda hasta la esquina superior derecha.

Además de la curva en sí, a menudo se utiliza una medida llamada Área Bajo la Curva ROC (AUC-ROC) para cuantificar el rendimiento del clasificador. Esta medida resume el rendimiento del clasificador a lo largo de todos los umbrales posibles, proporcionando una sola medida de efectividad del modelo. Un AUC de 1.0 indica un clasificador perfecto, mientras que un AUC de 0.5 sugiere un rendimiento no mejor que el azar.
