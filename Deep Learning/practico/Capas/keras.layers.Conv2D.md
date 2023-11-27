## Descripción General
`keras.layers.Conv2D` es una de las capas más fundamentales en redes [[Redes Neuronales Convolucionales|neuronales convolucionales (CNNs)]] en [[Keras]], una biblioteca de Deep Learning en Python. Es utilizada para aplicar una convolución 2D sobre imágenes. vease [[Convolucion]]

Documentacion: https://keras.io/api/layers/convolution_layers/convolution2d/
## Parámetros Clave

- `filters`: Número de [[Convolucion#Filtros (Kernels)|filtros]] (kernels) en la convolución.
- `kernel_size`: [[Convolucion#Tamaño de Kernel|Tamaño del filtro/kernel]] (por ejemplo, (3, 3)).
- `strides`: [[Convolucion#Strides|Tamaño de los pasos]] del filtro durante la convolución.
- `padding`: 'valid' (sin padding) o 'same' (con [[Convolucion#Padding|padding]] para que la salida tenga el mismo tamaño que la entrada).
- `activation`: [[Machine Learning para IA/Función de Activación|Función de activación]], típicamente '[[Función ReLu|relu]]'.
- `input_shape`: Forma del tensor de entrada (solo necesario para la primera capa).

## Cálculo de Parámetros

### Número de Parámetros

El número total de parámetros en una capa Conv2D se calcula con la fórmula:

$$ \text{Número de parámetros} = (\text{kernel size}_\text{height} \times \text{kernel size}_\text{width} \times \text{input channels} + 1) \times \text{filters} $$

### Detalle de Cálculo
- Cada filtro tiene una dimensión de $\text{kernel size}_\text{height} \times \text{kernel size}_\text{width} \times \text{input channels}$.
- El '+1' se debe al término de sesgo (bias) para cada filtro.
- Multiplicamos por el número de filtros para obtener el total de parámetros.

### Ejemplo en Python

```python
from keras.layers import Conv2D

# Crear una capa Conv2D
conv_layer = Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu', input_shape=(28, 28, 1))

# Calcular el número de parámetros
num_params = (3 * 3 * 1 + 1) * 32
# 3 * 3: por el kernel_size=(3, 3)
# * 1: por input_shape=(28, 28, 1)
# + 1: es fijo (es el bias)
# 
print(f"Número de parámetros: {num_params}")
```

## Conclusión
`keras.layers.Conv2D` es esencial para extraer características espaciales en imágenes, siendo un componente crítico en muchas arquitecturas de CNN. Entender cómo se calculan sus parámetros ayuda a diseñar y depurar modelos de manera más efectiva.
