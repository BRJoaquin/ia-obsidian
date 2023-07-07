En estadística y [[Machine Learning]], los modelos se pueden clasificar en dos categorías amplias: paramétricos y no paramétricos. La distinción entre estos dos tipos de modelos tiene que ver con la cantidad y la naturaleza de las suposiciones que se hacen acerca de la distribución de los datos.

# Modelos paramétricos

Los modelos paramétricos son aquellos que **asumen una forma específica y fija para la distribución de los datos**. Por ejemplo, podríamos asumir que los datos se distribuyen normalmente, y luego utilizar la media y la varianza (los parámetros de la distribución normal) para describir completamente los datos. El número de parámetros es fijo y no cambia con el tamaño del conjunto de datos.

Un ejemplo de modelo paramétrico es la [[Regresión lineal]], donde se asume que la relación entre las variables independientes y la variable dependiente es lineal y se describen con un número fijo de parámetros (los coeficientes de la ecuación de regresión lineal). Otro ejemplo es la [[Regresión logística]], utilizada para predecir una variable binaria. 

La ventaja de los modelos paramétricos es que son más simples y más rápidos para calcular que los modelos no paramétricos, ya que se necesita menos datos para estimar los parámetros. Además, proporcionan un marco teórico sólido que puede facilitar la interpretación de los resultados.

Por otro lado, **la principal desventaja de los modelos paramétricos es que las suposiciones sobre la distribución de los datos pueden ser incorrectas**, lo que puede llevar a predicciones y conclusiones inexactas. **En la práctica, rara vez conocemos la verdadera distribución de los datos, por lo que estas suposiciones son a menudo violadas**.

# Modelos no paramétricos

A diferencia de los modelos paramétricos, los modelos no paramétricos no hacen suposiciones fuertes sobre la distribución de los datos. En lugar de ello, intentan aprender la distribución subyacente de los datos a partir de los datos en sí. Como tal, el número de parámetros en un modelo no paramétrico puede crecer con el tamaño del conjunto de datos.

Un ejemplo de un modelo no paramétrico es el algoritmo de los [[KNN (K vecinos mas cercanos)]]. KNN clasifica una observación basándose en las etiquetas de las k observaciones más cercanas en el conjunto de entrenamiento, sin asumir una forma específica para la distribución de los datos. Otro ejemplo es el [[Árbol de decisión]], que divide el espacio de características en regiones y asigna una predicción a cada región.

La principal ventaja de los modelos no paramétricos es su flexibilidad. Como no hacen suposiciones fuertes sobre la distribución de los datos, pueden adaptarse a una amplia variedad de formas de distribución, incluyendo las que tienen relaciones no lineales y de alta dimensión.

Por otro lado, **los modelos no paramétricos pueden ser más complejos y computacionalmente intensivos que los modelos paramétricos. También pueden requerir más datos para hacer predicciones precisas, ya que no se benefician de suposiciones a priori sobre la distribución de los datos.**

## Conclusión

En resumen, la elección entre modelos paramétricos y no paramétricos depende en gran medida de la naturaleza de los datos y del problema específico que se esté tratando de resolver. Los modelos paramétricos pueden ser una buena opción **cuando se tienen suposiciones razonables sobre la distribución de los datos y se dispone de datos limitados**. **Los modelos no paramétricos pueden ser más adecuados cuando se dispone de mucha información y no se quieren hacer suposiciones fuertes sobre la distribución de los datos**.
