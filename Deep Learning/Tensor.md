## Definición General

Un tensor es una entidad matemática y una generalización de conceptos más familiares como [[Escalar|escalares]], [[Vector|vectores]] y [[Matriz|matrices]]. Es fundamental en campos como el [[Deep Learning|deep learning]] y la física.

### Características Clave

- **Generalización**: 
  - **Escalar**: Un tensor de orden 0 (sin dimensiones).
  - **Vector**: Un tensor de orden 1 (1D).
  - **Matriz**: Un tensor de orden 2 (2D).
  - **Tensor de Alto Orden**: Tensor de orden 3 o superior (3D o más).

- **Componentes**: 
  - Compuesto por elementos dispuestos en una estructura regular.
  - Puede contener números, símbolos o expresiones.

- **Dimensiones e Índices**:
  - Cada elemento en un tensor puede ser identificado usando un conjunto de índices, uno para cada dimensión del tensor.

- **Operaciones**: 
  - Soporta operaciones como suma, multiplicación, y otras transformaciones lineales.

## Aplicaciones en Deep Learning

- **Representación de Datos**: 
  - En deep learning, los tensores son usados para representar datos de entrada, pesos, y activaciones de las redes neuronales.

- **Redes Neuronales Convolucionales (CNN)**:
  - Tensor de orden 4 comúnmente usada para representar imágenes (ancho, alto, canales de color, número de imágenes).

- **Procesamiento de Series Temporales**:
  - Tensor de orden 3 para series temporales (tiempo, características, número de muestras).

- **Operaciones en Redes Neuronales**:
  - Las operaciones de redes neuronales, como la propagación hacia adelante y hacia atrás, implican cálculos con tensores.

## Importancia en Deep Learning

- **Flexibilidad**: Permite manejar datos de diversas formas y dimensiones.
- **Eficiencia Computacional**: Optimizado para operaciones matemáticas rápidas, especialmente en GPUs.
- **Compatibilidad con Herramientas**: Ampliamente soportado por frameworks de deep learning como TensorFlow y PyTorch.
