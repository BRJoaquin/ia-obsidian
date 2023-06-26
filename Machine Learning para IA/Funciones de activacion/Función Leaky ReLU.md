La **Leaky ReLU** es una variante de la [[Función ReLu]] que se propuso para solucionar el problema de las **"neuronas muertas"** en una red neuronal. En una ReLU, las entradas negativas se convierten en cero, lo que puede causar que las neuronas dejen de aprender si siempre se activan a cero (un problema conocido como "neuronas muertas").

La Leaky ReLU modifica la función para permitir pequeños valores negativos cuando la entrada es menor que cero. Tiene la forma:

$$
f(x) = 
\begin{cases} 
x & \text{if } x > 0 \\
\alpha x & \text{if } x \leq 0
\end{cases}
$$

donde $x$ es la entrada a la función y $\alpha$ es un pequeño coeficiente que generalmente se establece en 0.01. 

Por lo tanto, en lugar de aplastar todos los valores negativos a cero como la ReLU, la Leaky ReLU permite que estos valores se "filtren" a través, proporcionando una pequeña gradiente negativa.

Este ajuste ayuda a mitigar el problema de las "neuronas muertas" y puede ayudar a mejorar el rendimiento de la red. Sin embargo, la Leaky ReLU aún mantiene la mayoría de las propiedades que hacen que la ReLU sea atractiva para su uso en redes neuronales, como su simplicidad y eficiencia computacional.


![[Pasted image 20230626090511.png]]