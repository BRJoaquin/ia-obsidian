K-Nearest Neighbors (KNN) es un algoritmo de aprendizaje supervisado simple y fácil de entender que se utiliza tanto para tareas de [[Clasificación]] como de [[Regresión]]. Aunque es fácil de entender, KNN puede ser muy potente en aplicaciones prácticas, especialmente cuando se combina con técnicas de preprocesamiento de datos adecuadas.

# ¿Cómo funciona KNN?

KNN funciona sobre la base de la idea de que las observaciones en un conjunto de datos están cerca de otras observaciones que son similares. De esta manera, el algoritmo KNN asigna una observación a la clase que es más común entre sus K vecinos más cercanos.

En el caso de la clasificación, una observación se clasifica según la mayoría de sus vecinos más cercanos. Por ejemplo, si se eligiera k=3, una observación no clasificada se asignaría a la clase a la que pertenecen la mayoría de sus tres vecinos más cercanos. 

En el caso de la regresión, el valor de una observación no clasificada sería la media (o mediana) de los valores de sus vecinos más cercanos.

La "distancia" entre las observaciones se mide normalmente mediante la distancia euclidiana, aunque también se pueden utilizar otras métricas de distancia, como la distancia de Manhattan o la distancia de Minkowski.

# Ventajas y desventajas de KNN

Una de las ventajas de KNN es su simplicidad. No requiere ningún entrenamiento, lo que lo hace muy rápido para agregar nuevas observaciones a los datos. Además, KNN es un algoritmo no paramétrico, lo que significa que no hace supuestos sobre la distribución de los datos subyacentes.

Sin embargo, KNN también tiene algunas desventajas. En primer lugar, puede ser computacionalmente costoso en términos de memoria y tiempo de cálculo, especialmente cuando se trata de conjuntos de datos grandes con muchas características, ya que cada predicción requiere el cálculo de la distancia a todas las observaciones en los datos de entrenamiento. En segundo lugar, KNN puede ser sensible a la escala de las características, lo que significa que las características con rangos de valores más grandes pueden dominar en la medida de la distancia. Para mitigar esto, es importante escalar las características antes de usar KNN. Finalmente, elegir el valor correcto de k puede ser un desafío y puede requerir pruebas y ajustes.

# Elección de K en KNN

