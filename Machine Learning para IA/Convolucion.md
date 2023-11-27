La convolución es un concepto matemático que tiene aplicaciones en muchas áreas, incluyendo la estadística, la física y la ingeniería eléctrica, pero se ha vuelto especialmente conocida en el campo de la inteligencia artificial y el aprendizaje profundo (deep learning) debido a su uso en las [[Redes Neuronales Convolucionales]] (Convolutional Neural Networks, CNNs).

De manera general, la convolución es una operación matemática que integra dos funciones para producir una tercera función. Se puede interpretar como el grado de superposición entre las dos funciones originales cuando una de ellas se invierte y se desplaza.

En el caso de las CNNs, la convolución se utiliza para procesar imágenes. En este contexto, una de las funciones de la convolución es una imagen de entrada, y la otra función es un filtro o kernel, que es una pequeña matriz de números. El filtro se aplica a la imagen de entrada mediante la operación de convolución para producir una nueva imagen, o "mapa de características", que resalta ciertos aspectos de la imagen original.

Por ejemplo, un filtro de convolución podría estar diseñado para resaltar los bordes en una imagen, lo que sería útil en tareas de reconocimiento de objetos. Otro filtro podría ser diseñado para resaltar las regiones de la imagen que son de un cierto color.

La convolución se ha convertido en una herramienta muy útil en el procesamiento de imágenes y el aprendizaje profundo porque permite a las CNNs aprender automáticamente estos filtros durante el proceso de entrenamiento, en lugar de requerir que los ingenieros diseñen manualmente los filtros para cada tarea específica.

https://medium.com/@bdhuma/6-basic-things-to-know-about-convolution-daef5e1bc411

## Filtros (Kernels)
### Descripción
- **Definición**: Un filtro (o kernel) en una convolución es una matriz pequeña utilizada para aplicar efectos como bordes detectados, desenfoque, y otras características espaciales.
- **Función**: Al deslizarse sobre la imagen de entrada, el filtro realiza una operación de multiplicación y suma elemento a elemento con la parte de la imagen sobre la que se encuentra.

### Importancia
- **Extracción de Características**: Cada filtro puede extraer un tipo específico de característica de la imagen, como bordes verticales, horizontales, o texturas.
- **Aprendizaje Automático**: En el aprendizaje profundo, los filtros son aprendidos durante el entrenamiento para optimizar una tarea específica (por ejemplo, clasificación de imágenes).

## Tamaño de Kernel
### Definición
- **Tamaño**: El tamaño de un kernel (por ejemplo, 3x3, 5x5) define el área de la imagen de entrada que se utiliza para calcular una sola salida en el mapa de características.

### Consideraciones
- **Kernels Pequeños (3x3, por ejemplo)**: Capturan características locales, como bordes finos.
- **Kernels Grandes (5x5, 7x7, por ejemplo)**: Capturan información más global, como texturas o patrones más grandes.

## Strides
### Definición
- **Stride**: El stride es el número de píxeles por los que se desplaza el filtro a través de la imagen.

### Impacto
- **Strides Pequeños (por ejemplo, 1)**: Generan mapas de características más grandes, capturando más información detallada.
- **Strides Grandes (por ejemplo, 2 o más)**: Reducen la dimensión del mapa de características, proporcionando una forma de reducción de dimensionalidad.

## Padding
### Tipos
1. **Valid Padding**: 
   - No se añade padding.
   - Resulta en mapas de características más pequeños que la entrada.
2. **Same Padding**: 
   - Se añade padding para que el tamaño del mapa de características sea igual al de la imagen de entrada.
   - Útil para mantener la resolución espacial.
3. **Numero especifico**: 

### Importancia
- **Control de Dimensiones**: El padding permite controlar cómo cambian las dimensiones de los mapas de características después de cada capa convolucional.
- **Conservación de Información**: El padding de 'same' asegura que la información en los bordes de la imagen no se pierda demasiado rápido a medida que la señal pasa por las capas convolucionales.
