Los árboles de decisión son uno de los algoritmos de aprendizaje supervisado más comunes y efectivos utilizados en la ciencia de datos y el [[Machine Learning]]. Se utilizan tanto para la [[Clasificación]] como para los problemas de [[Regresión]].

Un árbol de decisión es una estructura similar a un diagrama de flujo donde cada nodo interno representa una "prueba" en un atributo (por ejemplo, si una moneda es cara o cruz), cada rama representa el resultado de esa prueba y cada hoja (o nodo terminal) contiene una etiqueta de clase. El camino desde la raíz hasta una hoja representa la clasificación de una instancia.

La idea es crear un árbol que minimice el costo de clasificar una nueva instancia, basándose en las instancias ya clasificadas.

# Construcción de un árbol de decisión

Para construir un árbol de decisión, se utiliza un algoritmo de dividir y conquistar. Se elige un atributo para dividir el conjunto de datos en subconjuntos que contengan instancias que sean lo más homogéneas posible según la etiqueta de clase. El atributo que mejor separe las instancias se elige utilizando una medida de impureza o diversidad como la [[Entropía]], la ganancia de información, el índice [[Gini]], en casos de calificación, y en casos de regresión,
el error cuadrático medio. 

El proceso se repite de manera recursiva en cada subconjunto hasta que se cumpla una condición de parada, como que todas las instancias en un subconjeto pertenezcan a la misma clase, que se haya alcanzado una profundidad máxima del árbol o que el número de instancias en un subconjunto sea menor a un umbral predefinido.

Una vez construido el árbol, para clasificar una nueva instancia, se comienza en la raíz del árbol y se va descendiendo por las ramas según los valores de los atributos de la instancia hasta llegar a un nodo hoja. La clase asignada a la instancia será la clase mayoritaria en ese nodo hoja.

El árbol de decisión es un modelo interpretable ya que permite entender el proceso de toma de decisiones. Sin embargo, es susceptible al sobreajuste si no se controla su crecimiento y puede ser inestable ante pequeñas variaciones en los datos.

![[Pasted image 20230708095609.png]]

## Ganancia de información

La ganancia de información es un concepto central en la creación de árboles de decisión en aprendizaje automático y ciencia de datos. Se utiliza para decidir qué atributo o característica debe usarse para dividir los datos en un punto específico del árbol.

En términos simples, la ganancia de información se calcula como la diferencia en entropía antes y después de la división de un conjunto de datos en base a un atributo específico. La entropía es una medida de impureza, incertidumbre o desorden. En este contexto, una mayor entropía significa que es más difícil predecir el resultado basándose en los datos actuales.

La fórmula general para calcular la ganancia de información (IG) es:

IG(T, A) = Entropía(T) - Entropía(T | A)

donde:

- T es el conjunto total de datos.
- A es un atributo en los datos.
- IG(T, A) es la ganancia de información al dividir los datos T en base al atributo A.
- Entropía(T) es la entropía del conjunto total de datos.
- Entropía(T | A) es la entropía media de los subconjuntos de datos resultantes al dividir T en base a A.

Al construir un árbol de decisión, se busca el atributo que proporciona la mayor ganancia de información para cada división, ya que este atributo será el más útil para hacer predicciones precisas.

## La pregunta

En los árboles de decisión, la elección de la pregunta para dividir cada nodo se basa en un criterio que busca **mejorar la pureza de los nodos hijos**. 

### Árboles de decisión para clasificación

El objetivo de los árboles de decisión para clasificación es dividir los datos de tal manera que cada grupo resultante sea lo más homogéneo posible en términos de la variable objetivo (la variable que estamos tratando de predecir). Para encontrar la mejor característica y el valor para dividir en cada nodo, los árboles de decisión utilizan una medida de impureza. Las dos más comunes son la [[Entropía]] y el índice [[Gini]].

1. **Entropía**: Esta medida viene de la teoría de la información. Para un conjunto de datos, su entropía es cero cuando todos sus elementos pertenecen a una misma clase. ver 
    
2. **Índice Gini**: Esta medida se deriva de la economía, donde se usa para medir la desigualdad. Un conjunto de datos tiene un índice Gini de cero cuando todos sus elementos pertenecen a una misma clase.


En cada nodo, el árbol de decisión considerará todas las posibles divisiones, calculando la impureza para cada una. Luego, elegirá la división que minimice la impureza.

### Árboles de decisión para regresión

En la regresión, el objetivo es predecir una variable continua en lugar de una categórica. En este caso, la impureza de un nodo se puede medir por el error cuadrático medio (MSE) o el error absoluto medio (MAE) de la variable objetivo en el nodo.

**En cada nodo, el árbol de decisión considerará todas las posibles divisiones y calculará el MSE o MAE para cada una. Luego, elegirá la división que minimice ese error.**


## Cuando para?

La creación de un árbol de decisión se detiene según ciertos criterios de parada que se establecen para prevenir el sobreajuste del modelo. Los criterios de parada más comunes son los siguientes:

