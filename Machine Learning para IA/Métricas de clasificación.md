![[Pasted image 20230708161217.png]]

En problemas de clasificación, existen varias métricas que nos permiten evaluar el rendimiento de un modelo:

1. **Exactitud (Accuracy)**: Es la proporción de predicciones correctas. Se calcula como el número de predicciones correctas dividido por el número total de predicciones.

   $$\text{Accuracy} = \frac{\text{Número de predicciones correctas}}{\text{Número total de predicciones}}$$

2. **Precisión (Precision)**: Es la proporción de predicciones positivas que son realmente positivas. En otras palabras, es la proporción de verdaderos positivos (TP) entre todos los que fueron clasificados como positivos (TP + FP). vease [[Precisión]]

   $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
> ¿Cuan creıble soy cuando digo “positivo”?

3. **Recall (Sensibilidad | Recuperacion)**: Es la proporción de verdaderos positivos que se identificaron correctamente. Es la proporción de verdaderos positivos (TP) entre todos los que son realmente positivos (TP + FN).

   $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
> ¿Cuantos “positivos” logre detectar?

4. **F1-Score**: Es una medida que combina precisión y recall en una sola métrica. Es la media armónica de precisión y recall, y su valor estará más cerca del valor más pequeño entre precisión y recall.

   $$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

5. **AUC-ROC**: El área bajo la curva de la característica operativa del receptor (AUC-ROC) es una métrica que nos permite evaluar el rendimiento de un clasificador binario. La curva ROC es un gráfico que muestra el rendimiento de un modelo de clasificación en todos los niveles de umbral de clasificación.

Además de estas métricas, la **matriz de confusión** es una herramienta útil que nos permite visualizar el rendimiento de un algoritmo de clasificación. Nos muestra los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos.

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

