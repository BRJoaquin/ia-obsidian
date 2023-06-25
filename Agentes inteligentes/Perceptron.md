El **Perceptrón Simple** es uno de los algoritmos más simples de [[Machine Learning]], y es la base de las [[Redes Neuronales Artificiales]] y del [[Deep Learning]].

Un Perceptrón Simple toma un conjunto de entradas numéricas y las pondera de acuerdo a un conjunto de pesos, sumándolas luego para obtener una puntuación. Esta puntuación luego pasa a través de una [[Función de Activación]] para producir la salida.

En forma de ecuación, el Perceptrón Simple se ve así:

$$\Large
y = f(\mathbf{w} \cdot \mathbf{x} + b)
$$

donde:
- $\mathbf{w}$ es el vector de pesos.
- $\mathbf{x}$ es el vector de entradas.
- $b$ es el sesgo.
- $f$ es la función de activación.
- $\cdot$ denota el producto escalar.

En el caso del Perceptrón Simple, la función de activación es una función de umbral que produce 1 si la puntuación es positiva y 0 en caso contrario.

Los pesos y el sesgo del Perceptrón se ajustan durante el entrenamiento para minimizar la discrepancia entre las predicciones del Perceptrón y las etiquetas verdaderas. Esto se hace a través de un proceso iterativo en el que se ajustan los pesos en proporción al error cometido en las predicciones.

Aunque el Perceptrón Simple es un modelo simple y no puede resolver problemas que no sean linealmente separables, fue la base para el desarrollo de las redes neuronales multicapa y los algoritmos de aprendizaje profundo, que son capaces de aprender representaciones más complejas y resolver problemas no lineales.
