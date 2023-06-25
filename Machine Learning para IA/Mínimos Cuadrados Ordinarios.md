El método de los Mínimos Cuadrados Ordinarios (Ordinary Least Squares, OLS) es una técnica de optimización que se utiliza para estimar los parámetros desconocidos (coeficientes) en la [[Regresión lineal]]. OLS minimiza la suma de los cuadrados de los residuos, que son las diferencias entre los valores observados y predichos de la variable objetivo.

Asumamos que tenemos un modelo de regresión lineal simple de la forma:

$$\large
y = a + bX + \epsilon
$$
El objetivo de OLS es encontrar los valores de $a$ (intersección) y $b$ (pendiente) que minimizan la suma de los cuadrados de los residuos, denotados como $RSS$:

$$\large
RSS = \sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - a - bX_i)^2
$$
Para encontrar los valores de $a$ y $b$ que minimizan [[RSS]], calculamos las derivadas parciales de $RSS$ con respecto a $a$ y $b$ y las igualamos a cero. Esto nos da un sistema de ecuaciones lineales, que puede resolverse para obtener los estimadores de mínimos cuadrados de $a$ y $b$:

$$\Large
\hat{b} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^{n} (X_i - \bar{X})^2}
$$
$$\Large
\hat{a} = \bar{Y} - \hat{b}\bar{X}
$$

Donde:

- $\bar{X}$ y $\bar{Y}$ son las medias de las variables $X$ e $Y$, respectivamente.
- $\hat{a}$ y $\hat{b}$ son los estimadores OLS de $a$ y $b$.

Es importante mencionar que los estimadores OLS son estimadores insesgados, lo que significa que en promedio, a lo largo de muchas muestras, están en lo correcto. También, bajo ciertas condiciones, son los estimadores de varianza mínima, lo que significa que de todos los estimadores insesgados, los estimadores OLS tienen la menor varianza. Esto los convierte en estimadores muy eficientes.

La técnica OLS se utiliza ampliamente en estadística y machine learning para estimar modelos lineales, debido a su simplicidad y propiedades estadísticas deseables.


![[Pasted image 20230625164919.png]]

