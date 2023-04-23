La función de distribución acumulada (FDA) es una función que representa la probabilidad de que una variable aleatoria $X$ tome un valor menor o igual a un valor específico $x$. Se utiliza en teoría de probabilidad y estadística para describir la distribución de probabilidad de una variable aleatoria.

La FDA se denota como $F(x)$ y se define de la siguiente manera:

$$\Large
F(x) = P(X \leq x)
$$
Para una variable aleatoria discreta, la FDA se calcula sumando las probabilidades de todos los posibles resultados de $X$ que son menores o iguales a $x$:

$$\Large
F(x) = \sum_{x_i \leq x} P(X = x_i)
$$

Para una [[Variable Aleatoria]] continua, la FDA se obtiene integrando la función de densidad de probabilidad $f(x)$ desde el límite inferior hasta $x$:

$$\Large
F(x) = \int_{-\infty}^{x} f(t) \, dt
$$
La función de distribución acumulada tiene las siguientes propiedades:

1.  F(x) es una función no decreciente: si $x_1 < x_2$, entonces $F(x_1) \leq F(x_2)$.
2. El límite inferior de la FDA es 0 y el límite superior es 1:


# Ejemplo

Supongamos que tenemos una variable aleatoria discreta $X$ que representa el número de fallos en un proceso de fabricación. La variable $X$ puede tomar valores en el conjunto ${0, 1, 2, 3}$ y tiene la siguiente función de probabilidad puntual (FPP):

P(X=0) = 0.5
P(X=1) = 0.3
P(X=2) = 0.1
P(X=3) = 0.1

Queremos calcular la función de distribución acumulada para $X$. Como $X$ es una variable aleatoria discreta, utilizamos la suma de las probabilidades:

$$F(0) = P(X \leq 0) = P(X=0) = 0.5$$
$$F(1) = P(X \leq 1) = P(X=0) + P(X=1) = 0.5 + 0.3 = 0.8 $$
$$F(2) = P(X \leq 2) = P(X=0) + P(X=1) + P(X=2) = 0.5 + 0.3 + 0.1 = 0.9 $$
$$F(3) = P(X \leq 3) = P(X=0) + P(X=1) + P(X=2) + P(X=3) = 0.5 + 0.3 + 0.1  + 0.1 = 1$$

Entonces, la función de distribución acumulada para esta variable aleatoria discreta es:

$$
F(x) = \begin{cases}
0, & \text{si } x < 0 \\
0.5, & \text{si } 0 \leq x < 1 \\
0.8, & \text{si } 1 \leq x < 2 \\
0.9, & \text{si } 2 \leq x < 3 \\
1, & \text{si } 3 \leq x
\end{cases}
$$

La FDA nos ayuda a determinar la probabilidad acumulada de que la variable aleatoria tome un valor igual o menor al valor dado. Por ejemplo, la probabilidad de que el número de fallos sea menor o igual a 1 es $F(1) = 0.8$, es decir, hay un 80% de probabilidad de que haya uno o ningún fallo en el proceso de fabricación.