La validación cruzada es una técnica utilizada en el [[Machine Learning]] para evaluar la capacidad de generalización de un modelo y evitar el [[Sobreajuste (Overfitting)]]. **Es especialmente útil cuando se dispone de un conjunto de datos limitado**. La validación cruzada implica dividir el conjunto de datos en un número determinado de subconjuntos o "**folds**" y, a continuación, entrenar y validar el modelo en cada combinación única de estos subconjuntos.

![[Pasted image 20230416190444.png]]

El proceso de validación cruzada consta de los siguientes pasos:

1.  **Dividir el conjunto de datos**: El conjunto de datos se divide en K subconjuntos (o "**folds**") de aproximadamente el mismo tamaño. El valor de K suele ser 5 o 10, pero puede variar según el tamaño y las características del conjunto de datos.

2.  **Entrenamiento y validación**: Se entrena el modelo K veces. En cada iteración, se utiliza un subconjunto diferente como conjunto de validación, y los K-1 subconjuntos restantes se combinan para formar el conjunto de entrenamiento. Después de entrenar el modelo en el conjunto de entrenamiento, se evalúa su rendimiento en el conjunto de validación.

3.  **Rendimiento promedio**: Después de completar las K iteraciones, se calcula la métrica de rendimiento promedio (como precisión, error cuadrático medio, etc.) en todos los conjuntos de validación. Este valor promedio proporciona una estimación más robusta del rendimiento del modelo en datos no vistos en comparación con la evaluación en un único conjunto de validación.

![[Pasted image 20230712114624.png]]

La validación cruzada ofrece varias ventajas:

-   Permite una estimación más precisa y confiable del rendimiento del modelo en datos no vistos, ya que se evalúa en múltiples subconjuntos de datos.
  
-   Ayuda a identificar si un modelo está sobreajustando los datos de entrenamiento, ya que el rendimiento del modelo en los conjuntos de validación puede ser significativamente peor que en el conjunto de entrenamiento.
  
-   Facilita la [[Selección de modelo]] y la elección de [[Hiperparámetro]] óptimos, ya que se pueden comparar las métricas de rendimiento promedio de diferentes modelos y configuraciones.
  
-  Rendimiento más estable: Como cada punto de datos se usa tanto para entrenamiento como para validación, los resultados son menos sensibles a la forma en que se dividen los datos.

- Utilización completa de los datos: Todos los datos se utilizan para entrenamiento y validación, lo que es particularmente útil cuando el tamaño del conjunto de datos es pequeño.

- Evaluación de la robustez del modelo: Permite evaluar cuánto varía el rendimiento del modelo con diferentes conjuntos de entrenamiento.

Sin embargo, la validación cruzada también puede ser computacionalmente costosa, especialmente para conjuntos de datos grandes y modelos complejos, ya que requiere entrenar y validar el modelo varias veces. En tales casos, se pueden utilizar enfoques alternativos, como la validación cruzada estratificada o la validación cruzada de series temporales, que tienen en cuenta las características específicas del conjunto de datos y pueden ser más eficientes.

# Ejemplo en código

Aquí está un ejemplo de cómo funciona esto en código:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression()

scores = cross_val_score(model, X, y, cv=5)
print("Cross-validation scores: ", scores)
print("Average cross-validation score: ", scores.mean())
```

# Desventajas

A pesar de sus ventajas, la validación cruzada también tiene algunas desventajas:

- **Costo computacional**: Como se mencionó anteriormente, la validación cruzada puede ser costosa en términos de tiempo y recursos computacionales. Esto es especialmente cierto para los conjuntos de datos grandes y los modelos complejos, donde cada entrenamiento y validación puede llevar mucho tiempo.

- **No es adecuada para todos los tipos de datos**: La validación cruzada asume que los datos son independientes e idénticamente distribuidos (i.i.d.). Sin embargo, esto no siempre es cierto. Por ejemplo, en las series temporales o los datos geoespaciales, las observaciones cercanas pueden estar correlacionadas. En estos casos, una simple división aleatoria de los datos puede resultar en un sesgo en las estimaciones del rendimiento del modelo.

- **Riesgo de sobreajuste a la validación cruzada**: Si se utiliza la validación cruzada para seleccionar hiperparámetros o características del modelo, existe el riesgo de sobreajustar a la validación cruzada. Esto significa que el modelo podría funcionar bien en la validación cruzada pero mal en datos nuevos e independientes.

- **Varianza alta**: Aunque la validación cruzada proporciona una estimación más robusta del rendimiento del modelo que una única división de entrenamiento/prueba, todavía puede tener una varianza alta, especialmente si el número de folds (K) es pequeño. Esto significa que las estimaciones del rendimiento del modelo pueden variar mucho dependiendo de cómo se dividan exactamente los datos.

A pesar de estas desventajas, la validación cruzada sigue siendo una herramienta valiosa para evaluar y mejorar el rendimiento del modelo en muchas situaciones.


<iframe width="560" height="315" src="https://www.youtube.com/embed/6dbrR-WymjI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>