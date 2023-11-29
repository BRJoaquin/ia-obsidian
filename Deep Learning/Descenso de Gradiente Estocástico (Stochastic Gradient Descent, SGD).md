El **Descenso de Gradiente Estocástico (SGD)** es una variante del algoritmo de [[Descenso de Gradiente]] que se utiliza comúnmente en el aprendizaje automático y las redes neuronales para optimizar una función objetivo que tiene la forma de una suma de otras funciones.

![[Pasted image 20230704131123.png]]

# ¿Cómo funciona?

El algoritmo SGD funciona de la siguiente manera:

1. Inicializa los parámetros del modelo aleatoriamente.
2. Para cada punto de datos en el conjunto de entrenamiento:
   1. Calcula el [[Grandiente]] de la función de error con respecto a los parámetros del modelo utilizando sólo ese punto de datos.
   2. Actualiza los parámetros (pesos) en la dirección **opuesta** al gradiente. La magnitud de la actualización es proporcional a la tasa de aprendizaje y al valor del gradiente.


# Diferencias entre SGD y Descenso de Gradiente

La diferencia principal entre SGD y el descenso de gradiente estándar es que SGD **utiliza un solo punto de datos en cada actualización de los parámetros**, mientras que el descenso de gradiente estándar utiliza todos los puntos de datos ([[Batch]] o minibatch). Esto hace que SGD sea más ruidoso, pero también más rápido y más capaz de escapar de mínimos locales en problemas no convexos.

# Tasa de Aprendizaje

La tasa de aprendizaje es un [[Hiperparámetro|hiperparamentro]] importante en SGD. Una tasa de aprendizaje demasiado alta puede hacer que el algoritmo oscile alrededor del mínimo y nunca converja, mientras que una tasa de aprendizaje demasiado baja puede hacer que el algoritmo converja demasiado lentamente.


# Ejemplo

```python
# Ejemplo de uso de Stochastic Gradient Descent (SGD) en Python
import tensorflow as tf
from tensorflow.keras.optimizers import SGD

# Definición del modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilación del modelo utilizando SGD como optimizador
optimizer = SGD(learning_rate=0.01)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

```