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