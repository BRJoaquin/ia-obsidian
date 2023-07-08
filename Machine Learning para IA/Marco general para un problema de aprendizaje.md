El marco general para un problema de aprendizaje en Machine Learning consta de varios componentes clave:

# Ingredientes de un Problema de Aprendizaje

1. **Espacios de Atributos ($X$)**: Este es el conjunto de todas las posibles entradas que podría tomar nuestro modelo. En un problema de clasificación de imágenes, por ejemplo, el espacio de atributos podría ser el conjunto de todas las posibles imágenes de cierto tamaño y color.

2. **Espacio de Etiquetas ($Y$)**: Este es el conjunto de todas las posibles salidas o etiquetas que nuestro modelo podría predecir. En un problema de clasificación binaria, el espacio de etiquetas es generalmente $\{0, 1\}$.

3. **Espacio de Predicciones ($U$)**: Este es el conjunto de todas las posibles predicciones que nuestro modelo podría hacer. En muchos casos, $U$ y $Y$ son el mismo conjunto, pero en otros, como en la clasificación probabilística, pueden ser diferentes.

4. **Clase de Distribuciones de Probabilidad ($P$)**: Esta es la colección de todas las posibles distribuciones de probabilidad que podrían generar nuestros datos. Cada distribución en $P$ define una forma diferente en que se podrían muestrear los datos.

5. **Clase de Funciones ($H$)**: Este es el conjunto de todas las posibles hipótesis que nuestro modelo podría adoptar. Cada hipótesis es una función diferente de $X$ a $U$. Este conjunto $H$ representa nuestro [[Sesgo inductivo]].

6. **Función de Pérdida ($\ell$)**: Esta es una función que toma una etiqueta y una predicción y devuelve un número real que cuantifica cuánto "cuesta" predecir la predicción cuando la verdadera etiqueta es la etiqueta. vease [[Función de pérdida]]

# Proceso de Aprendizaje

El proceso de aprendizaje se lleva a cabo de la siguiente manera:

1. Se genera una muestra independiente e idénticamente distribuida (i.i.d.) $S$ de la distribución de probabilidad que estamos tratando de modelar.

2. Denotamos $\text{Muestras}(N, D)$ el conjunto de posibles muestras de tamaño $N$.

3. Un algoritmo de aprendizaje es una secuencia $A = \{A_N\}_{N=1}^{\infty}$ de asignaciones. Cada $A_N$ toma una muestra de tamaño $N$ y produce una hipótesis $h \in H$. El objetivo es que esta hipótesis $h$ aproxime bien la función desconocida que estamos tratando de aprender.
