![[Pasted image 20230712194440.png]]
![Directed By Robert Credits GIF - Directed By Robert Credits ...](https://media.tenor.com/wBbAVcEb3hcAAAAC/directed-by-robert-credits.gif)

**Random Forest** es un algoritmo de aprendizaje supervisado de conjunto que se utiliza tanto para tareas de clasificación como de regresión. Se basa en el concepto de [[Bagging]] introducido por Leo Breiman en 1996, y la idea esencial es combinar la salida de varios árboles de decisión independientes para obtener una predicción más precisa y robusta. 

Random Forest se considera uno de los algoritmos de machine learning más efectivos y versátiles debido a su capacidad para manejar grandes volúmenes de datos con numerosas variables, su tolerancia al ruido y los datos faltantes, y su facilidad de interpretación.

En términos generales, un Random Forest se construye de la siguiente manera:

1. **Bootstrap de los datos**: Para cada árbol en el bosque, se genera una muestra bootstrap del conjunto de datos de entrenamiento, es decir, una muestra de la misma longitud que el conjunto de datos original, obtenida mediante muestreo con reemplazo. 
2. **Construcción del árbol de decisión**: A partir de la muestra bootstrap, se construye un árbol de decisión. Sin embargo, a diferencia de un árbol de decisión normal, en **cada nodo** del árbol, en lugar de seleccionar la mejor división entre todas las variables, **primero se selecciona un subconjunto aleatorio de variables y luego se selecciona la mejor división entre esas variables**. Esto introduce una mayor diversidad entre los árboles y **ayuda a reducir la correlación entre ellos, mejorando así el rendimiento del modelo en general**.
   
   > El numero de features varia pero en general es $\sqrt{\text{nro features}}$ o $\log_2{\text{nro features}} + 1$

![[Pasted image 20230713091901.png]]

3. **Predicción**: Para hacer una predicción, cada árbol en el bosque hace su propia predicción y la predicción final se obtiene combinando las predicciones de todos los árboles. En el caso de la clasificación, la predicción final suele ser la clase que obtiene más votos (voto mayoritario). En el caso de la regresión, la predicción final es normalmente la media de las predicciones de los árboles.

![[Pasted image 20230708193358.png]]

Las características anteriores hacen de Random Forest un modelo muy robusto y flexible. En particular, tiene las siguientes ventajas:

- **Robustez frente al sobreajuste**: **Gracias al muestreo bootstrap y la selección aleatoria de variables**, los árboles de Random Forest tienden a ser diversos y **no correlacionados**, lo que reduce el riesgo de sobreajuste.

- **Manejo de datos faltantes y categóricos**: Random Forest puede manejar variables categóricas y puede ser robusto frente a datos faltantes.

- **Importancia de las variables**: Random Forest proporciona una medida de la importancia de las variables al calcular el aumento promedio en el error de predicción cuando los valores de una variable son permutados aleatoriamente. Esta es una característica muy útil para la selección de variables y la interpretación del modelo.
  
- **Estimación del error de generalización**: Random Forest proporciona una estimación "**gratuita**" del error de generalización utilizando las observaciones OOB (Out-of-bag), es decir, aquellas que no fueron seleccionadas durante el muestreo bootstrap.

# Variable Importance

Los Random Forest determinan la importancia de las variables mediante el cálculo de la disminución promedio en la impureza de los nodos que se obtiene al dividir sobre esa variable, es decir, la ganancia de información promedio. Este valor se denomina "Importancia de la Variable" o "Feature Importance".

![[Pasted image 20230708193905.png]]

En el caso de la clasificación, la impureza de un nodo se mide generalmente mediante el índice Gini o la entropía, mientras que en el caso de la regresión, se utiliza el error cuadrático medio.

Para calcular la importancia de una variable, el algoritmo de Random Forest sigue los siguientes pasos:

1. Para cada árbol en el bosque, calcula la disminución en la impureza de los nodos cada vez que la variable es utilizada para dividir.
2. Promedia estas disminuciones en impureza sobre todos los árboles en el bosque.

Esto proporciona una medida de cuánto contribuye cada variable a mejorar las divisiones del árbol y, por lo tanto, la precisión de las predicciones. Las variables que tienen una gran importancia son aquellas que contribuyen en gran medida a mejorar las divisiones del árbol, y por lo tanto son las que tienen más capacidad para predecir la variable objetivo.

En resumen, Random Forest determina la importancia de las variables calculando cuánto contribuyen a mejorar las divisiones del árbol y, por lo tanto, la precisión de las predicciones.

# Por que quita las features en cada nodo?

El algoritmo Random Forest selecciona características (o "features") en cada nodo para **aumentar la diversidad de los árboles que conforman el bosque**, y por ende, mejorar la capacidad de generalización del modelo.

En Random Forest, se implementa lo que se conoce como muestreo con reemplazo y selección aleatoria de características. Es decir, para cada árbol que se construye, no sólo se utiliza un subconjunto aleatorio de las observaciones, sino también un subconjunto aleatorio de las características.

Este proceso se lleva a cabo por varias razones:

1. **Reducción de la correlación entre los árboles**: Si no se seleccionaran diferentes características para cada nodo, cada árbol en el bosque podría terminar pareciéndose demasiado a los demás, especialmente si hay unas pocas características muy predictivas. Esto resultaría en árboles altamente correlacionados, lo que limitaría la eficacia del ensemble al promediar las predicciones.

2. **Mayor diversidad de los árboles**: Al seleccionar diferentes características en cada nodo, cada árbol tiene la oportunidad de "aprender" de diferentes aspectos de los datos, lo que conduce a un bosque de árboles más diverso y robusto.

3. **Evitar el sobreajuste**: Al seleccionar solo un subconjunto de características en cada nodo, el algoritmo se vuelve más robusto a los errores de modelado debido al sobreajuste, que es cuando un modelo se ajusta demasiado a los datos de entrenamiento y pierde la capacidad de generalizar a datos no vistos.


Si Random Forest no seleccionara características en cada nodo, básicamente se convertiría en un conjunto de árboles de decisión completos sin regularización, lo que probablemente llevaría a un sobreajuste, ya que cada árbol podría seguir muy de cerca los datos de entrenamiento. Además, perdería su capacidad de diversificar los árboles y evitar la correlación entre ellos. En última instancia, esto reduciría el poder predictivo del modelo en datos no vistos.

# Comentarios

A pesar de sus numerosas ventajas, Random Forest también tiene algunas limitaciones. En particular, a pesar de ser relativamente rápido de entrenar, **puede ser lento para hacer predicciones, especialmente si el número de árboles es muy alto**. Además, aunque Random Forest puede manejar una gran cantidad de variables, **puede ser menos efectivo si la mayoría de las variables son irrelevantes** para la predicción, ya que esto puede dificultar la selección de las variables importantes en cada nodo.

# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/r5C3TUIw6Zk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>