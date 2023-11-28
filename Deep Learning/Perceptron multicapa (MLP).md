## Introducción

### Definición
El Perceptrón Multicapa (MLP) es un tipo de [[Redes Neuronales Artificiales|red neuronal artificial]] organizada en múltiples capas. Es un modelo de aprendizaje profundo utilizado ampliamente para tareas de clasificación y regresión.

### Historia y Evolución
- **Orígenes**: Basado en el perceptrón simple, desarrollado por Frank Rosenblatt en los años 50.
- **Evolución**: La introducción del algoritmo de retropropagación en los años 80 permitió el entrenamiento eficiente de MLP.

## Arquitectura

### Componentes Básicos
1. **Capas**: 
   - *Capa de Entrada*: Recibe los datos de entrada.
   - *Capas Ocultas*: Capas intermedias donde ocurre el procesamiento computacional.
   - *Capa de Salida*: Proporciona el resultado final del modelo.

2. **Neuronas**:
   - Unidades de procesamiento que suman ponderadamente las entradas y aplican una función de activación.

3. **Pesos y Sesgos**:
   - Elementos ajustables durante el entrenamiento que determinan la fuerza de las conexiones entre neuronas.

### Funcionamiento
- **Procesamiento de la Información**: Los datos pasan secuencialmente a través de las capas, transformándose en cada etapa.
- **Funciones de Activación**: Como ReLU, sigmoide o tanh, introducen no linealidades en el modelo.

## Algoritmo de Aprendizaje

### Retropropagación
- **Concepto**: Método para ajustar los pesos y sesgos mediante la minimización de un error.
- **Gradiente Descendente**: Algoritmo utilizado para actualizar los pesos en la dirección que reduce el error.

### Entrenamiento
- **Fases**: 
  1. Propagación hacia adelante: Cálculo de la salida.
  2. Cálculo del error: Diferencia entre la salida obtenida y la esperada.
  3. Propagación hacia atrás: Ajuste de pesos y sesgos.

## Aplicaciones

1. **Clasificación**: Identificación de categorías dentro de los datos.
2. **Regresión**: Predicción de valores continuos.
3. **Reconocimiento de Patrones**: En imágenes, sonido, texto, etc.
4. **Series Temporales**: Predicción y análisis de datos secuenciales.

## Ventajas y Desventajas

### Ventajas
- **Flexibilidad**: Capaz de modelar complejas relaciones no lineales.
- **Generalización**: Buen desempeño en una amplia gama de tareas.

### Desventajas
- **Sobreajuste**: Riesgo de memorizar los datos de entrenamiento en lugar de aprender la relación subyacente.
- **Costo Computacional**: Requiere recursos significativos para entrenamiento y ajuste de modelos.

## Herramientas y Librerías Populares

1. **TensorFlow**: Ampliamente utilizada en investigación y desarrollo.
2. **PyTorch**: Preferida por su facilidad de uso y flexibilidad en el diseño de modelos.
3. **Keras**: Interfaz de alto nivel para TensorFlow, centrada en la facilidad de uso.

## Ejemplo en Python

A continuación, se presenta un ejemplo básico de cómo implementar un MLP en Python utilizando Keras.

```python
from keras.models import Sequential
from keras.layers import Dense

# Crear el modelo
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu')) # Capa de entrada y primera capa oculta
model.add(Dense(8, activation='relu')) # Segunda capa oculta
model.add(Dense(1, activation='sigmoid')) # Capa de salida

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Ajustar el modelo
model.fit(X, Y, epochs=150, batch_size=10)
```