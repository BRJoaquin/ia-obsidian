La función de distribución acumulada (FDA) es una función que representa la probabilidad de que una variable aleatoria $X$ tome un valor menor o igual a un valor específico $x$. Se utiliza en teoría de probabilidad y estadística para describir la distribución de probabilidad de una variable aleatoria.

La FDA se denota como $F(x)$ y se define de la siguiente manera:

$$\Large
F(x) = P(X \leq x)
$$
Para una variable aleatoria discreta, la FDA se calcula sumando las probabilidades de todos los posibles resultados de $X$ que son menores o iguales a $x$:

$$\Large
F(x) = \sum_{x_i \leq x} P(X = x_i)
$$

Para una variable aleatoria continua, la FDA se obtiene integrando la función de densidad de probabilidad $f(x)$ desde el límite inferior hasta $x$:

