La regresión lineal es un algoritmo de aprendizaje supervisado que se utiliza en machine learning y estadísticas. Su objetivo es predecir una variable objetivo (también conocida como variable dependiente) basándose en una o más variables de entrada (también conocidas como variables independientes o predictores).

La regresión lineal asume una relación lineal entre las variables de entrada y la variable objetivo. En otras palabras, se puede representar matemáticamente como:

$$
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


# Estimación de coeficientes

La regresión lineal simple tiene la siguiente forma:

$$\Large
y = a + bX + \epsilon
$$

Donde:
- $y$ es la variable objetivo (la que intentamos predecir).
- $X$ es la variable predictora (la que usamos para hacer la predicción).
- $a$ es la intercepción o coeficiente de sesgo. Es el valor de $y$ cuando $X$ es 0.
- $b$ es el coeficiente de la variable predictora $X$. Representa la pendiente de la línea, es decir, cuánto cambia $y$ por cada cambio unitario en $X$.
- $\epsilon$ es el error, que es la diferencia entre la predicción del modelo y el valor real.

La idea es encontrar los valores de $a$ y $b$ que minimizan la suma de los cuadrados de los errores ($\epsilon$). Esto se conoce como el método de [[Mínimos Cuadrados Ordinarios]](Ordinary Least Squares, OLS).

En un modelo de regresión lineal múltiple, donde hay más de una variable predictora, la ecuación se expande para incluir todos los predictores, pero la idea general sigue siendo la misma:

$$\Large
y = a + b_1X_1 + b_2X_2 + ... + b_nX_n + \epsilon
$$

Aquí, $X_1, X_2, ..., X_n$ son las variables predictoras y $b_1, b_2, ..., b_n$ son sus coeficientes respectivos.


# Regresión lineal vs Regresión logística

La regresión lineal se utiliza para predecir valores continuos mientras que la regresión logística se utiliza para predecir probabilidades de resultados binarios. Ambos métodos son valiosos en función del contexto y los objetivos de la investigación.



<iframe width="560" height="315" src="https://www.youtube.com/embed/k964_uNn3l0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