### Profundidad máxima del árbol:

Este es uno de los criterios más simples. Si el árbol alcanza una profundidad máxima predeterminada, se detiene la división, independientemente de cuánto podría mejorarse el modelo con divisiones adicionales. Este enfoque es una forma eficaz de prevenir el sobreajuste.

### Número mínimo de instancias por nodo:

Si un nodo tiene un número de instancias menor a un umbral predefinido, entonces ese nodo no se divide, independientemente de cuánto podría mejorarse el modelo con una división adicional. Este enfoque ayuda a garantizar que el modelo no se ajuste excesivamente a las instancias individuales en el conjunto de datos de entrenamiento.

### Reducción mínima en el error:

Si una división propuesta no reduciría el error en al menos un umbral predefinido, entonces esa división no se realiza. Este enfoque ayuda a garantizar que el modelo solo se complica cuando esa complicación aporta una mejora significativa en el rendimiento.

En resumen, la división en un árbol de decisión se detiene cuando se alcanza un criterio de parada predefinido, lo que ayuda a prevenir el sobreajuste y a garantizar que el modelo sea lo suficientemente general como para hacer predicciones precisas en instancias no vistas.

![[Pasted image 20230708100052.png]]


# Ventajas y desventajas

Una de las principales ventajas de los árboles de decisión es su interpretabilidad. Los árboles de decisión pueden visualizarse y entenderse fácilmente, incluso por personas sin conocimientos de aprendizaje automático. Esto los convierte en una buena opción cuando la interpretabilidad es importante.

Otra ventaja es que los árboles de decisión pueden manejar tanto datos numéricos como categóricos, y no requieren suposiciones sobre la distribución de los datos.

Sin embargo, los árboles de decisión también tienen sus desventajas. **Son propensos al sobreajuste, especialmente cuando son muy profundos**. Para evitar esto, es común podar el árbol (eliminar ramas del árbol que aporten poca información) o utilizar métodos de conjunto como [[Random Forest]].

**Además, los árboles de decisión pueden ser inestables, en el sentido de que pequeños cambios en los datos pueden provocar grandes cambios en la estructura del árbol**. Esto también se puede mitigar con métodos de conjunto.

En resumen, los árboles de decisión son un algoritmo de aprendizaje supervisado versátil y fácilmente interpretable, aunque pueden ser propensos al [[Sobreajuste (Overfitting)]] y la inestabilidad. A pesar de estas desventajas, son una herramienta valiosa en la caja de herramientas de cualquier científico de datos.

# Regresión

Los árboles de decisión no sólo se utilizan para problemas de clasificación, sino que también se pueden utilizar para problemas de regresión. En lugar de predecir una clase en cada nodo de hoja, en un problema de regresión, cada nodo de hoja predice un valor numérico. El objetivo de un árbol de decisión de regresión es minimizar la suma de los errores cuadrados.

## Predicción con un árbol de decisión de regresión

Una vez que se ha construido el árbol de decisión de regresión, se puede utilizar para hacer predicciones. Para predecir el valor de una nueva instancia, se recorre el árbol de decisión, empezando por la raíz y siguiendo la rama correspondiente a los valores de los atributos de la instancia, hasta que se llega a un nodo de hoja. **El valor predicho es el valor medio de las instancias del nodo de hoja**.

## Ventajas y desventajas

Las ventajas y desventajas de los árboles de decisión de regresión son similares a las de los árboles de decisión de clasificación. Son fáciles de entender e interpretar, pueden manejar tanto datos numéricos como categóricos y no requieren suposiciones sobre la distribución de los datos. Sin embargo, son propensos al sobreajuste, especialmente si el árbol es muy profundo, y pueden ser inestables, en el sentido de que pequeños cambios en los datos pueden provocar grandes cambios en la estructura del árbol.

# Clasificación

Los árboles de decisión son algoritmos de aprendizaje supervisado que se utilizan tanto para tareas de regresión como de clasificación. En una tarea de clasificación, el árbol de decisión se utiliza para determinar la clase de una instancia dada. 

La estructura de un árbol de decisión es similar a la de un flujo de decisiones, donde cada nodo representa una prueba en un atributo, cada rama representa el resultado de la prueba, y cada hoja representa una clase. La instancia se clasifica siguiendo el camino desde la raíz hasta una hoja basado en los valores de sus atributos.

El proceso de construcción de un árbol de decisión implica seleccionar el mejor atributo para dividir el conjunto de datos en cada paso. La elección del "mejor" atributo puede hacerse de diferentes formas, pero a menudo se basa en medidas de impureza como la entropía o el índice Gini. La idea es que el mejor atributo es el que más reduce la impureza.

![[Pasted image 20230708113659.png]]


# Cálculo de error en árboles de decisión

El cálculo del error en un árbol de decisión depende de si estamos hablando de un problema de regresión o de clasificación.

## Árboles de decisión de regresión

En el caso de un árbol de decisión para regresión, el error se mide típicamente como el error cuadrático medio (MSE) o el error absoluto medio (MAE). 