La elección del valor de k en KNN es crucial. Un valor de k demasiado pequeño puede hacer que el algoritmo sea sensible al [[Ruido]] y a los valores atípicos ([[Outlier]], lo que puede llevar al sobreajuste. Por otro lado, un valor de k demasiado grande puede hacer que el algoritmo sea insensible a las características locales de los datos, lo que puede llevar al subajuste. La elección de k suele hacerse a través de la [[Validación cruzada (Cross-validation)]].

![[Pasted image 20230707162403.png]]

# Aplicaciones de KNN

KNN se utiliza en una variedad de aplicaciones, como la recomendación de productos, la clasificación de documentos, el reconocimiento de patrones, la detección de anomalías y la imputación de datos faltantes. Aunque es un algoritmo relativamente simple, su flexibilidad y facilidad de uso hacen que sea una herramienta valiosa para cualquier científico de datos.

El algoritmo de los k-vecinos más cercanos (KNN, por sus siglas en inglés) es una técnica de aprendizaje supervisado comúnmente asociada con problemas de clasificación. Sin embargo, KNN también puede utilizarse para resolver problemas de regresión, es decir, cuando la variable objetivo es continua en lugar de categórica. En este contexto, KNN se utiliza para predecir un valor numérico a partir de los valores numéricos de los vecinos más cercanos.

# Rendimiento

Los K-Vecinos más Cercanos (KNN) es un algoritmo computacionalmente costoso debido a que requiere calcular las distancias a todas las muestras en el conjunto de datos para cada predicción. Específicamente, KNN tiene un tiempo de ejecución de $O(DN)$, donde $D$ es la dimensión de los datos (el número de características) y $N$ es el número de muestras en el conjunto de datos. Como resultado, KNN puede ser lento para grandes conjuntos de datos y/o datos de alta dimensión.

Para mejorar la eficiencia, se han desarrollado estructuras de datos especiales, como los árboles Ball y KD, que permiten realizar búsquedas más rápidas de los vecinos más cercanos.

## Ball-Tree y KD-Tree

Un **Ball-Tree** es una estructura de datos de árbol binario que particiona los datos en una serie de nodos hiperesféricos o "bolas". Cada nodo en el árbol representa una "bola", que contiene un subconjunto de los puntos de los datos. El Ball-Tree acelera las búsquedas de los vecinos más cercanos al eliminar rápidamente las bolas que están demasiado lejos para contener los vecinos más cercanos.

Un **KD-Tree** (árbol de k-dimensional) es otro tipo de estructura de árbol binario que particiona los datos a lo largo de los ejes de las características. Al igual que el Ball-Tree, el KD-Tree permite realizar búsquedas de los vecinos más cercanos de manera más eficiente al eliminar rápidamente las regiones del espacio de características que están demasiado lejos para contener los vecinos más cercanos.

Ambos árboles, Ball y KD, pueden acelerar considerablemente las consultas de los vecinos más cercanos en datos de baja a moderada dimensión. Sin embargo, su rendimiento tiende a degradarse a medida que la dimensión de los datos aumenta, lo que nos lleva a la maldición de la dimensionalidad.

## Maldición de la dimensionalidad

La maldición de la dimensionalidad se refiere al fenómeno por el cual la dificultad para manejar, procesar y generalizar datos aumenta exponencialmente con cada dimensión adicional en el conjunto de datos. En el caso de KNN, la maldición de la dimensionalidad se manifiesta de varias maneras.

Primero, a medida que la dimensión de los datos aumenta, la distancia entre cualquier par de puntos tiende a ser más similar, lo que hace que la noción de "cercanía" sea menos útil. Esto puede hacer que KNN sea menos efectivo en datos de alta dimensión.

Segundo, debido a la creciente similitud en las distancias, se requieren más datos para mantener la misma densidad de muestras en un espacio de alta dimensión, lo que puede hacer que KNN sea ineficaz en conjuntos de datos de alta dimensión con un número limitado de muestras.

Tercero, el costo computacional de calcular las distancias en un espacio de alta dimensión puede ser considerable. Aunque las estructuras de datos como los árboles Ball y KD pueden ayudar, su eficacia se reduce a medida que la dimensión de los datos aumenta.

En resumen, aunque KNN puede ser un algoritmo de aprendizaje automático útil, es importante tener en cuenta sus limitaciones y desafíos, especialmente cuando se trabaja con datos de alta dimensión.


# KNN en regresión

## ¿Cómo funciona KNN en regresión?

El principio fundamental de KNN en regresión sigue siendo el mismo que en la clasificación: las observaciones similares están cerca unas de otras. La "similitud" se mide generalmente en términos de una métrica de distancia, como la distancia euclidiana, aunque otras métricas también pueden ser apropiadas dependiendo del problema.

Sin embargo, la principal diferencia entre la regresión y la clasificación en el contexto de KNN es cómo se utiliza la información de los vecinos más cercanos para hacer una predicción. En la clasificación, una nueva observación se asigna a la clase que es más común entre sus k vecinos más cercanos. En la regresión, por otro lado, se predice un valor numérico para una nueva observación calculando un resumen estadístico, como la media o la mediana, de los valores numéricos de sus k vecinos más cercanos.

Por ejemplo, considera un problema de regresión en el que estás tratando de predecir el precio de una casa basándote en sus características, como el número de habitaciones, la superficie habitable, la edad de la casa, etc. Para predecir el precio de una nueva casa, el algoritmo KNN identificaría las k casas en los datos de entrenamiento que son más "similares" a la nueva casa en términos de estas características. Luego calcularía la media (o mediana) de los precios de estas k casas más cercanas y usaría este valor como la predicción del precio de la nueva casa.

## Ventajas y desventajas de KNN en regresión

Al igual que en la clasificación, una de las ventajas de KNN en regresión es su simplicidad y su capacidad para manejar cualquier tipo de relación entre las características y la variable objetivo, ya que no hace suposiciones paramétricas sobre la forma de esta relación.

Sin embargo, KNN también tiene algunas limitaciones en el contexto de la regresión. En primer lugar, puede ser sensible a la presencia de valores atípicos, que pueden influir de manera desproporcionada en la media o la mediana de los k vecinos más cercanos. Además, como KNN depende del cálculo de distancias, puede ser sensible a la escala de las características y generalmente requiere un escalado previo de los datos para funcionar bien. Finalmente, al igual que en la clasificación, elegir el valor óptimo de k puede ser un desafío y puede requerir un ajuste fino basado en la validación cruzada u otros métodos.

## Conclusión

En resumen, aunque KNN es más conocido por su uso en problemas de clasificación, también puede ser una herramienta útil para los problemas de regresión. A pesar de su simplicidad, puede manejar relaciones complejas y no lineales entre las características y la variable objetivo. Sin embargo, su rendimiento puede verse afectado por la presencia de valores atípicos y la escala de las características, y la elección del número de vecinos puede requerir un ajuste fino. Como siempre, la eficacia de KNN en un problema de regresión dado dependerá de las características particulares del conjunto de datos y del problema en cuestión.
