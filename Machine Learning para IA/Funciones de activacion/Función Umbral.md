
La **Función Umbral**, también conocida como función escalón de Heaviside, es una [[Función de Activación]] que se utiliza en algunos modelos de [[Machine Learning]]. Es una función binaria que produce una salida de 1 si su entrada es mayor que un cierto valor de umbral y 0 en caso contrario.

En forma de ecuación, la función umbral se puede expresar como:

$$
f(x) = 
\begin{cases} 
1 & \text{if } x > \theta \\
0 & \text{otherwise}
\end{cases}
$$

donde $\theta$ es el valor de umbral.

Esta función de activación es a menudo utilizada en el [[Perceptrón]] simple , que es un modelo de aprendizaje automático para la clasificación binaria. En el Perceptrón Simple, la suma ponderada de las entradas pasa a través de la función umbral para producir la salida, que es una predicción de la clase.

**Es importante notar que la función umbral es una función no diferenciable**, lo que significa que no se puede utilizar con métodos de optimización basados en el gradiente, como el descenso de gradiente. Por esta razón, en la mayoría de las redes neuronales modernas se utilizan otras funciones de activación, como la función logística (o [[Sigmoide]]), la tangente hiperbólica o la [[Función ReLu]] (Rectified Linear Unit), que son diferenciables.
