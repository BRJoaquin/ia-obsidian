

El **Perceptrón Simple** es uno de los algoritmos más simples de [[Machine Learning]], y es la base de las [[Redes Neuronales Artificiales]] y del [[Deep Learning]].

![[Pasted image 20230626085610.png]]

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

En el caso del Perceptrón Simple, la función de activación es una [[Función Umbral]]que produce 1 si la puntuación es positiva y 0 en caso contrario.

Los pesos y el sesgo del Perceptrón se ajustan durante el entrenamiento para minimizar la discrepancia entre las predicciones del Perceptrón y las etiquetas verdaderas. Esto se hace a través de un proceso iterativo en el que se ajustan los pesos en proporción al error cometido en las predicciones.

Aunque el Perceptrón Simple es un modelo simple y no puede resolver problemas que no sean linealmente separables, fue la base para el desarrollo de las [[Perceptrón Multicapa]] y los algoritmos de [[Deep Learning]], que son capaces de aprender representaciones más complejas y resolver problemas no lineales.

# Actualización de Pesos

Los pesos en un **Perceptrón Multicapa (MLP)** se actualizan durante el proceso de entrenamiento. El objetivo del entrenamiento es minimizar la [[Función de pérdida]], una medida del error entre las predicciones del modelo y los valores reales.

Para actualizar los pesos, se utiliza un algoritmo llamado [[Retropropagación del error]] (backpropagation) en combinación con un método de optimización, comúnmente el [[Decenso de Gradiente]] o alguna de sus variantes (como el Descenso de Gradiente Estocástico o Adam).

El proceso general para la actualización de pesos es el siguiente:

1. **Feedforward**: Las entradas se pasan a través de la red, capa por capa, hasta que se generan las salidas.

2. **Cálculo de la Pérdida**: Se calcula la función de pérdida utilizando las salidas de la red y los valores reales.

3. **Backpropagation**: Se calculan las derivadas parciales de la función de pérdida con respecto a cada uno de los pesos en la red (es decir, el gradiente de la pérdida con respecto a los pesos). Este proceso se realiza retrocediendo a través de la red, comenzando con la capa de salida y yendo hacia las capas de entrada.

4. **Actualización de Pesos**: Los pesos se actualizan restando una fracción del gradiente calculado en el paso 3. La fracción se determina por la tasa de aprendizaje ([[Taza de aprendizaje]]), un parámetro que se establece antes de comenzar el entrenamiento.

# Funciones de Pérdida

La elección de la función de pérdida en un MLP depende del tipo de problema que se esté resolviendo. Aquí algunos ejemplos de funciones de pérdida comunes:

- **Error Cuadrático Medio (MSE)**: Se utiliza comúnmente para problemas de regresión. Esta función de pérdida calcula la media de los cuadrados de las diferencias entre las predicciones del modelo y los valores reales. vease [[MSE]]

- **Entropía Cruzada Binaria**: Se utiliza para problemas de clasificación binaria. Esta función de pérdida mide qué tan diferente es la distribución de probabilidad predicha por el modelo de la distribución de probabilidad real (que en este caso es una distribución de Bernoulli). vease [[Entropía Cruzada binaria (log loss)]]

- **Entropía Cruzada Categórica**: Se utiliza para problemas de clasificación multiclase. Al igual que la entropía cruzada binaria, mide la diferencia entre la distribución de probabilidad predicha por el modelo y la distribución de probabilidad real, pero en este caso, la distribución real puede ser una distribución multinomial.



<iframe width="560" height="315" src="https://www.youtube.com/embed/uiJiZ3JDafY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

