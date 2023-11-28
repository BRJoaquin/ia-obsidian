Las **Redes Neuronales Artificiales (ANN)** son una rama del aprendizaje automático que se inspira en la estructura y el funcionamiento de las redes neuronales biológicas. En el ámbito de la inteligencia artificial, una ANN es un modelo computacional diseñado para simular la forma en que un cerebro humano analiza y procesa la información.

![[Pasted image 20230626093910.png]]

# Estructura de las ANN

Una ANN se compone de una serie de nodos interconectados llamados "neuronas" o "nodos" (vease [[Neuronas Artificiales]]). Estas neuronas se organizan en diferentes capas (vease [[Capa (DL)]]):

1. **Capa de entrada**: Esta es la capa que recibe la entrada del exterior (por ejemplo, los datos de entrenamiento).

2. **Capas ocultas**: Estas son las capas entre la capa de entrada y la capa de salida. Pueden ser pocas o muchas dependiendo de la profundidad de la red.

3. **Capa de salida**: Esta capa produce el resultado final de la red.

Cada neurona en una capa está conectada a todas las neuronas de la capa siguiente, con cada conexión tiene un "peso" asociado, que se ajusta durante el entrenamiento de la red.

# Funcionamiento de las ANN

El funcionamiento de una ANN se basa en la propagación hacia adelante de las señales a través de la red y el ajuste de los pesos mediante el algoritmo de retropropagación del error.

1. **Propagación hacia adelante (Feedforward)**: La entrada se propaga desde la capa de entrada, a través de las capas ocultas, hasta la capa de salida. Cada neurona recibe la suma ponderada de las salidas de las neuronas de la capa anterior y aplica una función de activación a esta suma para producir su propia salida.

2. **Retropropagación (Backpropagation)**: Este es el proceso de ajuste de los pesos de la red. Después de la propagación hacia adelante, se calcula la diferencia entre la salida de la red y la salida deseada (el "error"). Luego, este error se propaga hacia atrás a través de la red, ajustando los pesos de manera que minimicen el error. vease [[Retropropagación del error]]

# Aplicaciones de las ANN

Las ANN se utilizan en una amplia gama de aplicaciones, incluyendo:

- Reconocimiento de voz, de imágenes y de patrones.
- Procesamiento del lenguaje natural.
- Sistemas de recomendación.
- Diagnóstico médico.
- Análisis financiero.
- Control autónomo de vehículos.

Las redes neuronales artificiales son una herramienta potente y flexible en el campo de la inteligencia artificial y el aprendizaje automático.


# Importancia de las Funciones de Activación

Las **funciones de activación** son un componente esencial de las redes neuronales artificiales y juegan un papel vital en su capacidad para aprender y realizar predicciones. Aquí están algunas de las razones por las cuales son importantes:

1. **No linearidad**: Las funciones de activación introducen no linearidad en el modelo. Sin una función de activación, una red neuronal, sin importar cuántas capas tenga, sería equivalente a un único modelo de regresión lineal. Las funciones de activación permiten a la red aprender de datos más complejos y realizar tareas más allá de la simple clasificación o regresión lineal.

2. **Derivabilidad**: Muchos algoritmos de aprendizaje para redes neuronales, como la retropropagación, requieren que las funciones utilizadas en la red sean derivables. Las funciones de activación comúnmente usadas, como la función sigmoide, la función tangente hiperbólica y la función ReLU, son todas derivables.

3. **Normalización**: Algunas funciones de activación, como la función sigmoide o la tangente hiperbólica, acotan la salida de la neurona a un rango específico. Esto puede ser útil para mantener los valores de la red bajo control y evitar problemas de estabilidad numérica durante el entrenamiento.

4. **Activación esparza**: Algunas funciones de activación, como la función ReLU y sus variantes, inducen lo que se llama activación esparza. Esto significa que sólo un subconjunto de las neuronas se activará en un momento dado, haciendo que la red sea más eficiente y también ayudando a evitar problemas de sobreajuste.

5. **Decidibilidad**: Las funciones de activación actúan como un umbral de decisión. Si la suma ponderada de las entradas a la neurona supera un cierto valor (el "punto de activación" de la función de activación), entonces la neurona se activará y transmitirá información a la siguiente capa. Esto es análogo al modo en que las neuronas biológicas disparan un impulso eléctrico cuando reciben suficiente entrada.

Por todas estas razones, las funciones de activación son un componente crucial de las redes neuronales.

# Tipos de Redes Neuronales Artificiales (ANN)

Las ANN pueden tener diversas arquitecturas, cada una de las cuales es adecuada para un tipo específico de tarea de aprendizaje automático. A continuación, se presentan algunos de los tipos más comunes de ANN:

1. **Perceptrón Multicapa (MLP)**: Este es el tipo más básico de red neuronal y consiste en tres partes: una capa de entrada, una o más capas ocultas y una capa de salida. Las MLP son adecuadas para problemas de clasificación y regresión. vease [[Perceptrón Multicapa]]

2. **Redes Neuronales Convolucionales (CNN)**: Las CNN son especialmente buenas para trabajar con datos que tienen una estructura de cuadrícula espacial, como las imágenes. Las CNN utilizan capas convolucionales que aplican filtros a una porción local del input. vease [[Redes Neuronales Convolucionales]]

3. **Redes Neuronales Recurrentes (RNN)**: Las RNN son efectivas para procesar secuencias de datos, como series temporales o texto, porque son capaces de "recordar" entradas anteriores en la secuencia al pasar su estado oculto de un paso de tiempo al siguiente.

4. **Long Short-Term Memory (LSTM)**: LSTM es un tipo especial de RNN que evita el problema del "desvanecimiento del gradiente" (dificultad para aprender y ajustar los parámetros en las RNN debido a los gradientes que se vuelven muy pequeños) que suelen tener las RNN.

5. **Redes Adversarias Generativas (GAN)**: Las GAN constan de dos partes: un generador que produce datos y un discriminador que trata de distinguir entre los datos reales y los datos generados por el generador. Las GAN se utilizan a menudo para generar nuevos datos que se parecen a algunos datos de entrenamiento dados.

6. **Autoencoders (AE)**: Los AE son redes neuronales utilizadas para la reducción de dimensionalidad y la detección de anomalías. Aprenden a comprimir los datos de entrada en una representación de menor dimensión y luego a reconstruir los datos originales a partir de esta representación.

Estos son sólo algunos ejemplos de los tipos de redes neuronales que existen. Cada tipo tiene sus propias fortalezas y debilidades, y la elección del tipo de red a utilizar dependerá en gran medida de la tarea específica que se esté tratando de resolver.

ver ademas [[Parametros aprendibles (Learnable Parameters)]]
<iframe width="560" height="315" src="https://www.youtube.com/embed/MRIv2IwFTPg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/uwbHOpp9xkc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/eNIqz_noix8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/hfK_dvC-avg?si=SGAXN7LTKpVD0SwC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
