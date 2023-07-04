Una capa en una [[Redes Neuronales Artificiales]] es un conjunto de [[Neuronas Artificiales]], también conocidas como nodos, que procesan diferentes partes de la información de entrada. Cada neurona en una capa toma un conjunto de entradas, las pondera según pesos previamente aprendidos o inicializados aleatoriamente, las suma y luego aplica una [[Machine Learning para IA/Función de Activación|Función de Activación]] a la suma para generar una salida.

Existen tres tipos principales de capas en una red neuronal:

1. **Capa de entrada (Input Layer)**: Esta es la capa que recibe los datos de entrada directamente. La cantidad de nodos en esta capa suele corresponder a la cantidad de características en los datos de entrada. Por ejemplo una imagen puede ser la cantidad de pixeles de dicha imagen.

2. **Capas ocultas (Hidden Layers)**: Estas son las capas entre la capa de entrada y la capa de salida. Cada capa oculta recibe entradas de la capa anterior (ya sea la capa de entrada o otra capa oculta), realiza cálculos y pasa la salida a la próxima capa. Una red neuronal puede tener cualquier número de capas ocultas, y el número de nodos en cada capa puede variar. Estas capas son las responsables de la mayor parte del aprendizaje realizado por la red.

3. **Capa de salida (Output Layer)**: Esta es la última capa en una red neuronal. Toma las salidas de la última capa oculta y realiza cálculos finales para generar la salida final de la red. En una tarea de clasificación, por ejemplo, esta capa podría tener tantos nodos como clases existen en el problema, y la función de activación a menudo es la función Softmax para proporcionar probabilidades de pertenencia a cada clase.

![[Pasted image 20230704092258.png]]

En general, cada capa de una red neuronal puede aprender a identificar diferentes características en los datos de entrada. Las primeras capas podrían aprender a identificar características de bajo nivel, como líneas o colores en imágenes, mientras que las capas más profundas pueden aprender a identificar conceptos más complejos a partir de las características identificadas por las capas anteriores.