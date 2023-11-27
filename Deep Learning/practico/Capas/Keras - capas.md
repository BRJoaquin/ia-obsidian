
Keras, una API de alto nivel para redes neuronales, ofrece una variedad de capas para construir modelos de aprendizaje profundo. A continuación se listan las diez capas más utilizadas en Keras, junto con sus características y aplicaciones típicas.

## 1. Dense
- **Descripción**: Capa de red neuronal totalmente conectada.
- **Aplicaciones**: Usualmente usada en las capas finales para tareas de clasificación y regresión.
vease [[keras.layers.Dense]]

## 2. Conv2D
- **Descripción**: Capa de convolución 2D, fundamental en redes neuronales convolucionales (CNNs).
- **Aplicaciones**: Ampliamente utilizada en el procesamiento de imágenes y visión por computadora.
vease [[keras.layers.Conv2D]]

## 3. MaxPooling2D
- **Descripción**: Capa de agrupamiento máximo 2D que reduce la dimensionalidad espacial.
- **Aplicaciones**: Se emplea en CNNs para reducir el sobreajuste y mejorar la eficiencia de cómputo.

## 4. Flatten
- **Descripción**: Transforma los datos multidimensionales en un vector unidimensional.
- **Aplicaciones**: Comúnmente usada antes de una capa Dense para aplanar la entrada.

## 5. Dropout
- **Descripción**: Aplica la regularización de dropout, desactivando aleatoriamente un porcentaje de neuronas.
- **Aplicaciones**: Ayuda a prevenir el sobreajuste en modelos de aprendizaje profundo.

## 6. Activation
- **Descripción**: Aplica una función de activación a la salida de una capa.
- **Aplicaciones**: Se utiliza para introducir no linealidades en el modelo.

## 7. BatchNormalization
- **Descripción**: Normaliza las activaciones de la capa anterior, estabilizando y acelerando el entrenamiento.
- **Aplicaciones**: Común en modelos profundos para mejorar el rendimiento y la estabilidad del entrenamiento.

## 8. Embedding
- **Descripción**: Convierte índices enteros en vectores densos de tamaño fijo.
- **Aplicaciones**: Esencial en el procesamiento de texto para representar palabras o frases.

## 9. Input
- **Descripción**: Capa para definir la forma de entrada de un modelo.
- **Aplicaciones**: Utilizada al inicio de un modelo para especificar el tamaño y tipo de los datos de entrada.
