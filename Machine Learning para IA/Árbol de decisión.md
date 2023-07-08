Los árboles de decisión son uno de los algoritmos de aprendizaje supervisado más comunes y efectivos utilizados en la ciencia de datos y el [[Machine Learning]]. Se utilizan tanto para la [[Clasificación]] como para los problemas de [[Regresión]].

Un árbol de decisión es una estructura similar a un diagrama de flujo donde cada nodo interno representa una "prueba" en un atributo (por ejemplo, si una moneda es cara o cruz), cada rama representa el resultado de esa prueba y cada hoja (o nodo terminal) contiene una etiqueta de clase. El camino desde la raíz hasta una hoja representa la clasificación de una instancia.

La idea es crear un árbol que minimice el costo de clasificar una nueva instancia, basándose en las instancias ya clasificadas.

# Construcción de un árbol de decisión

Para construir un árbol de decisión, se utiliza un algoritmo de dividir y conquistar. Se elige un atributo para dividir el conjunto de datos en subconjuntos que contengan instancias que sean lo más homogéneas posible según la etiqueta de clase. El atributo que mejor separe las instancias se elige utilizando una medida de impureza o diversidad como la [[Entropía]], la ganancia de información, el índice [[Gini]], etc.

Este proceso se repite de forma recursiva hasta que todas las instancias de un subconjunto pertenezcan a la misma clase, o no se pueda mejorar más la homogeneidad. El resultado es un árbol donde cada hoja tiene una única etiqueta de clase.

![[Pasted image 20230708095609.png]]

## La pregunta

En los árboles de decisión, la elección de la pregunta para dividir cada nodo se basa en un criterio que busca mejorar la pureza de los nodos hijos. En el caso de un árbol de decisión de regresión, este criterio se basa generalmente en el error cuadrático medio ([[MSE]], por sus siglas en inglés) o en la suma de los errores cuadrados ([[RSS]], por sus siglas en inglés).

### Error cuadrático medio (MSE) y suma de los errores cuadrados (RSS)

El MSE y el RSS son medidas del error en un modelo de regresión. El MSE se calcula como el promedio de los errores cuadrados, mientras que el RSS es simplemente la suma de los errores cuadrados. En el contexto de los árboles de decisión de regresión, el MSE y el RSS se utilizan para cuantificar cuánto varían los valores objetivo en un nodo dado del árbol.

El objetivo de la división de un nodo es minimizar el MSE o el RSS en los nodos hijos. Para cada posible pregunta (es decir, para cada valor de cada atributo), se calculan el MSE y el RSS en los nodos hijos que resultarían de la división. La pregunta que da como resultado la mayor reducción del MSE o del RSS se selecciona para dividir el nodo.

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

Si una división propuesta no reduciría el error (MSE o RSS) en al menos un umbral predefinido, entonces esa división no se realiza. Este enfoque ayuda a garantizar que el modelo solo se complica cuando esa complicación aporta una mejora significativa en el rendimiento.

En resumen, la división en un árbol de decisión se detiene cuando se alcanza un criterio de parada predefinido, lo que ayuda a prevenir el sobreajuste y a garantizar que el modelo sea lo suficientemente general como para hacer predicciones precisas en instancias no vistas.

![[Pasted image 20230708100052.png]]

# MSE

El Error Cuadrático Medio (MSE, por sus siglas en inglés) de un árbol de decisión de regresión se calcula de la siguiente manera:

1. Para cada nodo terminal (hoja) del árbol, calcula el valor de predicción para ese nodo. En un árbol de decisión de regresión, este valor es simplemente el promedio de los valores objetivo de las instancias de entrenamiento que caen en ese nodo.

2. Para cada instancia de entrenamiento, encuentra el nodo hoja que corresponde a esa instancia y toma el valor de predicción de ese nodo como la predicción del árbol para esa instancia.

3. Calcula la diferencia entre la predicción del árbol y el valor objetivo real para cada instancia de entrenamiento. Eleva al cuadrado cada una de estas diferencias.

4. Suma todas estas diferencias cuadradas y luego divide por el número de instancias de entrenamiento. Este valor es el MSE del árbol de decisión.

![[Pasted image 20230708100743.png]]


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
