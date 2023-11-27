
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

# Densa 

## Concepto de Capa Densa

La capa densa, o completamente conectada, es una de las estructuras fundamentales en las redes neuronales. En la literatura y en la práctica del aprendizaje profundo, estas capas se utilizan para procesar las entradas aplicando una transformación lineal seguida de una no lineal.

El perceptron 

### Definición Matemática

- Una capa densa se define con la función:
  
  \( D(X; W, b) = \text{act}(XW + b) \)
  
  donde:
  
  - \( X \) es la matriz de entrada.
  - \( W \) es la matriz de pesos.
  - \( b \) es el vector de sesgo (bias).
  - \( \text{act} \) es una función de activación.
  - Las dimensiones son \( X \in \mathbb{R}^{(n,m)}, W \in \mathbb{R}^{(m,k)}, b \in \mathbb{R}^{(n,k)} \).

### Función de Activación

La función de activación \( \text{act} \) es un componente crucial que introduce no linealidad en el modelo, lo que permite a la red aprender y modelar relaciones complejas entre los datos de entrada y la salida. Algunas de las funciones de activación más comunes son:

- Signo
- Sigmoidea
- Tangente Hiperbólica
- Rectified Linear Unit (ReLU)

## Broadcasting en Matrices

El concepto de broadcasting se refiere a la forma en que las operaciones de matrices se llevan a cabo, especialmente cuando se suman vectores a matrices:

- La suma en la operación \( XW + b \) utiliza broadcasting para sumar el vector de sesgo \( b \) a cada fila del resultado de la multiplicación de matrices \( XW \).

### Shapes y Broadcasting

- En la práctica, los shapes de las matrices y vectores deben ser compatibles para realizar operaciones de multiplicación de matrices y broadcasting de suma.
- Para \( XW + b \), los shapes deben ser \( (n, m) \), \( (m, k) \), y \( (n, k) \) respectivamente.

## Notación Gráfica y Dimensiones

El documento proporciona una notación gráfica detallada y explicaciones sobre las dimensiones de las matrices y vectores invol
