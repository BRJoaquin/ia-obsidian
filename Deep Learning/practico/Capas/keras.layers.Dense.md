
La capa `Dense` es una de las más fundamentales y utilizadas en Keras. A continuación, se detalla su funcionamiento, características, y aplicaciones.

Documentacion oficinal: https://keras.io/api/layers/core_layers/dense/
## Funcionamiento Básico

- **Descripción General**: La capa `Dense` representa una capa de red neuronal totalmente conectada. Cada neurona en una capa `Dense` recibe entradas de todas las neuronas de la capa anterior.
- **Operación Matemática**: La operación principal es `output = activation(dot(input, kernel) + bias)`.
  - `input`: Datos de entrada.
  - `kernel`: Matriz de pesos.
  - `bias`: Vector de sesgo.
  - `activation`: Función de activación.

## Parámetros Clave

- **units**: Número de neuronas en la capa.
- **activation**: Función de activación a utilizar (`'relu'`, `'sigmoid'`, `'tanh'`, etc.).
- **use_bias**: Booleano que indica si se debe agregar un vector de sesgo a la salida.
- **kernel_initializer**: Inicializador para la matriz de pesos.
- **bias_initializer**: Inicializador para el vector de sesgo.
- **kernel_regularizer**: Regularizador aplicado a la matriz de pesos.
- **bias_regularizer**: Regularizador aplicado al vector de sesgo.

## Aplicaciones

- **Clasificación y Regresión**: Común en las capas finales de modelos para tareas de clasificación (con funciones de activación como `softmax`) y regresión.
- **Modelado de Características**: Utilizada en capas intermedias para aprender representaciones de alto nivel de los datos de entrada.

## Ejemplo de Uso en Keras

```python
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
# Añadiendo una capa Dense con 64 unidades y función de activación ReLU
model.add(Dense(64, activation='relu', input_shape=(input_dimension,)))
# Añadiendo una capa Dense para clasificación con función de activación Softmax
model.add(Dense(num_classes, activation='softmax'))
```
```