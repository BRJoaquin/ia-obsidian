![[Pasted image 20230626100021.png]]

Las **Redes Neuronales Convolucionales (CNN)** son un tipo especial de [[Redes Neuronales Artificiales]] que están diseñadas para procesar datos con una estructura de cuadrícula espacial, **como las imágenes**. Las CNN son eficaces para tareas como el reconocimiento de imágenes y de voz.

### Estructura de las CNN

Una CNN típica consiste en una serie de capas que transforman la imagen de entrada en una salida, como una clasificación. Estas capas pueden ser de varios tipos:

1. **Capas convolucionales**: En estas capas, un conjunto de filtros (también conocidos como "kernels") se pasa a través de la imagen de entrada (o a través de la salida de la capa anterior). Cada filtro produce una "mapa de características" que representa las áreas de la imagen que activaron el filtro. 

2. **Capas de pooling**: Estas capas reducen la dimensionalidad de los datos, lo que ayuda a evitar el sobreajuste y a reducir el coste computacional. Una operación común de pooling es el "max pooling", que toma el valor máximo de una región de la imagen. Vease [[Pooling]]

3. **Capas completamente conectadas**: Al final de la red, una o más capas completamente conectadas se utilizan a menudo para realizar la clasificación final. Estas capas funcionan de la misma manera que en una Red Neuronal Artificial (ANN) normal.

# Funcionamiento de las CNN

Las CNN funcionan propagando la imagen a través de la red, transformándola capa por capa hasta llegar a la salida. En cada capa convolucional, los filtros se aplican a la imagen para crear mapas de características. Estos mapas de características pasan por una función de activación, como ReLU, y luego pueden ser reducidos en tamaño por una capa de pooling.

# Aplicaciones de las CNN

Las CNN son utilizadas en una variedad de aplicaciones, que incluyen:

- **Reconocimiento de imágenes**: Identificar objetos, personas, animales, etc., en imágenes.
- **Detección de objetos**: Localizar la presencia de objetos en la imagen y clasificarlos.
- **Reconocimiento facial**: Identificar o verificar la identidad de una persona a partir de su rostro.
- **Análisis de video**: Extraer información de los frames de un video.
- **Visión por computadora en vehículos autónomos**: Para identificar objetos, peatones, señales de tráfico, etc.

Las CNN han demostrado ser extremadamente eficaces en muchas tareas y son una herramienta esencial en cualquier kit de herramientas de aprendizaje profundo.

# Convolución en CNN

La **Convolución** es una operación matemática fundamental en las Redes Neuronales Convolucionales (CNN). Es un tipo especial de transformación lineal que se aplica a la entrada de la red.

## ¿Cómo funciona?

La convolución en el contexto de las CNN implica el uso de un conjunto de filtros o "kernels", que son matrices pequeñas de números. Cada filtro se aplica a la imagen de entrada (o a la salida de la capa anterior) desplazándose por toda la imagen. 

![[convoluting-a-5x5x1-image-with-a-3x3x1-kernel-to-get-a-3x3x1-convolved-feature.gif]]

Para cada posición, se realiza el producto punto entre el filtro y la porción de la imagen que cubre, sumando los resultados para obtener un solo número. Este número se coloca en la misma posición en un nuevo mapa de características. 

## ¿Qué hacen los filtros?

Cada filtro en una capa convolucional puede aprender a reconocer un tipo específico de característica en la imagen. Por ejemplo, un filtro puede aprender a reconocer bordes verticales, mientras que otro puede aprender a reconocer bordes horizontales. 

A medida que avanzamos en la red, los filtros pueden comenzar a reconocer características más complejas, como formas y patrones específicos. 

# Lectura recomendada
> https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 


# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/V8j1oENVz00" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YRhxdVk_sIs?si=LwylcbBEQOXu01N6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
