![[Pasted image 20230625122840.png]]

El aprendizaje profundo, o deep learning en inglés, es una rama del campo de la [[Inteligencia Artificial]] que se basa en la construcción y entrenamiento de [[Machine Learning para IA/Redes neuronales artificiales]] para aprender y realizar tareas específicas. Las redes neuronales artificiales son modelos matemáticos **inspirados** en el funcionamiento del cerebro humano, compuestos por capas de unidades interconectadas llamadas [[Neuronas Artificiales]].


El término "profundo" en el aprendizaje profundo hace referencia a la estructura de **múltiples capas** en una [[Machine Learning para IA/Redes Neuronales Artificiales]]. Estas capas están **diseñadas para extraer automáticamente características y patrones complejos de los datos de entrada**, permitiendo que el modelo aprenda representaciones cada vez más abstractas a medida que avanza en las capas. En otras palabras, **las capas iniciales pueden detectar características simples como líneas y bordes, mientras que las capas más profundas pueden aprender representaciones más complejas como formas, objetos y conceptos**.

El proceso de entrenamiento de una red neuronal profunda implica presentarle un conjunto de datos de entrenamiento etiquetados, donde las etiquetas representan las salidas esperadas para cada dato de entrada. Durante el entrenamiento, la red **ajusta los pesos y las conexiones entre las neuronas** para minimizar la diferencia entre las salidas predichas y las etiquetas reales. Esto se logra mediante el uso de algoritmos de optimización y retropropagación del error, que permiten propagar el error de salida hacia atrás a través de la red para ajustar los pesos de las conexiones.

Una vez que la red ha sido entrenada, se puede utilizar para realizar predicciones o tomar decisiones sobre nuevos datos de entrada que no se hayan visto durante el entrenamiento. Esto se conoce como la fase de inferencia o evaluación del modelo. El aprendizaje profundo ha demostrado un gran éxito en una amplia gama de aplicaciones, como reconocimiento de imágenes, procesamiento del lenguaje natural, traducción automática, conducción autónoma y mucho más.

Para empezar a aprender y practicar el aprendizaje profundo, es recomendable tener conocimientos básicos de matemáticas, álgebra lineal y cálculo, ya que estos conceptos son fundamentales para comprender las operaciones y los algoritmos utilizados en las redes neuronales.

# Conceptos clave

1. [[Redes Neuronales Artificiales]]: Son modelos matemáticos inspirados en el funcionamiento del cerebro humano, compuestos por capas de unidades interconectadas llamadas neuronas. Las redes neuronales son la base del aprendizaje profundo.

2. [[Neuronas Artificiales]]: Son unidades fundamentales en una red neuronal artificial. Reciben entradas, las combinan mediante una función de activación y generan una salida. Estas salidas se propagan a través de la red para realizar cálculos y tomar decisiones.

3. [[Capas (DL)]]: Las redes neuronales se organizan en capas, que son conjuntos de neuronas. Las capas pueden ser de diferentes tipos, como capas de entrada, capas ocultas y capas de salida. Cada capa procesa la información y la pasa a la siguiente capa.

4. [[Agentes inteligentes/Función de Activación]]: Es una función que determina la salida de una neurona dado un conjunto de entradas. La función de activación introduce no linealidad en la red neuronal y permite modelar relaciones y patrones complejos en los datos.

5. [[Retropropagación del error]]: Es un algoritmo utilizado para entrenar redes neuronales. Consiste en calcular el error entre las salidas predichas y las salidas reales, y luego propagar ese error hacia atrás a través de la red para ajustar los pesos de las conexiones mediante el gradiente descendente.

6. [[Aprendizaje supervisado]]: Es un tipo de entrenamiento en el que se proporciona a la red neuronal un conjunto de datos etiquetados, es decir, datos de entrada junto con las salidas deseadas. La red aprende a relacionar los datos de entrada con las salidas correspondientes, de manera que pueda realizar predicciones precisas en nuevos datos.

7. [[Aprendizaje no supervisado]]: A diferencia del aprendizaje supervisado, en el aprendizaje no supervisado no se proporcionan salidas deseadas durante el entrenamiento. La red neuronal se encarga de encontrar patrones y estructuras ocultas en los datos de entrada por sí misma. Este enfoque es útil para descubrir información subyacente o agrupar datos similares.

8. [[Arquitectura de red]]: Se refiere a la estructura y configuración de una red neuronal. Las redes neuronales pueden tener diferentes arquitecturas, como redes totalmente conectadas, redes convolucionales o redes recurrentes. La elección de la arquitectura depende de la naturaleza de los datos y la tarea a realizar.

9. [[Sobreajuste (Overfitting)]]: Es un fenómeno en el que una red neuronal se ajusta demasiado a los datos de entrenamiento y no generaliza bien a nuevos datos. El sobreajuste puede ocurrir cuando el modelo es demasiado complejo o cuando el conjunto de datos de entrenamiento es insuficiente. Se utilizan técnicas de [[Regularización]] para combatir el sobreajuste.