Para calcular el MSE, se toman las diferencias entre los valores observados y los predichos, se elevan al cuadrado, se suman y se dividen por el número de observaciones. En notación matemática:

$$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$

donde:
* $y_i$ es el valor observado
* $\hat{y}_i$ es el valor predicho
* $n$ es el número total de observaciones

![[Pasted image 20230708100743.png]]

## Árboles de decisión de clasificación

En el caso de un árbol de decisión para clasificación, el error se mide típicamente utilizando la tasa de error de clasificación (misclassification rate), la entropía cruzada o la pérdida logarítmica.

La tasa de error de clasificación es simplemente la fracción de las predicciones que el modelo clasificó incorrectamente. Se calcula sumando el número de errores y dividiendo por el número total de observaciones.

La entropía cruzada y la pérdida logarítmica se utilizan cuando las predicciones son probabilísticas. En lugar de predecir una clase única, el modelo predice una probabilidad para cada clase, y estas medidas evalúan cuán buenas son estas probabilidades.

Por ejemplo, la pérdida logarítmica se calcula de la siguiente manera:

$$ LogLoss = - \frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$

donde:
* $y_i$ es el valor observado
* $\hat{y}_i$ es el valor predicho
* $n$ es el número total de observaciones

Estas son solo algunas de las métricas que se pueden utilizar para evaluar el rendimiento de un árbol de decisión. La elección de la métrica dependerá del problema específico y de los objetivos del modelado.

## Tasa de clasificación errónea (Misclassification Rate)

La tasa de clasificación errónea, también conocida como "misclassification rate", es una métrica utilizada para evaluar el rendimiento de un modelo de clasificación. Esencialmente, mide la proporción de predicciones que el modelo hizo incorrectamente.

La tasa de clasificación errónea se calcula de la siguiente manera:

$$ Misclassification Rate = \frac{1}{n} \sum_{i=1}^{n} I(y_i \neq \hat{y}_i) $$

donde:
* $n$ es el número total de observaciones.
* $y_i$ es la etiqueta verdadera de la i-ésima observación.
* $\hat{y}_i$ es la etiqueta predicha por el modelo para la i-ésima observación.
* $I(.)$ es la función indicadora, que es 1 si la condición dentro del paréntesis es verdadera, y 0 si no lo es.

Entonces, por cada observación, la función indicadora devolverá 1 si la etiqueta verdadera es diferente de la etiqueta predicha (es decir, el modelo hizo una predicción incorrecta), y 0 si las dos etiquetas son iguales (el modelo hizo una predicción correcta). Sumamos todos estos valores y luego los dividimos por el número total de observaciones para obtener la proporción total de predicciones incorrectas.

Es importante tener en cuenta que la tasa de clasificación errónea puede ser una métrica engañosa si las clases están desbalanceadas. Por ejemplo, si el 95% de las observaciones pertenecen a la clase 0 y el 5% a la clase 1, un modelo que predice siempre la clase 0 tendrá una tasa de clasificación errónea del 5%, a pesar de que no es capaz de identificar ninguna observación de la clase 1.

## Error ponderado en un árbol de decisión

La expresión que has proporcionado es una manera de calcular el error de un árbol de decisión, donde el error en cada hoja se pondera por el número de observaciones que caen en esa hoja.

La ecuación se puede desglosar de la siguiente manera:

$$ Err(h) = \sum_{m \in \text{hojas}(h)} \frac{|S_m|}{|S|} Err(y; S_m) $$

Aquí:

- $Err(h)$ es el error total del árbol.
- $S_m$ es el conjunto de observaciones que caen en la m-ésima hoja del árbol.
- $|S_m|$ es el número de observaciones que caen en la m-ésima hoja.
- $|S|$ es el número total de observaciones.
- $\text{hojas}(h)$ es el conjunto de todas las hojas del árbol.
- $Err(y; S_m)$ es el error de la m-ésima hoja.

Esta ecuación calcula el error de cada hoja ($Err(y; S_m)$), lo pondera por la fracción de observaciones que caen en esa hoja ($\frac{|S_m|}{|S|}$), y luego suma estos errores ponderados en todas las hojas del árbol.

Por ejemplo, si estás utilizando un árbol de decisión para la clasificación y calculas $Err(y; S_m)$ como la tasa de clasificación errónea en la m-ésima hoja, entonces $Err(h)$ será la tasa de clasificación errónea ponderada por hoja para todo el árbol. 

Esta medida puede proporcionar una evaluación más precisa del rendimiento del árbol, ya que tiene en cuenta no solo cuántas observaciones se clasifican incorrectamente, sino también dónde ocurren estos errores en el árbol.

![[Pasted image 20230708120954.png]]



# Algunas notas
https://sebastianraschka.com/pdf/lecture-notes/stat451fs20/06-trees__notes.pdf

# Videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/3vZo0ApLz0A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/a-SIt_X0_oY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/cLWZVinpAu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

