# Concepto de Capa Densa

La capa densa, o completamente conectada, es una de las estructuras fundamentales en las redes neuronales. En la literatura y en la práctica del aprendizaje profundo, estas capas se utilizan para procesar las entradas aplicando una transformación lineal seguida de una no lineal.

El [[Perceptron]] es un caso particular de capa densa. 

## Definición Matemática

- Una capa densa se define con la función:
  
  $$D(X; W, b) = \text{act}(XW + b)$$
  
  donde:
  
  - $X$ es la matriz de entrada.
  - $W$ es la matriz de pesos.
  - $b$ es el vector de sesgo (bias).
  - $\text{act}$ es una función de activación.
  - Las dimensiones son $$X \in \mathbb{R}^{(n,m)}, W \in \mathbb{R}^{(m,k)}, b \in \mathbb{R}^{(n,k)}$$

## Función de Activación

La función de activación $\text{act}$ es un componente crucial que introduce no linealidad en el modelo, lo que permite a la red aprender y modelar relaciones complejas entre los datos de entrada y la salida. 

vease [[Machine Learning para IA/Función de Activación|Función de Activación]]

Algunas de las funciones de activación más comunes son:

- Signo
- Sigmoidea
- Tangente Hiperbólica
- Rectified Linear Unit (ReLU)

# Broadcasting en Matrices

El concepto de broadcasting se refiere a la forma en que las operaciones de matrices se llevan a cabo, especialmente cuando se suman vectores a matrices:

- La suma en la operación $XW + b$ utiliza broadcasting para sumar el vector de sesgo $b$ a cada fila del resultado de la multiplicación de matrices $XW$.

## Shapes y Broadcasting

- En la práctica, los shapes de las matrices y vectores deben ser compatibles para realizar operaciones de multiplicación de matrices y broadcasting de suma.
- Para $XW + b$, los shapes deben ser $(n, m)$, $(m, k)$, y $(n, k)$ respectivamente.




vease tambien [[keras.layers.Dense]]