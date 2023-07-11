La Negative Log-Likelihood (NLL) es una métrica usada frecuentemente en estadística y aprendizaje automático para evaluar la bondad de ajuste de un modelo a los datos. En el contexto de la [[Regresión lineal]], a menudo se utiliza como una función de pérdida para ajustar los parámetros del modelo.

La verosimilitud ([[Máxima Verosimilitud (MLE)]]) de un modelo dado es una medida de qué tan probable es que los datos observados se generen dada la distribución de probabilidad especificada por el modelo. Cuando trabajamos con verosimilitudes, a menudo es más conveniente trabajar con el logaritmo de la verosimilitud (log-likelihood) en lugar de la verosimilitud misma, principalmente porque los logaritmos convierten los productos en sumas, lo que simplifica el cálculo.

La negative log-likelihood (NLL) simplemente es el negativo del logaritmo de la verosimilitud:

$$\Large NLL = -\log(L)$$

donde $L$ es la verosimilitud del modelo.

En el contexto de la regresión lineal, la función de pérdida más comúnmente utilizada es el [[MSE]], que es equivalente a maximizar la log-verosimilitud bajo el supuesto de que los errores siguen una distribución normal. Sin embargo, en otros contextos, como la clasificación, la NLL se utiliza a menudo como una función de pérdida, como en el caso de la pérdida de [[Entropía Cruzada Categórica]] en la regresión logística.

Minimizar la NLL equivale a maximizar la log-verosimilitud (es decir, estamos buscando los parámetros del modelo que hacen que nuestros datos observados sean los más probables bajo el modelo). En este sentido, el método de máxima verosimilitud y la minimización de NLL están estrechamente relacionados.

![[Pasted image 20230707154411.png]]