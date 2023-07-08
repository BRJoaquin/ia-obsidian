
![[Pasted image 20230625165818.png]]

# Regresión logística

La regresión logística es una técnica de modelado estadístico que se utiliza comúnmente para predecir la probabilidad de un evento binario. En otras palabras, es una forma de modelar la relación entre un conjunto de variables independientes (también conocidas como variables explicativas o características) y una variable dependiente categórica que puede tomar dos posibles valores.

# Logits y su relación con la regresión logística

En el contexto de la regresión logística, los logits son el resultado de la transformación logit, que es simplemente el logaritmo de las probabilidades pronosticadas dividido por uno menos las probabilidades pronosticadas. En otras palabras, es el logaritmo del odds ratio, a menudo llamado log-odds.

La regresión logística se llama así porque utiliza la función logit como enlace para conectar la combinación lineal de los predictores con la respuesta binomial. Específicamente, en lugar de modelar la probabilidad $P(Y=1|X)$ directamente, la regresión logística modela el log-odds de la probabilidad.

$$
\text{logit}(P(Y=1|X)) = \log\left(\frac{P(Y=1|X)}{1 - P(Y=1|X)}\right) = \beta_0 + \beta_1X
$$

La función logit es la inversa de la función sigmoide, que es utilizada para convertir la combinación lineal de los predictores en una probabilidad.

# ¿Cómo funciona la regresión logística?

A diferencia de la regresión lineal, que utiliza una combinación lineal de características para predecir un valor continuo, la regresión logística transforma su salida utilizando la función logística (también conocida como función sigmoide) para devolver una probabilidad. La función sigmoide tiene la siguiente forma:

$$
f(x) = \frac{1}{1 + e^{-x}}
$$

Esta función convierte cualquier valor real en un valor en el rango (0, 1), lo que la hace útil para interpretar la salida del modelo como una probabilidad.

La regresión logística modela la probabilidad de que la variable dependiente pertenezca a una "clase" particular (por ejemplo, la probabilidad de que un correo electrónico sea "spam" o "no spam") dadas las características. Esta probabilidad se puede expresar como:

$$
P(Y=1|X) = \frac{1}{1 + e^{-(b_0 + b_1X)}}
$$

donde:
- $P(Y=1|X)$ es la probabilidad condicional de que la variable dependiente sea igual a 1 dado el valor de las variables independientes.
- $b_0$ y $b_1$ son los coeficientes que se aprenden del conjunto de entrenamiento.
- $X$ es el vector de variables independientes.

El lado derecho de la ecuación es simplemente la función logística (sigmoide) aplicada a una combinación lineal de las características. El resultado es una probabilidad que puede interpretarse fácilmente.

# Estimación de los coeficientes

Los coeficientes del modelo (los $b$ en la ecuación anterior) se suelen estimar mediante el método de máxima verosimilitud. La idea es encontrar los coeficientes que maximizan la "verosimilitud" de los datos observados.

Para la regresión logística, esto significa encontrar los coeficientes que hacen que las probabilidades predichas por el modelo sean lo más cercanas posible a las verdaderas etiquetas de las observaciones en el conjunto de datos de entrenamiento.

Formalmente, la función de verosimilitud $L$ para la regresión logística se define como:

$$
L(b_0, b_1) = \prod_{i: y_i=1} P(y_i = 1|X) \prod_{i: y_i=0} (1 - P(y_i = 1|X))
$$

