
[Keras](https://keras.io/)es una biblioteca de aprendizaje profundo ([[Deep Learning]]) de código abierto que se utiliza en el campo de la [[Inteligencia Artificial]]. Ofrece una forma sencilla y flexible para construir y experimentar con [[Modelo (Hipotesis) |modelos]] de [[Redes Neuronales Artificiales]].

## Características Principales

- **Interfaz Amigable:** Keras es conocido por su facilidad de uso, haciendo que la creación de modelos de aprendizaje profundo sea **más accesible**.
- **Modularidad:** Permite construir modelos [[Capa (DL)|capa]] por capa, ofreciendo una gran flexibilidad en el diseño de arquitecturas de redes neuronales.
- **Extensibilidad:** Soporta la creación de nuevas capas, [[Función de pérdida|funciones de perdida]] y otros elementos para adaptarse a necesidades específicas.

## Compatibilidad con Backends

- **TensorFlow:** Originalmente, Keras funcionaba como una interfaz de alto nivel para múltiples backends, pero actualmente es parte integral de [[Tensorflow]].

## Aplicaciones Comunes

- **Visión por Computadora:** Utilizado en tareas como reconocimiento de imágenes y vídeo. vease [[Visión por Computadora]]
- **Procesamiento del Lenguaje Natural (PLN):** Ayuda en la creación de modelos para comprensión y generación de texto. vease [[Procesamiento del Lenguaje Natural (PLN)]]
- **Predicción y Análisis de Datos:** Aplicado en áreas como la predicción del tiempo, análisis de sentimientos, entre otros. vease [[Regresión]] y [[Clasificación]]

## Ventajas de Keras

- **Facilidad de Uso:** Ideal para principiantes por **su simplicidad y documentación clara**.
- **Rápido Prototipado:** Permite crear prototipos de modelos de forma rápida y eficiente.
- **Comunidad Amplia:** Cuenta con una gran comunidad de usuarios y desarrolladores, facilitando el acceso a soporte y recursos.

## Desventajas de Keras

- **Rendimiento Optimizado:** En algunos casos, puede ser menos eficiente en términos de velocidad y rendimiento en comparación con otras bibliotecas de mas bajo nivel como [[PyTorch]]

# Ejemplo Básico en Keras: Red Neuronal para Clasificación

A continuación, se presenta un ejemplo sencillo de cómo utilizar Keras para construir y entrenar una red neuronal básica para clasificación. Este ejemplo asume que se trabaja con un conjunto de datos de clasificación binaria.

## Paso 1: Importar las Bibliotecas Necesarias

```python
import keras
from keras.models import Sequential
from keras.layers import Dense
```

- **keras:** El módulo principal de Keras.
- **Sequential:** Un modelo lineal de capas.
- **Dense:** Una capa densa (o completamente conectada).
## Paso 2: Crear el Modelo

```python
model = Sequential()
```

- **Sequential:** Inicializa un modelo lineal vacío.
## Paso 3: Añadir Capas al Modelo

```python
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

- **Dense(12, input_dim=8, activation='relu'):** Añade una capa densa con 12 neuronas, dimensiones de entrada de 8 y activación ReLU.
- **Dense(1, activation='sigmoid'):** Añade una capa de salida con una neurona (para clasificación binaria) y activación sigmoide.

vease https://keras.io/api/layers/core_layers/dense/

## Paso 4: Compilar el Modelo

```python
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

- **loss='binary_crossentropy':** Define la función de pérdida para clasificación binaria.
- **optimizer='adam':** Especifica el optimizador (Adam en este caso).
- **metrics=['accuracy']:** Determina la métrica de evaluación (exactitud).

## Paso 5: Entrenamiento del Modelo

```python
model.fit(X_train, y_train, epochs=100, batch_size=10)
```

- **X_train, y_train:** Datos de entrenamiento.
- **epochs=100:** Número de iteraciones sobre el conjunto de datos completo.
- **batch_size=10:** Número de muestras por actualización del gradiente.

## Paso 6: Evaluación del Modelo

```python
accuracy = model.evaluate(X_test, y_test)
```

- **X_test, y_test:** Datos de prueba para evaluar el modelo.
- **accuracy:** Devuelve la precisión del modelo en los datos de prueba.

