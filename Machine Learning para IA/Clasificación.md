La clasificación es una tarea de aprendizaje supervisado en la que el objetivo es predecir a qué categoría o clase pertenece una entrada dada. El modelo de clasificación se entrena utilizando datos etiquetados, es decir, un conjunto de ejemplos de entradas junto con las respectivas categorías a las que pertenecen. A través del proceso de entrenamiento, el modelo aprende a reconocer patrones y características en los datos que le permiten asignar clases a entradas nuevas y no vistas.

![[Pasted image 20230416185303.jpg]]

La clasificación puede ser:

1.  **Binaria**: Cuando solo hay dos clases posibles. Un ejemplo común es clasificar correos electrónicos como spam o no spam.

2.  **Multiclase**: Cuando hay más de dos clases posibles. Por ejemplo, clasificar imágenes de dígitos escritos a mano en diez clases (0-9).


Algunos algoritmos de clasificación populares incluyen:

-   [[Regresión logística]]: Es un modelo lineal simple que utiliza una función logística para predecir la probabilidad de que una entrada pertenezca a una clase específica. Es especialmente útil para clasificación binaria.

-   Máquinas de vectores de soporte (SVM): Son algoritmos que buscan encontrar un hiperplano que separe las clases de manera óptima. SVM puede utilizarse tanto para clasificación binaria como multiclase.

-  [[Árbol de decisión]] y [[Random Forest]]: Los árboles de decisión son modelos que dividen los datos en subconjuntos basados en características de entrada, siguiendo una estructura jerárquica. Los bosques aleatorios son conjuntos de árboles de decisión que combinan sus predicciones para obtener un resultado más preciso y robusto.

-   [[Redes Neuronales Artificiales]]: Son modelos de aprendizaje profundo que pueden manejar tareas de clasificación complejas, como la clasificación de imágenes y el reconocimiento de voz.


Para evaluar el rendimiento de un modelo de clasificación, se utilizan métricas de evaluación como [[Precisión]], exhaustividad ([[Recall]]), [[F1-score]] y área bajo la [[Curva ROC]] ([[AUC-ROC]]). Estas métricas ayudan a entender qué tan bien el modelo predice las clases correctas y a comparar diferentes modelos entre sí.

# Componentes 

En un problema de clasificación, tenemos los siguientes componentes:

## Atributos (X)

Los atributos, a veces llamados características, son las entradas del modelo. Estos son los datos que se utilizan para hacer una predicción. Los atributos pueden ser cualquier cosa que se considere relevante para el problema de clasificación en cuestión. Por ejemplo, en un problema de clasificación de correos electrónicos como spam o no spam, los atributos podrían incluir la frecuencia de ciertas palabras en el correo electrónico, la dirección de correo electrónico del remitente, la hora del día en que se envió el correo electrónico, y así sucesivamente.

## Etiquetas (Y)

Las etiquetas son las salidas verdaderas del modelo. En un problema de clasificación, las etiquetas son las clases que el modelo intenta predecir. En el ejemplo del correo electrónico, las etiquetas serían "spam" y "no spam".

## Predicciones (U)

Las predicciones son las salidas del modelo. En un problema de clasificación, las predicciones son las clases que el modelo estima que son las más probables basándose en los atributos. El objetivo es que las predicciones coincidan con las etiquetas lo más a menudo posible.

## Clase de Probabilidad (P)

La clase de probabilidad es un modelo matemático de cómo los atributos y las etiquetas se relacionan entre sí. En el aprendizaje automático, se hace un **supuesto** (a veces explícito, a veces implícito) sobre cómo se genera la etiqueta a partir de los atributos. La clase de probabilidad representa este supuesto.

## Sesgo Inductivo (H)

El sesgo inductivo se refiere a las suposiciones realizadas por el modelo para hacer predicciones a partir de los atributos. Por ejemplo, un árbol de decisión hace la suposición de que la etiqueta se puede predecir tomando decisiones basadas en los valores de los atributos. Un modelo de regresión lineal hace la suposición de que la etiqueta es una combinación lineal de los atributos.

## Función de Pérdida

La función de pérdida cuantifica cuánto "duele" cuando las predicciones del modelo no coinciden con las etiquetas. En un problema de clasificación, una función de pérdida comúnmente utilizada es la pérdida logarítmica (también conocida como cross-entropy, vease [[Entropía Cruzada binaria (log loss o NLL)]]), que es muy sensible a las predicciones que están confiadamente equivocadas.

El **proceso de aprendizaje** implica el uso de un algoritmo para ajustar los parámetros del modelo de manera que minimice la función de pérdida en un conjunto de datos de entrenamiento. En otras palabras, el modelo "aprende" de los ejemplos en el conjunto de entrenamiento ajustando sus parámetros para hacer predicciones que están lo más cerca posible de las etiquetas verdaderas, según la medida de la función de pérdida.

![[Pasted image 20230708101514.png]]


> En algunos escenarios de aprendizaje automático, el espacio de predicciones `U` puede ser diferente del espacio de etiquetas `Y`. Aquí hay un par de ejemplos:
En el caso de la clasificación multiclase, las etiquetas `Y` podrían ser un conjunto de clases múltiples, por ejemplo, `{perro, gato, pájaro}`. En este caso, podrías tener una representación en el espacio de predicciones `U` que es un vector de probabilidades para cada clase. Entonces, `U` sería algo como `(0.2, 0.3, 0.5)`, que representa la probabilidad estimada de que la entrada sea de cada clase. En este caso, `Y` y `U` son diferentes porque `Y` representa la clase real y `U` representa un conjunto de probabilidades.
En un problema de regresión, las etiquetas `Y` son valores numéricos continuos. Sin embargo, en algunos casos, podrías tener un modelo que estima una distribución de probabilidad para `Y` en lugar de un valor específico. En este caso, `U` podría ser una distribución de probabilidad (como una distribución Gaussiana con una media y una varianza), mientras que `Y` son valores numéricos reales.
