La regresión lineal es un algoritmo de aprendizaje supervisado que se utiliza en machine learning y estadísticas. Su objetivo es predecir una variable objetivo (también conocida como variable dependiente) basándose en una o más variables de entrada (también conocidas como variables independientes o predictores).

La regresión lineal asume una relación lineal entre las variables de entrada y la variable objetivo. En otras palabras, se puede representar matemáticamente como:

$$ \Large
y = a + b*X
$$
Aquí:

- 'y' es la variable objetivo que estamos tratando de predecir o estimar.
- 'X' representa las variables de entrada.
- 'a' es el término de intercepción, es decir, el valor de 'y' cuando 'X' es 0.
- 'b' es el coeficiente de la variable de entrada, representa la pendiente de la línea, es decir, el cambio en 'y' por cada cambio unitario en 'X'.

El algoritmo de regresión lineal aprende los parámetros 'a' y 'b' de los datos de entrenamiento. Lo hace minimizando el error cuadrático medio ([[MSE]]), que es la diferencia cuadrada media entre las predicciones del modelo y los valores reales. En otras palabras, intenta trazar una línea a través de los datos de entrada que minimiza la suma de los cuadrados de los errores.

En el caso de múltiples variables de entrada, esto se conoce como regresión lineal múltiple. En este caso, la ecuación se expande para incluir todos los predictores:
$$\large
y = a + b1*X1 + b2*X2 + ... + bn*Xn
$$
La regresión lineal es una técnica simple pero poderosa que se usa ampliamente tanto en estadísticas como en machine learning. Es particularmente útil cuando tienes una relación lineal clara entre las variables de entrada y la variable objetivo.

# Regresión lineal vs Regresión logística

La regresión lineal se utiliza para predecir valores continuos mientras que la [[Regresión logística]] se utiliza para predecir probabilidades de resultados binarios o multiclase. Ambos métodos son valiosos en función del contexto y los objetivos de la investigación.



<iframe width="560" height="315" src="https://www.youtube.com/embed/k964_uNn3l0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
