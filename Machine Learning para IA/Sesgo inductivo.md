El sesgo inductivo en el [[Machine Learning]] se refiere a las suposiciones y restricciones que un algoritmo de aprendizaje hace al intentar aprender un [[Modelo (Hipotesis)]] a partir de los datos. Estas suposiciones guían el proceso de aprendizaje y afectan la selección del modelo final entre las posibles hipótesis que explican los datos. Todos los algoritmos de aprendizaje automático tienen cierto nivel de sesgo inductivo, ya que es necesario para reducir la complejidad de la búsqueda de soluciones y encontrar una [[Modelo (Hipotesis)]] que se ajuste a los datos observados.

El sesgo inductivo puede manifestarse de varias formas, como:

1.  **Suposiciones sobre la estructura del modelo**: Algunos algoritmos de aprendizaje automático hacen suposiciones específicas sobre la forma del modelo que se ajusta a los datos. Por ejemplo, la [[Regresión lineal]] asume que la relación entre las [[Características]] y la [[Variable objetivo]] es lineal, mientras que otros algoritmos pueden suponer que la relación es no lineal o que tiene cierta estructura específica.

2.  **Suposiciones sobre la distribución de los datos**: Algunos algoritmos hacen suposiciones sobre la distribución de los datos de entrada, como la normalidad de los datos en el caso del análisis discriminante lineal.

3.  **Preferencias por modelos más simples**: Algunos algoritmos de aprendizaje automático, como la regresión lineal regularizada o las máquinas de vectores de soporte, tienen un sesgo inductivo que favorece modelos más simples o menos complejos para evitar el [[Sobreajuste (Overfitting)]].


**El sesgo inductivo es un aspecto importante del aprendizaje automático porque determina cómo se selecciona el modelo a partir de los datos y cómo el algoritmo generaliza a datos no vistos**. Un sesgo inductivo apropiado puede mejorar la capacidad de generalización de un algoritmo y evitar problemas como el sobreajuste. **Sin embargo, un sesgo inductivo inadecuado puede conducir a un modelo que no se ajusta bien a los datos o que no puede capturar las relaciones subyacentes en los datos.**

> A fines prácticos es elegir el modelo de aprendizaje (ejemplo KNN) y los [[Hiperparámetros]] para el modelo (ejemplo el K en KNN, o la profundidad en un árbol de decisión)

Es importante tener en cuenta el sesgo inductivo al seleccionar y ajustar algoritmos de aprendizaje automático para un problema específico. La elección del algoritmo adecuado y la comprensión de sus suposiciones y restricciones pueden ser fundamentales para lograr un buen rendimiento y una generalización efectiva en aplicaciones del mundo real.

![[Pasted image 20230422152658.png]]

# Ejemplo

Claro, consideremos un problema de clasificación muy simple con dos características y dos clases. Imagina que tenemos un conjunto de datos que consta de puntos en un plano bidimensional, y nuestro objetivo es entrenar un modelo para clasificar nuevos puntos en una de las dos clases.

Supongamos que tenemos dos algoritmos de aprendizaje automático para resolver este problema: la regresión logística y un árbol de decisión.

**Regresión logística** ([[Regresión logística]]): Este algoritmo asume que la relación entre las características y la probabilidad de pertenencia a una clase sigue una función logística. Esto implica que el límite de decisión entre las dos clases será una línea recta en el plano bidimensional. El sesgo inductivo en este caso es la suposición de que la frontera entre las clases es lineal.

**Árbol de decisión** ([[Árbol de decisión]]: Este algoritmo construye un modelo basado en reglas basadas en las características de los datos. En el plano bidimensional, esto se traduciría en fronteras de decisión que son líneas verticales u horizontales. El sesgo inductivo en este caso es la suposición de que la frontera entre las clases se puede describir mediante reglas basadas en una única característica a la vez.

Ahora, supongamos que la relación real entre las características y las clases en nuestros datos no es lineal, sino que sigue una forma más compleja, como un círculo. La regresión logística, debido a su sesgo inductivo, no podrá capturar esta relación, ya que solo puede aprender límites de decisión lineales. Por otro lado, un árbol de decisión podría capturar la relación de manera más efectiva, ya que su sesgo inductivo permite aprender límites de decisión más flexibles.

En resumen, el sesgo inductivo se refiere a las suposiciones inherentes que un algoritmo de aprendizaje automático hace sobre la estructura de los datos y las relaciones subyacentes. Estas suposiciones afectan la capacidad del algoritmo para aprender y generalizar a partir de los datos. En este ejemplo, la regresión logística tiene un sesgo inductivo que favorece las fronteras de decisión lineales, mientras que el árbol de decisión tiene un sesgo inductivo que favorece las fronteras de decisión basadas en reglas simples.


<iframe width="560" height="315" src="https://www.youtube.com/embed/EuBBz3bI-aA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

> [!quote]
> Correction: [4:06](https://www.youtube.com/watch?v=EuBBz3bI-aA&t=246s) I say that the difference in fits between the training dataset and the testing dataset is called Variance. However, I should have said that the difference is a consequence of variance. Technically, variance refers to the amount by which the predictions would change if we fit the model to a different training data set.

> El [[Sesgo]] no es lo mismo que el sesgo inductivo