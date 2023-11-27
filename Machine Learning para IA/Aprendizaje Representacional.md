















# Representación composicional

# Representación Composicional en Deep Learning

## Definición
La representación composicional en Deep Learning se refiere a la capacidad de un modelo, como una red neuronal, para aprender y representar datos a través de múltiples capas de abstracción. Cada capa construye una representación más compleja basada en la salida de la capa anterior.

## Ejemplo en la Imagen
La imagen muestra un ejemplo de cómo una red neuronal profunda procesa una imagen para identificar objetos:

### Capas Visibles
- **Layer Visible (input pixels)**: La capa más baja que recibe píxeles de imagen como entrada.

### Capas Ocultas
- **1st Hidden Layer (edges)**: La primera capa oculta que puede detectar bordes a partir de los píxeles de entrada.
- **2nd Hidden Layer (corners and contours)**: La segunda capa que identifica esquinas y contornos, construyendo sobre las detecciones de bordes.
- **3rd Hidden Layer (object parts)**: La tercera capa que reconoce partes de objetos utilizando la información de esquinas y contornos.

### Capa de Salida
- **Output (object identity)**: La capa de salida que identifica el objeto completo, en este caso, una persona.

## Importancia
La representación composicional es crucial para el aprendizaje profundo ya que permite que las redes:
- Manejen la complejidad de los datos de entrada.
- Aprendan características jerárquicas de los datos.
- Generalicen mejor a nuevos ejemplos no vistos durante el entrenamiento.

## Aplicaciones
- **Visión por computadora**: como el reconocimiento de objetos en imágenes.
- **Procesamiento de lenguaje natural**: para entender la estructura y el significado del texto.
- **Robótica**: para que los robots reconozcan y manipulen objetos.

## Conclusión
La representación composicional es un concepto clave en el Deep Learning, permitiendo a las máquinas aprender de manera similar a como los humanos construimos entendimiento a partir de conceptos simples a más complejos.


![[Pasted image 20231127092722.png]]