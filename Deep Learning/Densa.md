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

vease [[Machine Learning para IA/Función de Activación|Función de Activación]]

Algunas de las funciones de activación más comunes son:

- Signo
- Sigmoidea
- Tangente Hiperbólica
- Rectified Linear Unit (ReLU)

![[Pasted image 20231128100404.png]]
# Broadcasting en Matrices

**Definición**: Broadcasting es una técnica utilizada en bibliotecas como NumPy o TensorFlow que permite realizar operaciones aritméticas entre arrays de diferentes shapes sin replicar físicamente los datos.

**Funcionamiento**: 
  - En el broadcasting, la biblioteca automáticamente *expande* la matriz más pequeña a lo largo de las dimensiones donde no coinciden.
  - Esto se hace generalmente en la dirección de las filas (axis 0) o de las columnas (axis 1), dependiendo de la operación y la orientación de las matrices.

**Ejemplo**: Si `b` es un vector de shape `(k,)` y `XW` es una matriz de shape `(n, k)`, el broadcasting permite sumar `b` a cada fila de la matriz `XW` sin necesidad de copiar `b` en múltiples filas.

## Shapes

- **Definición**: El *shape* de una matriz o tensor es la dimensión o el tamaño de este. En el contexto de arrays o matrices, se refiere al número de filas y columnas que tiene el array.
  
- **Notación**: Se denota como un par de números entre paréntesis, por ejemplo `(n, m)`, donde `n` es el número de filas y `m` es el número de columnas.

- **Importancia**: Comprender el shape de las matrices es crucial para operaciones matemáticas como la multiplicación de matrices, donde la concordancia de las dimensiones es necesaria.
## Aplicación en la Expresión Lineal

- **Expresión**: `U = XW + b`
  
- **Shapes en la Operación**:
  - `X` tiene un shape `(n, m)`
  - `W` tiene un shape `(m, k)`
  - `b` tiene un shape `(k,)` que, gracias al broadcasting, se trata como si tuviera un shape `(n, k)` para la operación de suma con el resultado de `XW`.
  
![[Pasted image 20231128100544.png]]

- **Concordancia**:
  - La multiplicación `XW` requiere que el número de columnas de `X` sea igual al número de filas de `W`.
  - Para la suma, el broadcasting adapta el shape de `b` para que concuerde con el resultado de `XW`.

## Código en Python para Broadcasting

```python
import numpy as np

# Ejemplo de broadcasting en Python con NumPy
X = np.random.rand(n, m)  # n x m matrix
W = np.random.rand(m, k)  # m x k matrix
b = np.random.rand(k)     # Vector de longitud k

# Multiplicación de matrices
XW = np.dot(X, W)  # Resultado es una matriz de n x k

# Broadcasting en la operación de suma
U = XW + b  # NumPy broadcastea b a lo largo del eje 1 automáticamente
```




vease tambien [[keras.layers.Dense]]