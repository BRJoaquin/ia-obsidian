![[Pasted image 20230626084514.png]]

El **Perceptrón Multicapa (MLP, por sus siglas en inglés)** es un **tipo**  de [[Redes Neuronales Artificiales]] feedforward (o adelante directa). Un MLP consta de al menos tres capas de nodos: una capa de entrada, una o más capas ocultas y una capa de salida.

**A diferencia del Perceptrón Simple, que solo puede separar linealmente los datos, el MLP puede distinguir datos que no son linealmente separables, gracias a la inclusión de una o más capas ocultas.**

La operación en cada nodo es la misma que en el Perceptrón Simple: se toma la suma ponderada de las entradas, se le añade un sesgo y luego se pasa el resultado a través de una [[Deep Learning/Función de Activación|Función de Activación]]. Sin embargo, en un MLP, la salida de los nodos en una capa sirve como entrada a los nodos de la siguiente capa.

En forma de ecuación, un nodo en un MLP se ve así:

$$\Large
y = f(\mathbf{w} \cdot \mathbf{x} + b)
$$

donde:
- $\mathbf{w}$ es el **vector** de pesos.
- $\mathbf{x}$ es el **vector** de entradas.
- $b$ es el sesgo.
- $f$ es la función de activación.
- $\cdot$ denota el producto escalar.

En un MLP, la función de activación a menudo no es una [[Función Umbral]], sino una función no lineal como la [[Función Sigmoide]] (o [[Sigmoide]]), la función tangente hiperbólica o la [[Función ReLu]] (Rectified Linear Unit).

El MLP se entrena ajustando los pesos y los sesgos para minimizar una función de pérdida, a menudo utilizando un algoritmo de optimización como el [[Descenso de Gradiente]]. El proceso de entrenamiento se realiza a través de un proceso llamado **retropropagación**, que consiste en pasar el error de la salida hacia atrás a través de la red para ajustar los pesos y los sesgos.

# Actualización de Pesos

Los pesos en un **Perceptrón Multicapa (MLP)** se actualizan durante el proceso de entrenamiento. El objetivo del entrenamiento es minimizar la [[Función de pérdida]], una medida del error entre las predicciones del modelo y los valores reales.

Para actualizar los pesos, se utiliza un algoritmo llamado [[Retropropagación del error]] (backpropagation) en combinación con un método de optimización, comúnmente el [[Descenso de Gradiente]] o alguna de sus variantes (como el Descenso de Gradiente Estocástico o Adam).

El proceso general para la actualización de pesos es el siguiente:

1. **Feedforward**: Las entradas se pasan a través de la red, capa por capa, hasta que se generan las salidas.

2. **Cálculo de la Pérdida**: Se calcula la función de pérdida utilizando las salidas de la red y los valores reales. vease [[Función de pérdida]]

3. **Backpropagation**: Se calculan las derivadas parciales de la función de pérdida con respecto a cada uno de los pesos en la red (es decir, el gradiente de la pérdida con respecto a los pesos). Este proceso se realiza retrocediendo a través de la red, comenzando con la capa de salida y yendo hacia las capas de entrada. vease [[Retropropagación del error]]

4. **Actualización de Pesos**: Los pesos se actualizan restando una fracción del gradiente calculado en el paso 3. La fracción se determina por la tasa de aprendizaje ([[Taza de aprendizaje]]), un parámetro que se establece antes de comenzar el entrenamiento.

# Funciones de Pérdida

La elección de la [[Función de pérdida|función de pérdida]] en un MLP depende del tipo de problema que se esté resolviendo. Aquí algunos ejemplos de funciones de pérdida comunes:

- **Error Cuadrático Medio (MSE)**: Se utiliza comúnmente para problemas de regresión. Esta función de pérdida calcula la media de los cuadrados de las diferencias entre las predicciones del modelo y los valores reales. vease [[MSE]]

- **Entropía Cruzada Binaria**: Se utiliza para problemas de clasificación binaria. Esta función de pérdida mide qué tan diferente es la distribución de probabilidad predicha por el modelo de la distribución de probabilidad real (que en este caso es una distribución de Bernoulli). vease [[Entropía Cruzada binaria (log loss)]]

- **Entropía Cruzada Categórica**: Se utiliza para problemas de clasificación multiclase. Al igual que la entropía cruzada binaria, mide la diferencia entre la distribución de probabilidad predicha por el modelo y la distribución de probabilidad real, pero en este caso, la distribución real puede ser una distribución multinomial. vease [[Entropía Cruzada Categórica]]
