La validación cruzada es una técnica utilizada en el [[Machine Learning]] para evaluar la capacidad de generalización de un modelo y evitar el [[Sobreajuste (Overfitting)]]. **Es especialmente útil cuando se dispone de un conjunto de datos limitado**. La validación cruzada implica dividir el conjunto de datos en un número determinado de subconjuntos o "**folds**" y, a continuación, entrenar y validar el modelo en cada combinación única de estos subconjuntos.

![[Pasted image 20230416190444.png]]

El proceso de validación cruzada consta de los siguientes pasos:

1.  **Dividir el conjunto de datos**: El conjunto de datos se divide en K subconjuntos (o "folds") de aproximadamente el mismo tamaño. El valor de K suele ser 5 o 10, pero puede variar según el tamaño y las características del conjunto de datos.

2.  **Entrenamiento y validación**: Se entrena el modelo K veces. En cada iteración, se utiliza un subconjunto diferente como conjunto de validación, y los K-1 subconjuntos restantes se combinan para formar el conjunto de entrenamiento. Después de entrenar el modelo en el conjunto de entrenamiento, se evalúa su rendimiento en el conjunto de validación.

3.  **Rendimiento promedio**: Después de completar las K iteraciones, se calcula la métrica de rendimiento promedio (como precisión, error cuadrático medio, etc.) en todos los conjuntos de validación. Este valor promedio proporciona una estimación más robusta del rendimiento del modelo en datos no vistos en comparación con la evaluación en un único conjunto de validación.


La validación cruzada ofrece varias ventajas:

-   Permite una estimación más precisa y confiable del rendimiento del modelo en datos no vistos, ya que se evalúa en múltiples subconjuntos de datos.
-   Ayuda a identificar si un modelo está sobreajustando los datos de entrenamiento, ya que el rendimiento del modelo en los conjuntos de validación puede ser significativamente peor que en el conjunto de entrenamiento.
-   Facilita la selección de modelos y la elección de hiperparámetros óptimos, ya que se pueden comparar las métricas de rendimiento promedio de diferentes modelos y configuraciones.

Sin embargo, la validación cruzada también puede ser computacionalmente costosa, especialmente para conjuntos de datos grandes y modelos complejos, ya que requiere entrenar y validar el modelo varias veces. En tales casos, se pueden utilizar enfoques alternativos, como la validación cruzada estratificada o la validación cruzada de series temporales, que tienen en cuenta las características específicas del conjunto de datos y pueden ser más eficientes.