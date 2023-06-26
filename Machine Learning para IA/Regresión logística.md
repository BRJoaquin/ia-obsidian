Es un algoritmo de [[Aprendizaje supervisado]] utilizado para clasificación binaria, aunque puede ser adaptado para la clasificación multiclase. A diferencia de la [[Regresión lineal]], que trata de predecir un valor continuo, la regresión logística trata de predecir la probabilidad de que una observación pertenezca a una clase.

# Formula

La fórmula para la Regresión Logística es:

$$\Large
y = \frac{1}{1 + e^{-(b0 + b1*x)}}
$$

donde:
- $y$ es la probabilidad predicha.
- $b0$ y $b1$ son los parámetros del modelo.
- $x$ es la entrada del modelo.
- $e$ es la base del logaritmo natural.

La función $1/(1+e^{-z})$ es conocida como la función logística o [[Sigmoide]], que toma cualquier número real y lo transforma a un valor entre 0 y 1. Esto es útil para convertir una regresión lineal en una forma que pueda representar una probabilidad.

![[Pasted image 20230625165818.png]]

# Aprendizaje

En la **Regresión Logística**, los pesos (o coeficientes) para las variables predictoras se ajustan durante el proceso de entrenamiento para minimizar la función de pérdida, que a menudo es la pérdida de [[Entropía Cruzada binaria (log loss)]] en este caso.

El objetivo del ajuste de pesos es encontrar los valores que hacen que las predicciones del modelo se alineen lo más cerca posible de las etiquetas verdaderas de los datos de entrenamiento. 

El ajuste de los pesos se realiza generalmente a través de un algoritmo de optimización, como el **descenso de gradiente**. En cada iteración del entrenamiento, el algoritmo de optimización calcula el gradiente de la función de pérdida con respecto a cada peso, y luego actualiza los pesos en la dirección que reduce la pérdida.

Para un peso $w_i$ y una tasa de aprendizaje $\alpha$, la actualización de pesos puede expresarse como:

$$\Large
w_i := w_i - \alpha \frac{\partial L}{\partial w_i}
$$

donde:
- $L$ es la función de pérdida.
- $\frac{\partial L}{\partial w_i}$ es el gradiente de $L$ con respecto a $w_i$.

El tamaño de la actualización depende del gradiente y de la tasa de aprendizaje. Una tasa de aprendizaje más alta resulta en cambios más grandes en los pesos, mientras que una tasa de aprendizaje más baja resulta en cambios más pequeños.

Es importante destacar que el ajuste de los pesos debe hacerse de tal manera que el modelo generalice bien a los nuevos datos, no solo a los datos de entrenamiento. Para evitar el [[Sobreajuste (Overfitting)]], a menudo se utiliza alguna forma de regularización, que añade un término de penalización a la función de pérdida para limitar la magnitud de los pesos.

vease: [[Método de Máxima Verosimilitud]]


# Evaluación

El rendimiento de un modelo de Regresión Logística puede ser evaluado utilizando varias métricas, como la precisión, la [[Curva ROC]], el área bajo la curva ROC ([[AUC-ROC]]), la [[Matriz de confusion]], etc.

# Ventajas

- Puede proporcionar probabilidades para las predicciones.
- Puede manejar relaciones no lineales.
- Es simple y fácil de implementar.

# Desventajas

- No es capaz de manejar relaciones complejas.
- Tiene dificultades con las variables categóricas con múltiples niveles.
- Es sensible a la colinealidad en los datos.
  
# Regresión logística multinomial (Softmax)

La regresión logística también se puede generalizar a problemas de clasificación con más de dos clases. Esto se conoce como regresión logística multinomial, o regresión Softmax. En lugar de modelar la probabilidad de que la observación pertenezca a una clase (como en la regresión logística binaria), la regresión logística multinomial modela la probabilidad de que la observación pertenezca a cada clase. Para un problema de clasificación con $K$ clases. vease
