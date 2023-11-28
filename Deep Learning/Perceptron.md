
El perceptrón es uno de los modelos más sencillos de [[Redes Neuronales Artificiales|redes neuronales artificiales]] y se puede considerar el fundamento de algoritmos más complejos en el campo del aprendizaje automático. Fue desarrollado por Frank Rosenblatt en 1957.

# Definición Matemática

![[Pasted image 20231127161812.png]]

- El perceptrón se define matemáticamente como una función que toma un vector de entrada `x` y produce un valor de salida `1` o `-1`, basado en un conjunto de pesos `w`.
- La función se describe como `P(x; w) = sgn(∑(xi * wi))`, donde `sgn` es la función signo.

## Función Signo

- La función signo, denotada como `sgn(u)`, asigna un valor de `+1` si la entrada `u` es mayor o igual a cero y `-1` si es menor a cero.

# Representación Vectorial

![[Pasted image 20231127161828.png]]
- En forma vectorial, la función del perceptrón se expresa como `P(X; W) = sgn(XW)`.
- Aquí, `X` representa una matriz de entrada y `W` el vector de pesos.

# Conceptos Clave

- **Linearidad**: El perceptrón es un clasificador lineal, lo que significa que solo puede separar dos clases de puntos con una frontera de decisión lineal.
- **Limitaciones**: No puede resolver problemas no linealmente separables, como el problema XOR.
- **Aprendizaje**: El proceso de aprendizaje del perceptrón ajusta los pesos `w` en base a errores cometidos en las predicciones durante el entrenamiento.
- **Regla de Aprendizaje**: Generalmente se usa la regla de aprendizaje del perceptrón, que ajusta los pesos en función del error multiplicado por la tasa de aprendizaje y el valor de entrada.

# Aplicaciones

- A pesar de su simplicidad, el perceptrón puede ser usado para la clasificación binaria en problemas linealmente separables.
- También sirve como bloque de construcción para redes neuronales más complejas y algoritmos de aprendizaje profundo.

# Ejemplo en Python

Aquí un ejemplo simplificado de cómo podría implementarse un perceptrón en Python:

```python
import numpy as np

def sgn(u):
    return 1 if u >= 0 else -1

def perceptron_predict(x, w):
    return sgn(np.dot(x, w))

# Inicialización de pesos
weights = np.random.randn(m)

# Predicción con el perceptrón
prediction = perceptron_predict(input_vector, weights)
```

Este código representa la inicialización de un perceptrón con pesos aleatorios y la realización de una predicción con la función de activación signo.

# Ejemplo de implementacion AND

![[Pasted image 20231127162006.png]]

![[Pasted image 20231127162023.png]]
