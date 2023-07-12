

En machine learning, entender los conceptos de sesgo y varianza es fundamental para desarrollar modelos efectivos y para diagnosticar problemas como el sobreajuste y el subajuste. Estos dos conceptos representan dos tipos de errores que puede cometer un algoritmo de aprendizaje automático.

# Definiciones básicas

**Sesgo (Bias)**: El sesgo de un modelo es la diferencia entre la predicción esperada de nuestro modelo y los valores verdaderos que estamos tratando de predecir. Los modelos con alto sesgo simplifican demasiado los datos, lo que lleva a un error de predicción alto en el entrenamiento y en los datos de prueba. A este fenómeno se le conoce como subajuste.

**Varianza**: La varianza es la variabilidad de las predicciones del modelo para un dato dado. Los modelos con alta varianza prestan mucha atención a los datos de entrenamiento y no generalizan bien los datos no vistos. A este fenómeno se le conoce como sobreajuste.

![[Pasted image 20230708124644.png]]

# Sesgo inductivo y dependencia con el dataset

El [[Sesgo inductivo]] se refiere a las suposiciones hechas por el modelo para hacer las predicciones. Cada algoritmo de aprendizaje automático tiene un sesgo inductivo, que es la colección de suposiciones (prejuicios) que el algoritmo hace para predecir la salida dado los datos de entrada. 

La dependencia del sesgo inductivo con el dataset viene de que si el sesgo inductivo del modelo se alinea bien con la realidad de los datos, entonces el modelo será capaz de generalizar bien y tendrá un error bajo. Pero si las suposiciones del modelo no se alinean con los datos, entonces el modelo tendrá un error alto, ya que no podrá generalizar bien los datos.

![[Pasted image 20230708124906.png]]

# Error esperado

![[Pasted image 20230712105937.png]]

# Descomposición del error

![[Pasted image 20230712105521.png]]

![[Pasted image 20230712105504.png]]



# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/r25dWiyDPQA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/R13lpnXVtXo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/IvHZ4-yd5is" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
