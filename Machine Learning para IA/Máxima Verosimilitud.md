
El método de **Máxima Verosimilitud** es un enfoque de estimación de parámetros en estadísticas y aprendizaje automático. El objetivo es encontrar los parámetros del modelo que maximizan la verosimilitud de los datos observados.

La verosimilitud es la probabilidad de los datos observados dado un conjunto específico de parámetros del modelo. En términos matemáticos, si tenemos un conjunto de datos $D = \{x_1, x_2, ..., x_n\}$ y un modelo paramétrico con parámetros $\theta$, la verosimilitud se define como $L(\theta|D) = P(D|\theta)$.

El principio de la máxima verosimilitud establece que debemos elegir los parámetros $\theta$ que maximizan $L(\theta|D)$.

En la práctica, a menudo es más fácil trabajar con la log-verosimilitud, que es simplemente el logaritmo de la verosimilitud. La maximización de la log-verosimilitud es equivalente a la maximización de la verosimilitud porque el logaritmo es una función monótona creciente.

En el contexto del aprendizaje automático, la maximización de la verosimilitud puede interpretarse como un proceso de aprendizaje que ajusta los parámetros del modelo para hacer que los datos observados sean lo más probables posible bajo el modelo. Por ejemplo, en la [[Regresión logística]], utilizamos la maximización de la verosimilitud para encontrar los coeficientes que hacen que las clasificaciones observadas sean lo más probables posible.
