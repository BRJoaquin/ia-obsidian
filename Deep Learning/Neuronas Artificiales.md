Las neuronas artificiales, también conocidas como nodos o unidades, son componentes fundamentales de las redes neuronales artificiales. Se llaman "neuronas" porque están inspiradas en las neuronas biológicas que componen el cerebro humano.

![[Pasted image 20230704092521.png]]

Una neurona artificial toma un conjunto de entradas, cada una de las cuales está asociada con un peso. Los pesos son parámetros que la red aprende a través del entrenamiento. A menudo también hay un término de sesgo que se suma a la combinación ponderada de las entradas. Este valor sumado se pasa luego a través de una [[Deep Learning/Función de Activación|función de activación]] para producir la salida de la neurona. El proceso se puede resumir de la siguiente manera:

1. La neurona recibe múltiples entradas y cada entrada se multiplica por su peso correspondiente. Los pesos son simplemente valores numéricos que la neurona ha aprendido durante su entrenamiento.

2. Se suma el resultado de cada entrada ponderada con su respectivo peso, y luego se agrega un valor de sesgo. El sesgo permite desplazar la función de activación a la izquierda o a la derecha, lo que puede ser crítico para el aprendizaje de la neurona.

3. Esta suma ponderada se pasa a través de una función de activación. El propósito de la función de activación es introducir la no linealidad en la salida de la neurona. Esto permite a las redes neuronales modelar relaciones complejas y no lineales entre sus entradas y salidas.

4. El valor resultante se utiliza como entrada para las neuronas en la siguiente capa de la red.


Es importante recordar que, aunque las neuronas artificiales están inspiradas en las neuronas biológicas, son modelos muy simplificados y no reflejan completamente la complejidad y la capacidad de las neuronas biológicas.