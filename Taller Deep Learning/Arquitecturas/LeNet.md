
![[Pasted image 20231202095817.png]]

# Arquitectura LeNet

LeNet es una de las primeras redes neuronales convolucionales (CNN) propuestas por Yann LeCun en 1998. Fue diseñada para la clasificación de dígitos manuscritos, como los del dataset MNIST. Esta red fue un gran avance en el campo de la visión por computadora y el aprendizaje profundo.

## Componentes de LeNet

### Estructura General
- **Capas Convolucionales y de Pooling**: Alternancia de capas convolucionales y de pooling (submuestreo).
- **Capas Completamente Conectadas (FC)**: Una serie de capas FC siguen a las capas convolucionales/pooling.
- **Función de Activación Softmax**: Utilizada en la capa de salida para la clasificación multiclase.

## Parámetros y Entrenamiento

- **Número de Parámetros**: Aproximadamente 60k, relativamente pequeña en comparación con las redes modernas.
- **Entrenamiento**: Utiliza retropropagación y gradiente descendente para ajustar los pesos.
  
## Innovaciones y Contribuciones

- **Localización de Características**: A través de las capas convolucionales, LeNet puede localizar características en una imagen independientemente de su posición.
- **Reducción de Dimensionalidad**: Las capas de pooling reducen la cantidad de parámetros y la complejidad computacional.
- **Invariancia a la Distorsión y Escala**: Parcialmente lograda gracias a las capas convolucionales y de pooling.

## Impacto

- **Clasificación de MNIST**: Superó el estado del arte en la clasificación del dataset MNIST.
- **Aplicaciones en la Industria**: Influyó en el diseño de sistemas para el reconocimiento de caracteres en la vida real, como la lectura automática de códigos postales y dígitos en documentos bancarios.

## Limitaciones y Evolución

- **Sensibilidad a la Rotación y Escala**: Aunque LeNet maneja bien las variaciones pequeñas, las grandes transformaciones pueden requerir una red más sofisticada.
- **Necesidad de Preprocesamiento**: Las imágenes de entrada deben ser preprocesadas a un tamaño fijo (32x32).
- **Superada por Arquitecturas más Avanzadas**: Con el advenimiento de nuevas técnicas y potencia computacional, arquitecturas como AlexNet, VGG, y ResNet han superado a LeNet en rendimiento.

LeNet es un punto de referencia histórico importante en el desarrollo de las CNNs y continúa siendo estudiada por su simplicidad y eficacia en tareas de reconocimiento de imágenes básicas.
