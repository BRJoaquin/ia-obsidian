
El **Aprendizaje de Conceptos** es una estrategia de aprendizaje en Machine Learning que implica la inferencia de una función booleana a partir de ejemplos de entrenamiento. Los ejemplos están etiquetados como positivos o negativos, y el objetivo es aprender un "concepto" que pueda clasificar correctamente nuevos ejemplos.

# Datos (S)

Los **datos** en el aprendizaje de conceptos, a menudo denotados por $S$, son una colección de ejemplos de entrenamiento. Cada ejemplo es una instancia que consta de un conjunto de características y una etiqueta. Las etiquetas suelen ser binarias, correspondientes a 'positivo' (el ejemplo pertenece al concepto) o 'negativo' (el ejemplo no pertenece al concepto).

Por ejemplo, si nuestro concepto es "es un perro", entonces nuestras instancias serían imágenes de animales, y las etiquetas serían 'positivo' para las imágenes de perros y 'negativo' para las imágenes de cualquier otro animal.

# Distribución (D)

La **distribución** en el aprendizaje de conceptos, denotada por $D$, se refiere a la distribución probabilística subyacente de la cual se extraen los ejemplos de entrenamiento. En la práctica, rara vez conocemos $D$ exactamente, pero asumimos que nuestros ejemplos de entrenamiento son muestras representativas de esta distribución.

# Concepto (c)

Un **concepto** en el aprendizaje de conceptos es una función booleana que queremos aprender. Esta función toma una instancia como entrada y devuelve 'verdadero' (o 'positivo') si la instancia pertenece al concepto, y 'falso' (o 'negativo') de lo contrario. En otras palabras, un concepto es la regla de clasificación que estamos tratando de inferir a partir de nuestros ejemplos de entrenamiento.

Retomando el ejemplo anterior, el concepto "es un perro" sería la función que podemos aplicar a una nueva imagen para determinar si es o no una imagen de un perro. 

![[Pasted image 20230707115036.png]]


# Esto es una prueba de GPT

