# Concepto

La capa densa, o completamente conectada, es una de las estructuras fundamentales en las redes neuronales. En la literatura y en la práctica del aprendizaje profundo, estas capas se utilizan para procesar las entradas aplicando una transformación lineal seguida de una no lineal.

El [[Perceptron]] es un caso particular de capa densa. 

![[Pasted image 20231128100312.png]]

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

vease [[Deep Learning/Función de Activación|Función de Activación]]

Algunas de las funciones de activación más comunes son:

- Signo
- Sigmoidea
- Tangente Hiperbólica
- Rectified Linear Unit (ReLU)

![[Pasted image 20231128100404.png]]

vease tambien [[keras.layers.Dense]]