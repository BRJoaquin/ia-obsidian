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

El aprendizaje se realiza utilizando el método de [[Máxima Verosimilitud]]. En resumen, este método trata de encontrar los parámetros del modelo que maximizan la probabilidad de los datos observados.

### Evaluación

El rendimiento de un modelo de Regresión Logística puede ser evaluado utilizando varias métricas, como la precisión, la curva ROC, el área bajo la curva ROC (AUC-ROC), la matriz de confusión, etc.

### Ventajas

- Puede proporcionar probabilidades para las predicciones.
- Puede manejar relaciones no lineales.
- Es simple y fácil de implementar.

### Desventajas

- No es capaz de manejar relaciones complejas.
- Tiene dificultades con las variables categóricas con múltiples niveles.
- Es sensible a la colinealidad en los datos.
