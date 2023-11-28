La regularización es un conjunto de técnicas que se utilizan para prevenir el [[Sobreajuste (Overfitting)]] en los modelos de [[Machine Learning]]. El sobreajuste ocurre cuando un modelo aprende demasiado bien los datos de entrenamiento y pierde la capacidad de generalizar sobre nuevos datos desconocidos. Esencialmente, la regularización **agrega una penalización a los parámetros del modelo para reducir su complejidad** y hacer que el modelo sea más robusto a las fluctuaciones en los datos de entrenamiento.

![[Pasted image 20231128141403.png]]
vease: [[Error esperado]]

En términos más formales, la regularización **modifica la función de pérdida que se está minimizando al agregar un término adicional que penaliza la complejidad del modelo**. Esto a menudo implica restringir los valores de los parámetros del modelo (como los pesos en una red neuronal). La idea es que al agregar esta penalización, se puede equilibrar el trade-off entre [[Sesgo]] y [[Probablidad/Varianza|Varianza]].

Existen varios métodos de regularización, pero los más comunes son la regularización L1 y L2.

## Regularización L1 (Lasso)

En la regularización L1, la penalización es la suma de los valores absolutos de los parámetros del modelo. 

$$ L1 = \lambda \sum_{i=1}^{n} |w_i| $$

donde $w_i$ son los parámetros del modelo y $\lambda$ es el parámetro de regularización que controla la cantidad de regularización que se desea aplicar. Esta forma de regularización tiene la propiedad de generar soluciones dispersas, lo que significa que puede hacer que algunos de los parámetros del modelo sean exactamente cero. Esto puede ser útil si se cree que solo un subconjunto de las características es relevante para la tarea, ya que la regularización L1 puede ayudar a realizar una selección automática de características.

> Basicamente de "yapa" tenemos seleccion de caracteristicas.

## Regularización L2 (Ridge)

En la regularización L2, la penalización es la suma de los cuadrados de los parámetros del modelo. 

$$ L2 = \lambda \sum_{i=1}^{n} w_i^2 $$

Al igual que con L1, $\lambda$ controla la cantidad de regularización a aplicar. La regularización L2 tiene la propiedad de reducir los valores de los parámetros, pero a diferencia de L1, no los hace exactamente cero. Esto es útil cuando se cree que todas las características son relevantes para la tarea.

Finalmente, es importante destacar que la regularización es una herramienta para manejar la complejidad del modelo y ayudar a prevenir el sobreajuste, pero no es un sustituto de tener buenos datos de entrenamiento. Ninguna cantidad de regularización puede compensar datos de entrenamiento de mala calidad o insuficientes.

# Ejemplo: regresion lineal

Veamos algunos ejemplos para entender mejor cómo funcionan las regularizaciones L1 y L2.

Supongamos que estamos desarrollando un modelo de regresión lineal para predecir el precio de las casas en función de una serie de características como el tamaño de la casa, la cantidad de habitaciones, la edad de la casa, la ubicación, etc. Sin embargo, encontramos que nuestro modelo está sobreajustando los datos de entrenamiento. Para evitar este [[Sobreajuste (Overfitting)]], podemos agregar una regularización.

![[Pasted image 20230708173246.png]]

## Regularización L1 (Lasso)

La regularización L1, también conocida como Lasso (Least Absolute Shrinkage and Selection Operator), agrega una penalidad al costo del modelo igual al valor absoluto de la magnitud de los coeficientes. Matemáticamente, la regularización L1 se puede expresar de la siguiente manera:

$$\Large \text{Costo} = \text{MSE} + \alpha\sum_{i=1}^n |\beta_i| $$

donde $\alpha$ es un hiperparámetro que controla la fuerza de la regularización y $\beta_i$ son los coeficientes del modelo. Un valor más grande de $\alpha$ aumenta la regularización y simplifica el modelo.

La regularización L1 puede resultar en modelos con características dispersas, donde algunos coeficientes se hacen cero, es decir, algunos de los atributos son completamente ignorados por el modelo. Esto puede ser beneficioso en casos donde tenemos muchas características y queremos seleccionar solo las más importantes.

![[Pasted image 20230708173316.png]]

## Regularización L2 (Ridge)

La regularización L2, también conocida como Ridge, añade una penalidad al costo del modelo igual al cuadrado de la magnitud de los coeficientes. Matemáticamente, la regularización L2 se puede expresar de la siguiente manera:

$$\Large \text{Costo} = \text{MSE} + \alpha\sum_{i=1}^n \beta_i^2 $$

Al igual que con L1, $\alpha$ es un hiperparámetro que controla la fuerza de la regularización y $\beta_i$ son los coeficientes del modelo. A diferencia de L1, la regularización L2 no hace que los coeficientes se reduzcan a cero. En cambio, distribuye la magnitud de los coeficientes de manera más uniforme a través de las características. Por lo tanto, Ridge puede ser una mejor opción cuando todas las características son importantes.

![[Pasted image 20230708173325.png]]

]]