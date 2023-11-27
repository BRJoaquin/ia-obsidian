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


# Cálculo de Dimensiones

## Fórmula General
Para calcular la dimensión de salida (O) en una capa convolucional, utilizamos la fórmula:
$$ O = \frac{I - K + 2P}{S} + 1 $$
donde:
- `I` es la dimensión de entrada.
- `K` es el tamaño del kernel.
- `P` es el valor numérico del padding.
- `S` es el stride.

## Parámetros Detallados
1. **Tamaño del Kernel (K)**:
   - Tamaño de la matriz de filtro, por ejemplo, 3x3, 5x5.
   - Determina el área de la imagen de entrada que se utiliza para calcular un solo punto en el mapa de características.

2. **Stride (S)**:
   - Cantidad de píxeles que el filtro se mueve en cada paso, comúnmente 1 o 2.

3. **Padding (P)**:
   - Añade bordes de ceros alrededor de la imagen de entrada.
   - A diferencia de "same" o "valid", aquí `P` es un valor numérico específico.

## Ejemplos de Cálculo

### Ejemplo 1: Padding Específico
- **Entrada (I)**: 32x32
- **Kernel (K)**: 3x3
- **Stride (S)**: 1
- **Padding (P)**: 1 (un pixel de padding en cada lado)
- **Cálculo**:
  $$ O = \frac{32 - 3 + 2 \times 1}{1} + 1 = 32 $$
  - Resultado: 32x32

### Ejemplo 2: Sin Padding (P=0)
- **Entrada (I)**: 32x32
- **Kernel (K)**: 5x5
- **Stride (S)**: 2
- **Padding (P)**: 0
- **Cálculo**:
 $$O = \frac{32 - 5 + 2 \times 0}{2} + 1 = 14 $$
  - Resultado: 14x14

## Conclusión
El cálculo de dimensiones de salida con un valor específico de padding permite un mayor control sobre las dimensiones de los mapas de características resultantes en una red neuronal convolucional. Esto es crucial para el diseño y la comprensión detallada de las arquitecturas de CNN.
