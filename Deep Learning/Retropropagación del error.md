La **Retropropagación** es un método eficiente para calcular el gradiente de la [[Función de pérdida]] con **respecto a los pesos en una red neuronal**. Se utiliza en el proceso de entrenamiento de una red neuronal para realizar ajustes a los pesos y sesgos en función del error calculado.

La retropropagación se basa en el principio del cálculo del gradiente y la regla de la cadena. Aquí te dejo un resumen de los pasos:

1. **Feedforward**: Las entradas se pasan a través de la red para obtener la salida de la red neuronal.

2. **Cálculo de la pérdida**: La salida de la red se compara con la salida deseada utilizando una función de pérdida para calcular el error.

3. **Backpropagation del error**: Aquí es donde realmente entra en juego la retropropagación. Para cada nodo en cada capa de la red, empezando por la última capa (la capa de salida), calculamos qué tanto contribuye ese nodo al error total, en función de sus pesos. Este "error" se propaga hacia atrás, de ahí el nombre de retropropagación.

4. **Actualización de los pesos y sesgos**: Usando el error calculado y el gradiente de la función de pérdida, ajustamos los pesos y sesgos para minimizar el error. El grado de ajuste se controla por la tasa de aprendizaje.

Este procedimiento se repite para cada entrada de datos de entrenamiento hasta que el modelo esté suficientemente entrenado, es decir, hasta que la función de pérdida se minimice.

La belleza de la retropropagación es que nos permite actualizar todos los pesos de la red neuronal de manera simultánea, **tomando en cuenta su contribución relativa al error**. Sin embargo, esto no significa que la retropropagación no tenga desafíos. Por ejemplo, puede sufrir del problema del "desvanecimiento del gradiente", en el que los gradientes se vuelven muy pequeños a medida que se retropropagan hacia las primeras capas de la red. Esto puede hacer que el aprendizaje sea muy lento o incluso que se detenga. Se han desarrollado varias técnicas para abordar este problema, como las funciones de activación ReLU y sus variantes, la normalización de lotes y las redes neuronales de "residual learning".

# Matemáticas detrás de la Retropropagación

1. **Feedforward**: Durante esta etapa, las entradas se pasan a través de la red para producir una salida. Para cada capa, se calcula la suma ponderada de las entradas (que es el producto punto entre los pesos y las entradas) y luego se pasa por una función de activación para producir la salida de esa capa. Esto se repite hasta que se llega a la capa de salida.

2. **Cálculo del error**: Luego, se calcula el error de la red utilizando la función de pérdida. Esto generalmente implica tomar la diferencia entre la salida de la red y la salida deseada (etiqueta), y aplicar alguna función a esta diferencia (por ejemplo, cuadrarla en el caso del error cuadrático medio).

3. **Retropropagación del error**: En esta etapa, calculamos el gradiente de la función de pérdida con respecto a los pesos. Comenzamos con la última capa y avanzamos hacia atrás. Para cada peso, calculamos cuánto cambiaría la función de pérdida si cambiáramos ese peso un poco. Esto se hace utilizando la regla de la cadena.

   **La regla de la cadena es una fórmula en cálculo que nos dice cómo calcular la derivada de una función compuesta.** En el caso de una red neuronal, la función de pérdida es una función compuesta que depende de la salida de la red, que a su vez depende de las sumas ponderadas y las activaciones en cada capa, que a su vez dependen de los pesos.

   Entonces, para calcular el gradiente de la función de pérdida con respecto a un peso, aplicamos la regla de la cadena para descomponer este cálculo en el producto de varios términos más simples: el gradiente de la función de pérdida con respecto a la salida de la red, el gradiente de la salida de la red con respecto a las sumas ponderadas y activaciones, y el gradiente de las sumas ponderadas y activaciones con respecto al peso.

4. **Actualización de los pesos**: Una vez que tenemos el gradiente de la función de pérdida con respecto a los pesos, podemos usar este gradiente para actualizar los pesos. La idea es ajustar cada peso en la dirección que reduce la función de pérdida. Esto se hace restando una fracción del gradiente al peso. La fracción es determinada por la tasa de aprendizaje, un hiperparámetro que controla cuánto cambiamos los pesos en cada iteración.

La retropropagación es un algoritmo eficiente para calcular los gradientes que se necesitan en el proceso de entrenamiento de una red neuronal. Aunque puede ser un poco intimidante desde el punto de vista matemático, en esencia es sólo una aplicación de la regla de la cadena del cálculo diferencial.





<iframe width="560" height="315" src="https://www.youtube.com/embed/eNIqz_noix8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>