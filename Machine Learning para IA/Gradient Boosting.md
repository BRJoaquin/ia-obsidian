
Gradient Boosting es un método de aprendizaje automático que produce un modelo de predicción en forma de un conjunto de modelos de predicción débiles, normalmente [[Árbol de decisión]]. A diferencia de otros métodos de ensamble como AdaBoost, Gradient Boosting **optimiza una función de pérdida diferenciable, como el error cuadrático medio (MSE) en el caso de regresión o la entropía cruzada en el caso de la clasificación**.

# ¿Cómo funciona Gradient Boosting?

El algoritmo Gradient Boosting construye un modelo predictivo en etapas, donde en cada etapa se agrega un nuevo modelo débil que intenta corregir los errores residuales del modelo construido hasta el momento.

En el primer paso, se crea un modelo débil (por ejemplo, un árbol de decisión) que predice la variable objetivo basándose en las características de entrada. Este modelo no será perfecto y habrá un residuo, es decir, una diferencia entre las predicciones y los verdaderos valores de la variable objetivo.

A continuación, se construye un segundo modelo que intenta predecir este residuo. Es decir, intenta aprender dónde y cuánto se equivocó el primer modelo. Este segundo modelo se suma al primer modelo para obtener un modelo conjunto que es una mejor predicción que el primero.

El proceso continúa de esta manera, añadiendo nuevos modelos que intentan corregir los residuos del modelo conjunto construido hasta el momento. Este procedimiento se repite hasta que se alcanza un número predeterminado de modelos o hasta que los residuos no pueden ser reducidos más.

![[Pasted image 20230708204055.png]]

El sobreajuste puede ser un problema en Gradient Boosting si se utiliza un número demasiado grande de etapas o árboles de demasiada profundidad. Para evitar esto, se puede utilizar una técnica llamada "early stopping", donde se detiene el entrenamiento si el error de validación no mejora después de un cierto número de etapas.

## Importancia de las características

Al igual que en Random Forest, en Gradient Boosting también se puede medir la importancia de las características observando cuánto contribuyen a la disminución de la función de pérdida. Las características que contribuyen más a esta disminución son consideradas las más importantes.

# VS AdaBoost

Ambos, AdaBoost y Gradient Boosting, son técnicas de ensemble que construyen un fuerte predictor a partir de una combinación de múltiples predictores débiles, generalmente árboles de decisión. Sin embargo, hay algunas diferencias clave en cómo funcionan.

**1. Enfoque de actualización del modelo:** AdaBoost actualiza los pesos de las observaciones para mejorar el rendimiento en la próxima iteración. En otras palabras, las observaciones que se predicen incorrectamente en una iteración reciben un mayor peso en la siguiente iteración, por lo que el próximo clasificador se "centra" en esas observaciones difíciles.

Por otro lado, Gradient Boosting se centra en los residuos, o errores de predicción, de la iteración anterior. En lugar de cambiar los pesos de las observaciones, Gradient Boosting ajusta la próxima predicción para minimizar el error residual de la anterior.

**2. Pérdida de función:** AdaBoost utiliza una función de pérdida exponencial, que es más sensible a los outliers que la utilizada por Gradient Boosting. Gradient Boosting puede utilizar cualquier función de pérdida diferenciable, lo que la hace más flexible.

**3. Regularización:** Gradient Boosting incorpora un parámetro de tasa de aprendizaje para controlar la contribución de cada árbol y prevenir el sobreajuste. Esto no es común en AdaBoost.

**4. Uso común:** AdaBoost es a menudo mejor para problemas de clasificación binaria, mientras que Gradient Boosting es más efectivo en problemas de regresión (aunque puede ser utilizado para clasificación también).

Es importante tener en cuenta que a pesar de estas diferencias, ambos algoritmos son potentes técnicas de ensemble que pueden proporcionar resultados muy precisos en una amplia gama de problemas. La elección entre los dos a menudo depende del problema específico en cuestión y del conocimiento del dominio.

# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/zblsrxc7XpM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

