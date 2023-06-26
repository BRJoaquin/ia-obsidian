![[Pasted image 20230626084514.png]]

El **Perceptrón Multicapa (MLP, por sus siglas en inglés)** es un **tipo**  de [[Redes Neuronales Artificiales]] feedforward (o adelante directa). Un MLP consta de al menos tres capas de nodos: una capa de entrada, una o más capas ocultas y una capa de salida.

**A diferencia del Perceptrón Simple, que solo puede separar linealmente los datos, el MLP puede distinguir datos que no son linealmente separables, gracias a la inclusión de una o más capas ocultas.**

La operación en cada nodo es la misma que en el Perceptrón Simple: se toma la suma ponderada de las entradas, se le añade un sesgo y luego se pasa el resultado a través de una [[Función de Activación]]. Sin embargo, en un MLP, la salida de los nodos en una capa sirve como entrada a los nodos de la siguiente capa.

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

El MLP se entrena ajustando los pesos y los sesgos para minimizar una función de pérdida, a menudo utilizando un algoritmo de optimización como el [[Decenso de Gradiente]]. El proceso de entrenamiento se realiza a través de un proceso llamado **retropropagación**, que consiste en pasar el error de la salida hacia atrás a través de la red para ajustar los pesos y los sesgos.
