![[Pasted image 20231202100243.png]]
# Arquitectura AlexNet

AlexNet es una red neuronal convolucional más profunda y compleja que [[LeNet]], desarrollada por Alex Krizhevsky, Ilya Sutskever y Geoffrey Hinton. Ganó la competición ImageNet Large Scale Visual Recognition Challenge (ILSVRC) en 2012 por un amplio margen. Su éxito marcó el comienzo de la era moderna del aprendizaje profundo en visión por computadora.

## Características Clave de AlexNet

- **Profundidad**: Consiste en 5 capas convolucionales y 3 capas completamente conectadas.
- **Activación ReLU**: Introdujo la función de activación ReLU para acelerar el entrenamiento, sustituyendo las funciones sigmoide/tanh.
- **Uso de GPU**: Fue una de las primeras arquitecturas en utilizar GPUs para acelerar el entrenamiento.
- **Capas de Normalización Local**: Utilizadas después de algunas capas convolucionales para acelerar el entrenamiento y reducir el sobreajuste.
- **Dropout**: Implementó dropout en las capas completamente conectadas para combatir el sobreajuste.

### Detalles de la Arquitectura

- **Capas Convolucionales**: Cada una seguida por una función de activación ReLU; algunas seguidas por normalización local y max pooling.
- **Capas Completamente Conectadas (FC)**: Dos de ellas tienen 4096 neuronas cada una; la última capa FC conecta a 1000 neuronas, una para cada clase de ImageNet.
- **Overlapping Pooling**: AlexNet introdujo pooling con solapamiento para reducir el tamaño de las representaciones y evitar el sobreajuste.
- **Capa de Salida**: Utiliza la función de activación softmax para clasificar entre las 1000 categorías de ImageNet.

![[Pasted image 20231202100628.png]]

## Entrenamiento y Rendimiento

- **Innovación en Entrenamiento**: Utilizó técnicas como la inicialización de pesos cuidadosa, tasas de aprendizaje variables y momentum.
- **Data Augmentation**: Para ampliar el conjunto de datos y mejorar la generalización, se empleó la ampliación de datos mediante la introducción de transformaciones aleatorias.

## Parámetros y Hiperparámetros

- **Número de Parámetros**: Alrededor de 60 millones, lo que es sustancialmente mayor que LeNet.
- **Hiperparámetros**: Incluyen el tamaño de lote, la tasa de aprendizaje inicial y su programación, y la tasa de dropout.

## Impacto en el Campo

- **Benchmark para ILSVRC**: Estableció un nuevo estándar en la clasificación de imágenes y fue ampliamente adoptado como un benchmark.
- **Inspiración para Nuevas Arquitecturas**: Inspiró el diseño de arquitecturas posteriores como VGG, GoogLeNet y ResNet.
- **Aplicaciones en la Industria**: Ha influido en una amplia gama de aplicaciones de visión por computadora, desde aplicaciones móviles hasta sistemas de seguridad.

## Limitaciones y Avances

- **Computacionalmente Exigente**: Requiere hardware de alto rendimiento para el entrenamiento y la inferencia.
- **Sobreajuste en Conjuntos de Datos Pequeños**: Sin técnicas adecuadas de regularización y ampliación de datos, puede sobreajustar en conjuntos de datos más pequeños.

AlexNet es considerada una obra fundamental en el campo del aprendizaje profundo y la visión por computadora, y sigue siendo relevante tanto para la investigación académica como para aplicaciones prácticas.
