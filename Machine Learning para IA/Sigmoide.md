La función sigmoide, también conocida como función logística, es una función matemática que toma cualquier número real como entrada y la transforma en un valor comprendido entre 0 y 1. Matemáticamente, se puede representar como:

$$\Large
y = \frac{1}{1 + e^{x}}
$$
![[Pasted image 20230625165818.png]]

En esta fórmula, "e" es la base del logaritmo natural (aproximadamente 2.71828) y "x" es el valor de entrada.

La función sigmoide tiene una forma de "S" y se utiliza comúnmente en campos como la estadística, el aprendizaje automático y la inteligencia artificial. Tiene varias propiedades útiles, entre ellas:

1. Rango acotado: La función sigmoide siempre produce valores en el rango de 0 a 1, lo que la hace adecuada para representar probabilidades o activaciones en modelos de clasificación. vease [[Agentes inteligentes/Función de Activación]]
2. Suavidad: La función sigmoide es una curva suave y diferenciable en todo su dominio, lo que facilita su uso en algoritmos de optimización.
   >En muchos problemas de optimización, se busca encontrar los valores de los parámetros que minimicen o maximicen una función objetivo. La diferenciabilidad de la función objetivo es fundamental para utilizar métodos de optimización que se basan en el cálculo de gradientes, como el descenso de gradiente. Si una función no es diferenciable, estos métodos pueden no funcionar o ser mucho menos eficientes.
3. Transformación no lineal: La función sigmoide permite transformar entradas lineales en salidas no lineales, lo cual es útil para modelar relaciones no lineales en problemas de clasificación y regresión.

En el aprendizaje automático, la función sigmoide se utiliza a menudo como una función de activación en las [[Redes Neuronales Artificiales]], donde se aplica a la salida de cada neurona para introducir no linealidad en el modelo y producir probabilidades o valores de activación que van de 0 a 1. También se utiliza en modelos de [[Regresión logística]], donde se emplea para estimar probabilidades de pertenencia a una clase específica.


![[Pasted image 20231128113423.png]]