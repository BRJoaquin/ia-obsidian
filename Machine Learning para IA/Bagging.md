El Bagging es una técnica de aprendizaje de conjunto que combina las predicciones de varios modelos para obtener una predicción final más robusta y precisa. Fue propuesto por primera vez por Leo Breiman en 1994.

El término 'bagging' es un acrónimo de bootstrap aggregating. 'Bootstrap' se refiere a una técnica de muestreo con reemplazo, y 'aggregating' se refiere a la combinación de las predicciones de los diferentes modelos.

En el bagging, se entrena un conjunto de modelos, cada uno en un subconjunto diferente de los datos de entrenamiento. Estos subconjuntos se generan **mediante muestreo con reemplazo**, lo que significa que algunas observaciones pueden aparecer varias veces en un subconjunto, mientras que otras pueden no aparecer en absoluto.

![[Pasted image 20230708190531.png]]

El proceso de bagging es el siguiente:

1. Generar $B$ (o K) conjuntos de datos de entrenamiento a partir del conjunto de datos de entrenamiento original, mediante muestreo con reemplazo.
2. Entrenar un modelo en cada uno de los $B$ conjuntos de datos.
3. Para hacer una predicción, pasar la observación a través de cada uno de los $B$ modelos y combinar sus predicciones. En el caso de la regresión, la combinación suele ser la media de las predicciones. En el caso de la clasificación, la combinación puede ser un voto mayoritario.

> Cada clasificacador puede ser entrenado en paralelo!

El bagging puede mejorar la precisión de muchos algoritmos de aprendizaje automático y es particularmente **eficaz con los algoritmos que tienen alta varianza** (como los árboles de decisión).

Formalmente, el bagging puede describirse de la siguiente manera:

- Sea $D = {(x_{i}, y_{i})}_{i=1}^{n}$ el conjunto de datos de entrenamiento, donde $x_{i}$ son las características y $y_{i}$ es la etiqueta.
- Seleccionamos un número $B$ de conjuntos de datos de entrenamiento $D_{b}$, cada uno de tamaño $n$, mediante muestreo con reemplazo a partir de $D$.
- Entrenamos un modelo $M_{b}$ en cada conjunto de datos $D_{b}$.
- Para hacer una predicción para una nueva observación $x$, combinamos las predicciones de todos los modelos $M_{b}$:

El bagging es una técnica eficaz para reducir la varianza y mejorar la precisión de los algoritmos de aprendizaje automático. Sin embargo, puede ser computacionalmente costoso debido a la necesidad de entrenar y mantener múltiples modelos.

# Out-of-bag

En el contexto de bagging, "out-of-bag" (OOB) se refiere a las observaciones que no son seleccionadas durante el muestreo con reemplazo para la creación de un subconjunto particular de datos. En otras palabras, son las observaciones que se "quedan fuera" de la muestra bootstrap para un modelo particular.

![[Pasted image 20230708191205.png]]

La proporción de observaciones out-of-bag en un subconjunto de datos particular suele ser de aproximadamente 1/3, mientras que las 2/3 restantes son las observaciones que forman la muestra bootstrap.

![[Pasted image 20230708191230.png]]

La probabilidad de que un dato sea seleccionado en una muestra bootstrap es de 1/N, donde N es el tamaño del conjunto de datos. 
Por lo tanto, la probabilidad de que un dato no sea seleccionado en una sola extracción es de (1 - 1/N). Como se realizan N extracciones (con reemplazo) para formar una muestra bootstrap, la probabilidad de que un dato nunca sea seleccionado (es decir, que sea out-of-bag) es de (1 - 1/N)^N. 
Para N grande, esta probabilidad se aproxima a 1/e, o aproximadamente 0.368, por lo que, en promedio, alrededor del 36.8% de las observaciones quedan out-of-bag.

# Out-of-bag error (OOB error)

El **"out-of-bag error"** (OOB error) es una medida de rendimiento que se calcula usando las observaciones out-of-bag. Para cada observación, se utilizan los modelos para los que la observación estuvo out-of-bag para hacer una predicción. Luego se compara esta predicción con la etiqueta verdadera. El OOB error es la tasa de error o la pérdida promedio de estas predicciones.

![[Pasted image 20230708191918.png]]

El **Out-Of-Bag (OOB) error** juega un papel fundamental en los métodos de bagging y [[Random Forest]] y se usa principalmente por dos razones:

1. **Estimación de la precisión del modelo**: El OOB error es una forma eficiente de estimar la precisión de nuestro modelo. Cada árbol se entrena con un conjunto único de datos de entrenamiento. Por lo tanto, para cada árbol, una parte de los datos (los datos OOB) no se usa en el entrenamiento y puede ser utilizada como un conjunto de prueba. Las predicciones de cada árbol sobre sus datos OOB se pueden usar para estimar la precisión general del modelo, sin necesidad de separar un conjunto de datos de validación adicional. En cierto sentido, el OOB **error proporciona una estimación "gratuita" del error de generalización del modelo**.

2. **Selección de variables**: El OOB error también puede ser utilizado para la selección de variables en random forests. Para esto, el método consiste en permutar los valores de una variable en los datos OOB y medir cuánto aumenta el error OOB. Si una variable es importante, permutar sus valores debería aumentar mucho el error OOB. Por el contrario, si una variable no es relevante para la predicción, permutar sus valores debería tener poco efecto sobre el error OOB. De esta manera, el OOB error permite identificar las variables más importantes en el modelo.
   
   La **importancia de las características por permutación** es una técnica para estimar la importancia de las características al calcular el aumento en el error de predicción después de permutar los valores de la característica. Esta técnica puede ser útil para la selección de características y la interpretación del modelo.
   
   ![[Pasted image 20230708192139.png]]

# Bagging + Arboles de decision = ❤️

El bagging y los árboles de decisión suelen funcionar bien juntos porque los árboles de decisión son propensos al sobreajuste y a tener alta varianza, y el bagging puede ayudar a reducir esta varianza. Además, los árboles de decisión pueden capturar interacciones complejas en los datos, y el bagging puede ayudar a estabilizar estas estimaciones. Por último, los árboles de decisión son modelos no lineales y no paramétricos, lo que los hace flexibles y capaces de adaptarse a diferentes formas de los datos, lo que es beneficioso en el marco de bagging.
vease [[Random Forest]]

# Video


<iframe width="560" height="315" src="https://www.youtube.com/embed/pWSULhaZlQM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>