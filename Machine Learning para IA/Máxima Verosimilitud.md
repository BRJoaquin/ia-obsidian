
El principio de **Máxima Verosimilitud** (Maximum Likelihood Estimation, MLE) es un método utilizado en estadística y Machine Learning para estimar los parámetros de una distribución de probabilidad, dado un conjunto de datos. La idea es encontrar los parámetros que hacen que los datos observados sean "más probables".

Dado un modelo de distribución con algunos parámetros desconocidos, y un conjunto de datos observados, el método de máxima verosimilitud busca los valores de los parámetros que maximizan la función de verosimilitud. Esta función de verosimilitud se define como la probabilidad de los datos observados, dado el modelo y sus parámetros.

En términos más formales, si tenemos una distribución de probabilidad $P(x; \theta)$ que depende de los parámetros $\theta$, y un conjunto de datos $D = \{x_1, x_2, ..., x_N\}$, la función de verosimilitud $L(\theta; D)$ se define como:

$$\Large L(\theta; D) = P(D; \theta) = \prod_{i=1}^{N}P(x_i; \theta)$$

La estimación de máxima verosimilitud $\hat{\theta}_{MLE}$ se obtiene maximizando esta función de verosimilitud:

$$\Large \hat{\theta}_{MLE} = \arg\max_{\theta} L(\theta; D)$$

En el aprendizaje de máquinas, el método de máxima verosimilitud se utiliza comúnmente para ajustar modelos, encontrando los parámetros que maximizan la verosimilitud de los datos de entrenamiento dados los parámetros del modelo.
![[Pasted image 20230707123513.png]]