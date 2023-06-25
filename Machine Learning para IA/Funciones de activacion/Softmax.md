Softmax es una [[Función de Activación]] utilizada en el contexto del [[Machine Learning]] y las [[Redes Neuronales Artificiales]]. Esta función toma un vector de números reales y produce un nuevo vector en el que cada elemento se encuentra en el rango de 0 a 1, y la suma de todos los elementos es igual a 1. Es decir, la función softmax mapea los valores de entrada en una distribución de probabilidad.

Matemáticamente, la función softmax se define como:
$$\Large
\text{{softmax}}(x_i) = \frac{{e^{x_i}}}{{\sum_{j} e^{x_j}}} \quad \text{{para todo }} i
$$

La función softmax es utilizada comúnmente en problemas de [[Regresión logística#Regresión logística multinomial (Softmax)]] En la regresión logística multinomial, se busca clasificar una variable dependiente categórica con más de dos categorías utilizando una combinación lineal de variables independientes. La función softmax se aplica a la salida de la combinación lineal para obtener una distribución de probabilidad sobre las distintas categorías.

La relación entre softmax y la regresión logística multinomial radica en que la función softmax permite asignar probabilidades a cada una de las categorías de salida en un problema de clasificación multinomial. Cada elemento del vector de salida softmax representa la probabilidad de pertenecer a una categoría específica, y la suma de todas las probabilidades es igual a 1.