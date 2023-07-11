La **regresión lineal** es un algoritmo de [[Aprendizaje supervisado]] que se utiliza en [[Machine Learning]] y en estadística para predecir un valor de salida continuo a partir de una o más variables de entrada. Es un algoritmo de aprendizaje muy versátil, fácil de entender y tiene una amplia gama de aplicaciones.

# Regresión Lineal Simple y Múltiple

La regresión lineal se divide en dos tipos: **simple** y **múltiple**, dependiendo del número de variables de entrada utilizadas.

La **regresión lineal simple** usa una sola variable de entrada para predecir una variable de salida. El objetivo de la regresión lineal simple es encontrar una línea que mejor se ajuste a los datos. Esta línea es representada por la ecuación:

$$\Large
y = \beta_0 + \beta_1x + \epsilon$$

donde:
- $y$ es la variable de salida que queremos predecir,
- $x$ es la variable de entrada,
- $\beta_0$ es la ordenada en el origen o el punto de intersección de la línea con el eje y,
- $\beta_1$ es la pendiente de la línea, y
- $\epsilon$ es el error aleatorio.

La **regresión lineal múltiple** extiende la regresión lineal simple al usar dos o más variables de entrada para predecir una variable de salida. La ecuación es:

$$\Large
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon$$

donde ahora hay n términos $\beta_ix_i$ para n variables de entrada $x_i$.

# Regresión Polinomial

Cuando la relación entre las variables de entrada y la variable de salida no es lineal, se puede usar la regresión polinomial para modelar la relación. En la regresión polinomial, transformamos nuestras variables de entrada elevándolas a una potencia (por ejemplo, si nuestra variable de entrada es $x$, podríamos usar $x^2$, $x^3$, etc. como nuevas variables de entrada). Esto permite modelar relaciones curvilíneas entre las variables de entrada y la variable de salida.

Un ejemplo de una regresión polinomial sería:

$$\Large
y = \beta_0 + \beta_1x + \beta_2x^2 + \epsilon$$

Es importante tener en cuenta que la regresión polinomial puede ser propensa al sobreajuste si se elige un grado demasiado alto para el polinomio.

Aunque puede parecer contradictorio, la regresión polinomial **se considera una forma de regresión lineal**. Aunque la relación entre las variables independientes y la variable dependiente es polinomial (o no lineal), se llama "regresión lineal" porque los coeficientes de la ecuación de regresión se estiman de manera lineal.

En otras palabras, el término "lineal" en "regresión lineal" no se refiere a la forma de la ecuación de regresión, sino a cómo se estiman los coeficientes $\beta$ de la ecuación. En la regresión lineal (incluyendo la regresión polinomial), estos coeficientes se estiman de manera lineal a partir de las variables independientes. 

Así, una regresión polinomial de grado 2 podría tener la siguiente forma:

$$y = \beta_0 + \beta_1x + \beta_2x^2 + \epsilon$$

Aunque $x^2$ es una relación no lineal con $y$, la relación entre los coeficientes ($\beta_0$, $\beta_1$, $\beta_2$) y las variables independientes ($1$, $x$, $x^2$) es lineal, por lo que se considera regresión lineal.


# MLE, NLL y MSE en Regresión Lineal Simple

Para encontrar los coeficientes $\beta$ en la regresión lineal, necesitamos algún criterio que nos permita determinar qué tan bien nuestra línea se ajusta a los datos. Esto nos lleva a los conceptos de [[Máxima Verosimilitud (MLE)]], [[Negative Log-Likelihood (NLL)]] y [[MSE]].

El **Método de Máxima Verosimilitud (MLE)** busca los coeficientes que maximizan la verosimilitud de los datos observados, dado el modelo.

En la práctica, es común minimizar el **Logaritmo Negativo de Verosimilitud (NLL)**, que es simplemente el negativo del logaritmo de la función de verosimilitud. En el caso de la regresión lineal, minimizar el NLL es equivalente a minimizar el **Error Cuadrático Medio (MSE)**, que es una medida comúnmente utilizada para evaluar el rendimiento de los modelos de regresión.

El MSE se calcula como:

$$\Large MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

donde $y_i$ son los valores observados, $\hat{y}_i$ son los valores predichos y $n$ es el número de observaciones.

# Atributos Categóricos: One-hot Encoding y Label Encoding

En la regresión lineal, nuestras variables de entrada deben ser numéricas. Sin embargo, a menudo nos encontramos con **atributos categóricos**, es decir, variables que toman un número limitado de categorías en lugar de valores numéricos. Para poder usar estos atributos en la regresión lineal, necesitamos convertirlos en una forma numérica. Dos técnicas comunes para esto son el [[One-hot encoding]] y el [[Label encoding]].

El **One-hot encoding** implica convertir cada categoría de una variable categórica en una nueva variable binaria (0 o 1). Por ejemplo, si tenemos una variable categórica "color" con categorías "rojo", "verde" y "azul", el one-hot encoding crearía tres nuevas variables binarias: "es_rojo", "es_verde" y "es_azul".

El **Label encoding**, por otro lado, simplemente asigna un número entero único a cada categoría. Por ejemplo, podríamos asignar 1 a "rojo", 2 a "verde" y 3 a "azul". Sin embargo, hay que tener cuidado con el label encoding, ya que puede introducir un orden artificial en las categorías que puede no ser adecuado.

# Regresión lineal vs Regresión logística

La regresión lineal se utiliza para predecir valores continuos mientras que la [[Regresión logística]] se utiliza para predecir probabilidades de resultados binarios o multiclase. Ambos métodos son valiosos en función del contexto y los objetivos de la investigación.



<iframe width="560" height="315" src="https://www.youtube.com/embed/k964_uNn3l0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>




- **Regresión polinomial**: 
Cuando la relación entre las variables de entrada y la variable de salida no es lineal, se puede usar la regresión polinomial para modelar la relación. En la regresión polinomial, transformamos nuestras variables de entrada elevándolas a una potencia (por ejemplo, si nuestra variable de entrada es $x$, podríamos usar $x^2$, $x^3$, etc. como nuevas variables de entrada). Esto permite modelar relaciones curvilíneas entre las variables de entrada y la variable de salida.

Un ejemplo de una regresión polinomial sería:

$$y = \beta_0 + \beta_1x + \beta_2x^2 + \epsilon$$

Es importante tener en cuenta que la regresión polinomial puede ser propensa al sobreajuste si se elige un grado demasiado alto para el polinomio.
- **Regresión regularizada**: Cuando tenemos muchas variables de entrada, podemos tener el problema de la multicolinealidad y el sobreajuste. Para combatir esto, se pueden utilizar técnicas de regularización como Ridge, Lasso y Elastic Net que añaden un término de penalización a la función de coste que reduce los coeficientes de las variables de entrada. Esto ayuda a prevenir el sobreajuste y puede mejorar la interpretabilidad del modelo al reducir la cantidad de variables de entrada que se utilizan.

- **Regresión logística**: Cuando la variable de salida es binaria (por ejemplo, sí/no o 0/1), podemos utilizar la regresión logística. Aunque no es una extensión de la regresión lineal en el sentido estricto, la regresión logística se basa en muchos de los mismos conceptos y es un método importante en la caja de herramientas de cualquier científico de datos.

Espero que este resumen te haya proporcionado una sólida introducción a la regresión lineal y sus conceptos relacionados. ¡Buena suerte con tu aprendizaje!
