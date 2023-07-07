
El principio de **Máxima Verosimilitud** (Maximum Likelihood Estimation, MLE) es un método utilizado en estadística y Machine Learning para estimar los parámetros de una distribución de probabilidad, dado un conjunto de datos. La idea es encontrar los parámetros que hacen que los datos observados sean "más probables".

Dado un modelo de distribución con algunos parámetros desconocidos, y un conjunto de datos observados, el método de máxima verosimilitud busca los valores de los parámetros que maximizan la función de verosimilitud. Esta función de verosimilitud se define como la probabilidad de los datos observados, dado el modelo y sus parámetros.

En términos más formales, si tenemos una distribución de probabilidad $P(x; \theta)$ que depende de los parámetros $\theta$, y un conjunto de datos $D = \{x_1, x_2, ..., x_N\}$, la función de verosimilitud $L(\theta; D)$ se define como:

$$\Large L(\theta; D) = P(D; \theta) = \prod_{i=1}^{N}P(x_i; \theta)$$

La estimación de máxima verosimilitud $\hat{\theta}_{MLE}$ se obtiene maximizando esta función de verosimilitud:

$$\Large \hat{\theta}_{MLE} = \arg\max_{\theta} L(\theta; D)$$

En el aprendizaje de máquinas, el método de máxima verosimilitud se utiliza comúnmente para ajustar modelos, encontrando los parámetros que maximizan la verosimilitud de los datos de entrenamiento dados los parámetros del modelo.
![[Pasted image 20230707123513.png]]

# Para humanos

El principio de máxima verosimilitud es un concepto importante en estadística y teoría de la probabilidad. Aunque su formulación matemática puede resultar compleja, puedo explicarte el principio de máxima verosimilitud de una manera más accesible para no matemáticos.

Imaginemos que estás tratando de estimar un parámetro desconocido en base a un conjunto de datos observados. El principio de máxima verosimilitud sugiere que debes buscar el valor de ese parámetro que hace que los datos observados sean más probables o más verosímiles.

Para entenderlo mejor, pensemos en un ejemplo sencillo. Supongamos que estás lanzando una moneda y quieres saber cuál es la probabilidad de obtener cara. Lanzas la moneda varias veces y registras los resultados: cara (C) y cruz (X). Tus datos observados podrían ser: C, C, X, C, X.

El principio de máxima verosimilitud te dice que debes encontrar el valor de la probabilidad de cara que maximice la probabilidad de obtener los resultados observados. En este caso, la probabilidad de obtener cara en un lanzamiento de una moneda se puede representar con el parámetro p. Si asumimos que los lanzamientos de la moneda son independientes y que la moneda no está sesgada, entonces la probabilidad de obtener cara en un solo lanzamiento es p.

La probabilidad de obtener los resultados observados (C, C, X, C, X) se puede calcular multiplicando las probabilidades individuales de cada resultado. Por ejemplo, la probabilidad de obtener cara, cruz, cara, cara, cruz con p = 0.5 sería: 0.5 * 0.5 * 0.5 * 0.5 * 0.5.

El principio de máxima verosimilitud te diría que debes encontrar el valor de p que maximiza esta probabilidad. En este caso, la probabilidad sería máxima cuando p = 0.6, lo que significa que la probabilidad de obtener cara en un lanzamiento de la moneda es de aproximadamente 0.6.

Este es un ejemplo simple para ilustrar el principio de máxima verosimilitud. En problemas más complejos, los cálculos pueden ser más difíciles y se necesitan técnicas matemáticas más avanzadas para obtener la estimación del parámetro. Sin embargo, la idea básica sigue siendo la misma: encontrar el valor del parámetro que hace que los datos observados sean más probables.