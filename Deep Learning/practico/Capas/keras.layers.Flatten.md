# Descripción General
`keras.layers.Flatten` es una capa en Keras que se utiliza para convertir un tensor multidimensional en un vector unidimensional. Es comúnmente usada en [[Redes Neuronales Convolucionales|redes neuronales convolucionales (CNNs)]] para transicionar entre capas convolucionales y completamente conectadas.

Documentacion oficial: https://keras.io/api/layers/reshaping_layers/flatten/
# Propósito y Función
## Transformación de Datos

- **Conversión de Forma**: Convierte la estructura de datos de un tensor 3D (por ejemplo, de una capa convolucional o de pooling) a un vector 1D.

## Preparación para Capas Densas

- **Compatibilidad de Capas**: Prepara los datos para su procesamiento en capas densas (totalmente conectadas) que requieren un vector de entrada.

# Características Clave

- **Sin Aprendizaje**: No tiene parámetros entrenables, es decir, no aprende durante el entrenamiento.
- **Preservación de Información**: Mantiene toda la información del tensor de entrada, solo cambia su forma.

# Ejemplo en Python
```python
from keras.models import Sequential
from keras.layers import Flatten

# Crear un modelo y añadir una capa Flatten
model = Sequential()
model.add(Flatten(input_shape=(28, 28, 1)))
```

# Uso Común

En las CNNs, después de varias capas de convolución y pooling, se utiliza Flatten para aplanar los mapas de características antes de enviarlos a una o varias capas densas para la clasificación o regresión.

# Consideraciones

- **Aumento de Dimensionalidad**: Puede llevar a un gran número de características, especialmente si se aplanan mapas de características grandes.
- **Eficiencia**: Aunque no tiene parámetros entrenables, el tamaño del tensor aplanado puede afectar la eficiencia computacional y la memoria.

# Cantidad de parámetros en la CNN

Cero, solo cambian la forma de los datos, no tienen parámetros entrenables.

# Conclusión

La capa `Flatten` es un componente esencial en las arquitecturas de CNN, proporcionando un puente necesario entre las capas convolucionales/pooling y las densas, facilitando así la transición entre el procesamiento espacial y el aprendizaje basado en características aplanadas.
