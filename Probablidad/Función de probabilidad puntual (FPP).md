La función de probabilidad puntual (FPP) es una función asociada a una variable aleatoria discreta que describe la probabilidad de que la variable tome un valor específico. La FPP asigna una probabilidad a cada uno de los posibles valores que puede tomar la variable aleatoria discreta.

Dada una variable aleatoria discreta $X$ con posibles valores $x_1, x_2, x_3, ...$, la función de probabilidad puntual se denota como $P(X = x_i)$ y cumple con las siguientes propiedades:

1.  La probabilidad de cada valor es un número no negativo: $P(X = x_i) \geq 0$ para todo $i$.
2.  La suma de las probabilidades de todos los posibles valores de la variable aleatoria es igual a 1: $\sum_i P(X = x_i) = 1$.

Un ejemplo clásico de función de probabilidad puntual es el lanzamiento de un dado justo. Si denotamos por $X$ la variable aleatoria que representa el número que aparece en la cara superior del dado después de un lanzamiento, entonces la FPP se define como:

P(X=1) = 1/6
P(X=2) = 1/6
P(X=3) = 1/6
P(X=4) = 1/6
P(X=5) = 1/6
P(X=6) = 1/6

En este caso, la FPP asigna una probabilidad de 1/6 a cada uno de los posibles valores de la variable aleatoria $X$. La función de probabilidad puntual es útil para describir la distribución de probabilidad de una variable aleatoria discreta y permite calcular la probabilidad de eventos y realizar análisis estadísticos en base a los valores y sus probabilidades asociadas.

# Ejercicio 

![[Pasted image 20230423124641.png]]

Para encontrar la función de probabilidad puntual (FPP) de la variable aleatoria $X$ en este caso, necesitamos calcular la probabilidad de que se requieran $x$ extracciones para sacar una bola roja. Recordemos que hay 2 bolas rojas y 3 bolas blancas en la urna, y las extracciones se realizan sin reposición.

1.  **$X = 1$: Una extracción** La probabilidad de sacar una bola roja en la primera extracción es simplemente la proporción de bolas rojas en la urna:

$$P(X=1) = \frac{2 \text{ bolas rojas}}{2 \text{ bolas rojas} + 3 \text{ bolas blancas}} = \frac{2}{5}$$

2.  **$X = 2$: Dos extracciones** Para que se requieran dos extracciones para sacar una bola roja, la primera extracción debe ser una bola blanca y la segunda una roja:

$$P(X=2) = \frac{3 \text{ bolas blancas}}{2 \text{ bolas rojas} + 3 \text{ bolas blancas}} \times \frac{2 \text{ bolas rojas}}{1 \text{ bola roja} + 3 \text{ bolas blancas}} = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$$

3.  **$X = 3$: Tres extracciones** Para que se requieran tres extracciones para sacar una bola roja, las dos primeras extracciones deben ser bolas blancas y la tercera una roja:

$$P(X=3) = \frac{3 \text{ bolas blancas}}{2 \text{ bolas rojas} + 3 \text{ bolas blancas}} \times \frac{2 \text{ bolas blancas}}{1 \text{ bola roja} + 3 \text{ bolas blancas}} \times \frac{2 \text{ bolas rojas}}{2 \text{ bolas rojas} + 1 \text{ bola blanca}} = \frac{3}{5} \times \frac{2}{4} \times \frac{2}{3} = \frac{1}{5}$$

4.  **$X = 4$: Cuatro extracciones** Para que se requieran cuatro extracciones para sacar una bola roja, las tres primeras extracciones deben ser bolas blancas y la cuarta una roja:

$$P(X=4) = \frac{3 \text{ bolas blancas}}{2 \text{ bolas rojas} + 3 \text{ bolas blancas}} \times \frac{2 \text{ bolas blancas}}{1 \text{ bola roja} + 3 \text{ bolas blancas}} \times \frac{1 \text{ bola blanca}}{2 \text{ bolas rojas} + 1 \text{ bola blanca}} \times \frac{2 \text{ bolas rojas}}{2 \text{ bolas rojas}} = \frac{3}{5} \times \frac{2}{4} \times \frac{1}{3} \times 1 = \frac{1}{10}
$$

Entonces, la función de probabilidad puntual (FPP) de la variable aleatoria $X$ es:

$$P(X=1) = \frac{2}{5}$$
$$P(X=2) = \frac{3}{10} $$
$$P(X=3) = \frac{1}{5}$$
$$P(X=4) = \frac{1}{10}$$


La FDA de la variable aleatoria $X$ es:

$$\Large
F_X(x) = \left\{
\begin{array}{cl}
  \frac{2}{5} & \text{si } x = 1 \\
  \frac{7}{10} & \text{si } x = 2 \\
  \frac{9}{10} & \text{si } x = 3 \\
  1 & \text{si } x = 4
\end{array}
\right.

$$