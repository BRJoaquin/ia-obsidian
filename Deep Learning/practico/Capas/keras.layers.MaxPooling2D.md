# Descripción General

`keras.layers.MaxPooling2D` es una capa en [[Keras]] utilizada en [[Redes Neuronales Convolucionales|redes neuronales convolucionales (CNNs)]] para realizar operaciones de [[Pooling|pooling]] máxima en datos espaciales.

Documentacion oficial: https://keras.io/api/layers/pooling_layers/max_pooling2d/ 
# Propósito y Función
## Reducción de Dimensionalidad

- **Reducción Espacial**: Disminuye el tamaño de las representaciones para reducir la cantidad de parámetros y cálculos en la red.
- **Prevención del Sobreajuste**: Ayuda a evitar el sobreajuste al proporcionar una forma de abstracción de características.

## Extracción de Características

- **Resaltado de Características Dominantes**: Maximiza las características más destacadas (el valor máximo en una ventana específica).

# Parámetros Clave

- `pool_size`: El tamaño de la ventana de pooling (por ejemplo, (2, 2)).
- `strides`: Controla el desplazamiento de la ventana de pooling. Si es `None`, se tomará igual al `pool_size`.
- `padding`: Puede ser 'valid' (sin padding) o 'same' (con padding si es necesario).

# Ejemplo en Python
```python
from keras.layers import MaxPooling2D

# Crear una capa de MaxPooling2D
max_pool_layer = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid')
```

## Cálculo de Dimensiones de Salida

La dimensión de salida se puede calcular de manera similar a las capas convolucionales, utilizando la fórmula: 
$$ O = \frac{I - P + 2 \times padding}{S} + 1 $$
donde `I` es la dimensión de entrada, `P` es el `pool_size`, `padding` es el valor de padding y `S` son los `strides`.
# Cálculo de Parámetros de la red

Al ser una operación matemática fija no tiene parámetros en la red. 

# Conclusión

`keras.layers.MaxPooling2D` es una herramienta esencial en las CNNs, utilizada para reducir las dimensiones espaciales, resaltar características importantes y ayudar en la eficiencia computacional y en la prevención del sobreajuste.
