El aprendizaje supervisado es una categoría de técnicas de aprendizaje automático en la que los modelos se entrenan utilizando datos etiquetados, es decir, con ejemplos de entradas y las salidas correspondientes. En este enfoque, el algoritmo utiliza la información proporcionada en los datos de entrenamiento para ajustar sus parámetros internos y aprender a realizar predicciones.

El objetivo del aprendizaje supervisado es desarrollar un modelo que pueda generalizar y realizar predicciones precisas en datos nuevos y no vistos, basándose en el conocimiento adquirido durante el entrenamiento. Estos modelos son útiles para una amplia variedad de aplicaciones, como la clasificación de imágenes, el diagnóstico médico, la predicción de precios y la traducción automática, entre otros.

![[aprendizaje_supervisado.webp]]

Algunas técnicas y tareas comunes en el aprendizaje supervisado incluyen:

1.  **[[Clasificación]]**

2.  **[[Regresión]]**

3.  **Métricas de evaluación**: Para evaluar el rendimiento de un modelo de aprendizaje supervisado, se utilizan métricas de evaluación específicas. Para tareas de clasificación, algunas métricas comunes incluyen precisión, exhaustividad (recall), F1-score y área bajo la curva ROC (AUC-ROC). Para tareas de regresión, se utilizan métricas como el error cuadrático medio (MSE), el error absoluto medio (MAE) y el coeficiente de determinación (R²).

4.  **[[Validación]] y selección de modelos**: Para evitar el [[Sobreajuste (Overfitting)]] y garantizar que el modelo generalice bien a nuevos datos, se utiliza un proceso de validación, que consiste en dividir los datos en conjuntos de entrenamiento y validación (o utilizar validación cruzada) y comparar el rendimiento del modelo en ambos conjuntos. Además, se pueden explorar diferentes configuraciones de [[Hiperparámetros]] y modelos para seleccionar la mejor combinación.

El aprendizaje supervisado es un enfoque ampliamente utilizado en aprendizaje automático y ha demostrado ser efectivo en una variedad de tareas y aplicaciones. **Sin embargo, requiere la disponibilidad de datos etiquetados, lo que puede ser costoso o difícil de obtener en algunos casos**.