y queremos encontrar los valores de $b_0$ y $b_1$ que maximizan esta función. A menudo es más fácil trabajar con el logaritmo de la función de verosimilitud, que simplifica el cálculo sin cambiar la solución ([[Negative Log-Likelihood (NLL)]].

## Aprendizaje

En la **Regresión Logística**, los pesos (o coeficientes) para las variables predictoras se ajustan durante el proceso de entrenamiento para minimizar la función de pérdida, que a menudo es la pérdida de [[Entropía Cruzada binaria (log loss)]] en este caso.

![[Pasted image 20230708111531.png]]

El objetivo del ajuste de pesos es encontrar los valores que hacen que las predicciones del modelo se alineen lo más cerca posible de las etiquetas verdaderas de los datos de entrenamiento. 

El ajuste de los pesos se realiza generalmente a través de un algoritmo de optimización, como el **descenso de gradiente**. En cada iteración del entrenamiento, el algoritmo de optimización calcula el gradiente de la función de pérdida con respecto a cada peso, y luego actualiza los pesos en la dirección que reduce la pérdida.

Para un peso $w_i$ y una tasa de aprendizaje $\alpha$, la actualización de pesos puede expresarse como:

$$\Large
w_i := w_i - \alpha \frac{\partial L}{\partial w_i}
$$

donde:
- $L$ es la función de pérdida.
- $\frac{\partial L}{\partial w_i}$ es el gradiente de $L$ con respecto a $w_i$.

El tamaño de la actualización depende del gradiente y de la tasa de aprendizaje. Una tasa de aprendizaje más alta resulta en cambios más grandes en los pesos, mientras que una tasa de aprendizaje más baja resulta en cambios más pequeños.

Es importante destacar que el ajuste de los pesos debe hacerse de tal manera que el modelo generalice bien a los nuevos datos, no solo a los datos de entrenamiento. Para evitar el [[Sobreajuste (Overfitting)]], a menudo se utiliza alguna forma de regularización, que añade un término de penalización a la función de pérdida para limitar la magnitud de los pesos.

vease: [[Método de Máxima Verosimilitud]]

# Uso de la regresión logística para la clasificación

Una vez que tenemos un modelo de regresión logística ajustado, podemos usarlo para clasificar nuevas observaciones. Para una observación dada, simplemente calculamos la probabilidad predicha de que la variable dependiente sea igual a 1 (utilizando los coeficientes del modelo y los valores de las características de la observación). Si esta probabilidad es mayor que un cierto umbral (típicamente 0.5), clasificamos la observación como perteneciente a la clase 1; en caso contrario, la clasificamos como perteneciente a la clase 0.

Este umbral se puede ajustar para hacer que el modelo sea más conservador o más liberal en su clasificación de las observaciones como pertenecientes a la clase 1.

# Métricas de evaluación para la regresión logística

Hay varias métricas que se pueden utilizar para evaluar la calidad de un modelo de regresión logística. Algunas de las más comunes son la precisión, el recall, el área bajo la curva ROC (AUC-ROC), la log-loss, entre otras. Cada una de estas métricas tiene sus propios puntos fuertes y debilidades, y la elección de la métrica de evaluación más adecuada depende del problema específico que se esté abordando.

# La regresión logística es un modelo lineal

Es importante destacar que, aunque la regresión logística modela una probabilidad y utiliza una función no lineal (la función logística) para hacerlo, sigue siendo un modelo lineal. Esto es porque la decisión de clasificar una observación como perteneciente a la clase 1 o 0 se basa en si una combinación lineal de las características es mayor o menor que un cierto umbral. Esta linealidad tiene ventajas y desventajas. Por un lado, hace que el modelo sea fácil de interpretar y de calcular. Por otro lado, limita la capacidad del modelo para capturar relaciones complejas entre las características y la variable dependiente.

A pesar de estas limitaciones, la regresión logística sigue siendo una herramienta valiosa y ampliamente utilizada en el análisis estadístico y el aprendizaje automático debido a su simplicidad, eficiencia computacional y facilidad de interpretación.

# Evaluación

El rendimiento de un modelo de Regresión Logística puede ser evaluado utilizando varias métricas, como la precisión, la [[Curva ROC]], el área bajo la curva ROC ([[AUC-ROC]]), la [[Matriz de confusión]], etc.

# Extensiones

## Regresión Logística Multivariada

La regresión logística multivariada es una extensión de la regresión logística que permite múltiples predictores. Cada predictor tiene su propio coeficiente, y estos coeficientes determinan cuánto influye cada predictor en la probabilidad de que la variable de respuesta sea igual a 1.

La fórmula para la regresión logística multivariada es similar a la de la regresión logística simple, pero ahora la combinación lineal incluye todos los predictores:

$$
\text{logit}(P(Y=1|X)) = \beta_0 + \beta_1X_1 + \beta_2X_2 + \ldots + \beta_pX_p
$$

En este caso, $X_1, X_2, \ldots, X_p$ representan los predictores y $\beta_1, \beta_2, \ldots, \beta_p$ sus coeficientes correspondientes.

![[Pasted image 20230708111125.png]]

## Regresión Logística con Polinomios

La regresión logística también puede usarse con predictores polinomiales para modelar relaciones no lineales entre los predictores y la variable de respuesta. Al igual que en la regresión lineal, esto se hace simplemente añadiendo términos polinomiales a la combinación lineal de predictores.

Por ejemplo, un modelo de regresión logística con un predictor cuadrático podría tener la siguiente forma:

$$
\text{logit}(P(Y=1|X)) = \beta_0 + \beta_1X + \beta_2X^2
$$

Esta flexibilidad permite que la regresión logística modele relaciones más complejas entre los predictores y la variable de respuesta que la regresión logística simple.

![[Pasted image 20230708111205.png]]

## Regresión Logística Multiclase: One vs Rest (OVR)

Hasta ahora hemos hablado de regresión logística para clasificación binaria, donde la variable de respuesta tiene solo dos posibles valores. Sin embargo, la regresión logística también puede ser utilizada para la clasificación multiclase, donde la variable de respuesta puede tener más de dos posibles valores.

Un enfoque para la clasificación multiclase con regresión logística es el método de One vs Rest (OVR), también conocido como One vs All (OVA). Este método implica ajustar un modelo de regresión logística separado para cada clase contra todas las demás clases.

Por ejemplo, si tuviéramos un problema de clasificación con tres clases (A, B y C), ajustaríamos tres modelos de regresión logística:

1. Clase A vs Clases B y C
2. Clase B vs Clases A y C
3. Clase C vs Clases A y B

Para hacer una predicción para una nueva observación, simplemente aplicamos cada uno de los modelos a las características de esa observación y escogemos la clase que tiene la mayor probabilidad pronosticada.

Cabe destacar que, aunque el método OVR es intuitivo y fácil de implementar, puede ser problemático cuando las clases están desequilibradas. Si una clase es mucho más común que las demás, entonces el modelo para esa clase puede dominar a los otros modelos, lo que lleva a predicciones sesgadas.

![[Pasted image 20230708111438.png]]


# Ventajas

- Puede proporcionar probabilidades para las predicciones.
- Puede manejar relaciones no lineales.
- Es simple y fácil de implementar.

# Desventajas

- No es capaz de manejar relaciones complejas.
- Tiene dificultades con las variables categóricas con múltiples niveles.
- Es sensible a la colinealidad en los datos.

# Cálculo del error en Regresión Logística

En la regresión logística, comúnmente se utiliza la [[Entropía Cruzada binaria (log loss)]] para calcular el error del modelo. Esta es una métrica adecuada porque la regresión logística es un modelo probabilístico que estima la probabilidad de que una instancia pertenezca a una clase particular.

La pérdida logarítmica para una única instancia se calcula de la siguiente manera:

$$ LogLoss = - [y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y})] $$

Donde:
* $y$ es la etiqueta verdadera (0 o 1).
* $\hat{y}$ es la probabilidad predicha de que la etiqueta sea 1.

Cuando calculamos el error para un conjunto de datos con múltiples instancias, tomamos el promedio de la pérdida logarítmica de todas las instancias. Así, la pérdida logarítmica para un conjunto de datos se calcula como sigue:

$$ LogLoss = - \frac{1}{n} \sum_{i=1}^{n} [y_i \cdot \log(\hat{y}_i) + (1 - y_i) \cdot \log(1 - \hat{y}_i)] $$

Donde:
* $n$ es el número total de instancias en el conjunto de datos.
* $y_i$ es la etiqueta verdadera de la $i$-ésima instancia.
* $\hat{y}_i$ es la probabilidad predicha de que la $i$-ésima instancia pertenezca a la clase 1.

Es importante tener en cuenta que la pérdida logarítmica penaliza fuertemente las predicciones incorrectas que están seguras de su resultado. Por ejemplo, si la etiqueta verdadera es 1 pero el modelo predice una probabilidad muy cercana a 0, la pérdida logarítmica será muy alta.
