![[Pasted image 20231202100719.png]]

# Arquitectura VGGNet

VGGNet es una arquitectura de red neuronal convolucional desarrollada por el Visual Graphics Group (VGG) de la Universidad de Oxford y presentada en el ILSVRC 2014. Se destacó por su simplicidad y profundidad, utilizando exclusivamente capas convolucionales de pequeño tamaño de campo receptivo (3x3) y capas de max pooling.

## Componentes Clave de VGGNet

### Profundidad Uniforme
- **Capas Convolucionales**: Utiliza repetidamente capas convolucionales con filtros de 3x3 y un stride de 1, seguidas de una función de activación ReLU.
- **Capas de Max Pooling**: Después de varias capas convolucionales, se emplean capas de max pooling con un tamaño de 2x2 y un stride de 2 para reducir las dimensiones.

### Variaciones de la Arquitectura
- **VGG-16 y VGG-19**: Son las variantes más conocidas, con 16 y 19 capas respectivamente.
  
### Capas Completamente Conectadas
- **Capas FC**: Tres capas FC al final, donde las dos primeras tienen 4096 unidades y la última tiene 1000 unidades (para la clasificación de ImageNet).

### Normalización de Respuesta Local (LRN)
- **Removida en VGG**: A diferencia de AlexNet, VGGNet no utiliza LRN ya que no observaron mejoras significativas con su inclusión.

## Entrenamiento y Rendimiento

- **Inicialización de Pesos**: Entrenaron capas más profundas utilizando los pesos de una red menos profunda ya entrenada.
- **Optimización**: Utilizaron técnicas de optimización como el momentum y decay de la tasa de aprendizaje.
- **Data Augmentation**: Emplearon la ampliación de datos a través de recortes aleatorios y volteos horizontales.

## Impacto

- **Eficiencia en la Detección de Características**: La arquitectura permitió detectar características a múltiples escalas y lograr una mejor generalización.
- **Benchmark en Visión por Computadora**: Se convirtió en un estándar de referencia para la evaluación de modelos debido a su estructura simple y rendimiento.

## Limitaciones

- **Demanda de Recursos**: Los modelos VGG son muy grandes y requieren una cantidad significativa de recursos computacionales.
- **Tiempo de Entrenamiento**: Debido a su profundidad y número de parámetros, el entrenamiento puede ser muy lento.
- **Inferencia**: El tiempo de inferencia es también considerable debido al número de operaciones involucradas.
## Legado

VGGNet ha dejado un legado duradero en el campo del aprendizaje profundo, y sus pre-entrenados modelos aún se utilizan como extractores de características en muchas aplicaciones de visión por computadora.
