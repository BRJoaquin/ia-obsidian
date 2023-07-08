Los árboles de decisión son uno de los algoritmos de aprendizaje supervisado más comunes y efectivos utilizados en la ciencia de datos y el [[Machine Learning]]. Se utilizan tanto para la [[Clasificación]] como para los problemas de [[Regresión]].

Un árbol de decisión es una estructura similar a un diagrama de flujo donde cada nodo interno representa una "prueba" en un atributo (por ejemplo, si una moneda es cara o cruz), cada rama representa el resultado de esa prueba y cada hoja (o nodo terminal) contiene una etiqueta de clase. El camino desde la raíz hasta una hoja representa la clasificación de una instancia.

La idea es crear un árbol que minimice el costo de clasificar una nueva instancia, basándose en las instancias ya clasificadas.

# Construcción de un árbol de decisión

Para construir un árbol de decisión, se utiliza un algoritmo de dividir y conquistar. Se elige un atributo para dividir el conjunto de datos en subconjuntos que contengan instancias que sean lo más homogéneas posible según la etiqueta de clase. El atributo que mejor separe las instancias se elige utilizando una medida de impureza o diversidad como la [[Entropía]], la ganancia de información, el índice [[Gini]], etc.

Este proceso se repite de forma recursiva hasta que todas las instancias de un subconjunto pertenezcan a la misma clase, o no se pueda mejorar más la homogeneidad. El resultado es un árbol donde cada hoja tiene una única etiqueta de clase.

![[Pasted image 20230708095609.png]]

## La pregunta

En los árboles de decisión, la elección de la pregunta para dividir cada nodo se basa en un criterio que busca mejorar la pureza de los nodos hijos. 

### Reducción de la varianza

La reducción de la varianza se refiere a la disminución del MSE o del RSS que resulta de la división de un nodo. Cuanto mayor sea la reducción de la varianza, mejor será la pregunta para dividir el nodo.

La reducción de la varianza se calcula como la diferencia entre el MSE o el RSS en el nodo antes de la división y el MSE o el RSS ponderados en los nodos hijos después de la división. El objetivo es maximizar la reducción de la varianza.

![[Pasted image 20230708095850.png]]

### Recursive Binary Splitting

El Recursive Binary Splitting es el algoritmo utilizado para construir árboles de decisión. Es un algoritmo de tipo divide y conquista que opera de forma recursiva.

El algoritmo empieza en la raíz del árbol, con todas las instancias del conjunto de datos. A continuación, se busca la mejor pregunta para dividir las instancias en dos subconjuntos, utilizando el criterio de reducción de la varianza.

Una vez que se ha encontrado la mejor pregunta, se divide el conjunto de datos y se repite el proceso en cada uno de los subconjuntos resultantes. Este proceso de dividir el conjunto de datos y buscar la mejor pregunta en cada subconjunto se repite de forma recursiva hasta que se alcanza un criterio de parada, como una profundidad máxima del árbol o un número mínimo de instancias por nodo de hoja.

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

Además, los árboles de decisión pueden ser inestables, en el sentido de que pequeños cambios en los datos pueden provocar grandes cambios en la estructura del árbol. Esto también se puede mitigar con métodos de conjunto.

En resumen, los árboles de decisión son un algoritmo de aprendizaje supervisado versátil y fácilmente interpretable, aunque pueden ser propensos al [[Sobreajuste (Overfitting)]] y la inestabilidad. A pesar de estas desventajas, son una herramienta valiosa en la caja de herramientas de cualquier científico de datos.


# Regresión

Los árboles de decisión no sólo se utilizan para problemas de clasificación, sino que también se pueden utilizar para problemas de regresión. En lugar de predecir una clase en cada nodo de hoja, en un problema de regresión, cada nodo de hoja predice un valor numérico. El objetivo de un árbol de decisión de regresión es minimizar la suma de los errores cuadrados.

Aquí está la descripción detallada de cómo se construye un árbol de decisión de regresión:

## Construcción de un árbol de decisión de regresión

La construcción de un árbol de decisión de regresión es similar a la construcción de un árbol de decisión de clasificación, pero con una diferencia clave: en lugar de utilizar una medida de impureza para elegir el atributo en el que se dividirán los datos, se utiliza una medida de error, como la suma de los errores cuadrados.

El algoritmo de construcción del árbol de decisión intenta minimizar este error de las siguientes maneras:

1. Para cada atributo en el conjunto de datos, el algoritmo intenta encontrar un punto de división que minimice la suma de los errores cuadrados para los subconjuntos resultantes. Para hacer esto, el algoritmo prueba todos los posibles puntos de división y selecciona el que da como resultado la menor suma de los errores cuadrados.

2. Una vez que se ha encontrado el mejor punto de división para cada atributo, el algoritmo selecciona el atributo que da como resultado la menor suma de los errores cuadrados y divide los datos según el mejor punto de división para ese atributo.

3. Este proceso se repite de forma recursiva en cada subconjunto resultante hasta que se alcanza un criterio de parada, como una profundidad máxima del árbol o un número mínimo de instancias por nodo de hoja.

## Predicción con un árbol de decisión de regresión

Una vez que se ha construido el árbol de decisión de regresión, se puede utilizar para hacer predicciones. Para predecir el valor de una nueva instancia, se recorre el árbol de decisión, empezando por la raíz y siguiendo la rama correspondiente a los valores de los atributos de la instancia, hasta que se llega a un nodo de hoja. **El valor predicho es el valor medio de las instancias del nodo de hoja**.

## Ventajas y desventajas

Las ventajas y desventajas de los árboles de decisión de regresión son similares a las de los árboles de decisión de clasificación. Son fáciles de entender e interpretar, pueden manejar tanto datos numéricos como categóricos y no requieren suposiciones sobre la distribución de los datos. Sin embargo, son propensos al sobreajuste, especialmente si el árbol es muy profundo, y pueden ser inestables, en el sentido de que pequeños cambios en los datos pueden provocar grandes cambios en la estructura del árbol.

En resumen, los árboles de decisión de regresión son una herramienta valiosa para la regresión, con la capacidad de proporcionar modelos interpretables y manejar una variedad de tipos de datos.


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



