# Regresión Lineal (Simple, Polinómica, Multivariada)

_Idea General_: La regresión lineal es un algoritmo de aprendizaje supervisado que se utiliza en ML y estadísticas para predecir una variable dependiente continua a partir de una o más variables independientes. Simple utiliza una variable, multivariada utiliza múltiples y polinómica modela relaciones no lineales a través de potencias de las variables independientes.

_Buenos Para_: Ideal para relaciones lineales o no lineales (polinómica), análisis de tendencias y pronósticos.

_Ventajas_: Es **simple**, **interpretable** y requiere poca preparación de datos.

_Desventajas_: Puede ser limitado debido a la suposición de linealidad y puede ser **afectado por outliers**.

_No Funcionan Bien_: No funciona bien cuando las relaciones son altamente no lineales o **cuando los datos tienen muchas características irrelevantes**.

ver mas en: [[Regresión lineal]]

# Regresión Logística

_Idea General_: La regresión logística es un algoritmo de aprendizaje supervisado que se utiliza para clasificación binaria. Predice la probabilidad de que una instancia pertenezca a una clase específica.

_Buenos Para_: Ideal para clasificación binaria, especialmente en casos de **predicción de probabilidad**.

_Ventajas_: Produce probabilidades, funciona con características categóricas y numéricas.

_Desventajas_: **Puede tener problemas con variables correlacionadas y no puede manejar relaciones no lineales sin transformación**.

_No Funcionan Bien_: No funciona bien con límites de decisión complejos o en **clasificación multiclase sin adaptaciones**.

# KNN (K-Nearest Neighbors)

_Idea General_: KNN es un algoritmo de aprendizaje **greedy** y [[Modelo parametrico#Modelos no paramétricos|no parametrico]] que clasifica una instancia basándose en la mayoría de las clases de sus "K" vecinos más cercanos.

_Buenos Para_: Ideal para problemas de clasificación y regresión con límites de decisión que no sean lineales.

_Solucionar Desventaja_: KNN puede manejar límites de decisión que no son lineales, lo que puede ser un desafío para algoritmos como la regresión lineal y logística.

_Ventajas_: No se requiere entrenamiento, maneja bien relaciones no lineales.

_Desventajas_: **Es sensible a la elección de "K"** y a las características irrelevantes o correlacionadas.

_No Funcionan Bien_: No funciona bien en espacios de alta dimensión (**maldición de la dimensionalidad**) y con grandes conjuntos de datos debido a **la necesidad de calcular distancias**.

# Árboles de Decisión

_Idea General_: Los árboles de decisión son algoritmos de aprendizaje supervisado que se utilizan para clasificación y regresión. Se representan como estructuras de árbol donde cada nodo es una prueba de una característica y cada hoja es una predicción de la variable objetivo.

_Buenos Para_: Son buenos para problemas de clasificación y regresión con características categóricas y numéricas.

_Ventajas_: **Son interpretables**, no requieren mucho preprocesamiento de datos.

_Desventajas_: **Pueden sobreajustar fácilmente y son sensibles a los cambios en los datos**.

_No Funcionan Bien_: No funcionan bien con límites de decisión muy complejos y con datos de alta dimensionalidad.

# Ensamble (Bagging, Boosting, Stacking)

_Idea General_: Los métodos de ensamble combinan múltiples modelos de aprendizaje para mejorar las predicciones. Bagging (Bootstrap Aggregating) entrena modelos independientes en subconjuntos aleatorios de los datos y agrega sus predicciones. Boosting entrena modelos secuencialmente, cada uno tratando de corregir los errores del anterior. Stacking entrena un modelo (meta-modelo) para hacer la predicción final basándose en las predicciones de todos los modelos base.

_Buenos Para_: Son buenos para reducir la varianza (bagging), reducir el sesgo (boosting), y aprovechar la fuerza de varios tipos de modelos (stacking).

_Ventajas y Desventajas_: Pueden mejorar significativamente el rendimiento, pero a costa de la complejidad, el tiempo de entrenamiento y la dificultad de interpretación.

_No Funcionan Bien_: No funcionan bien si los modelos base son muy débiles o muy complejos, o si los datos son demasiado escasos para el entrenamiento de varios modelos.

## Bagging 

_Idea General_: Bagging, o Bootstrap Aggregating, es un método de ensamblado que entrena múltiples modelos (normalmente árboles de decisión) en subconjuntos aleatorios de los datos originales y luego agrega sus predicciones, normalmente por votación o promedio.

_Buenos Para_: Bagging es excelente para reducir la varianza en los modelos que tienden a sobreajustar, como los árboles de decisión.

_Ventajas y Desventajas_: Bagging puede mejorar significativamente la estabilidad y la precisión, pero a costa de aumentar la complejidad del modelo y el tiempo de cálculo (pero puede correr cada clasificador en paralelo, no es secuencial).

_No Funcionan Bien_: Bagging puede no ser efectivo si los modelos base son demasiado simples o si los datos son demasiado ruidosos.

## Boosting

_Idea General_: Boosting es una técnica de ensamblado que entrena modelos de manera secuencial, donde cada modelo siguiente trata de corregir los errores del anterior. Los modelos se ponderan en función de su precisión.

_Buenos Para_: Boosting es ideal para reducir tanto el sesgo como la varianza, mejorando la precisión de los modelos de aprendizaje débiles.

_Solucionar_: Boosting puede solucionar el problema del subajuste (underfitting) y mejorar la precisión de los modelos de aprendizaje débiles.

_Ventajas y Desventajas_: Boosting puede mejorar significativamente la precisión, pero es **propenso al sobreajuste si los datos son ruidosos** y puede ser computacionalmente costoso.

_No Funcionan Bien_: Boosting puede no funcionar bien con datos ruidosos y outliers, ya que intenta ajustarse a cada punto de datos.

## Stacking

_Idea General_: Stacking es un método de ensamblado que combina varios modelos de aprendizaje para obtener mejores predicciones. Las predicciones de los modelos base se utilizan como entrada para un meta-model que hace la predicción final.

_Buenos Para_: Stacking es útil cuando se quiere aprovechar la fuerza de varios modelos de aprendizaje diferentes.

_Ventajas y Desventajas_: Stacking puede mejorar la precisión, pero aumenta la complejidad del modelo y puede ser computacionalmente costoso.

_No Funcionan Bien_: **Stacking puede no mejorar el rendimiento si los modelos base ya son muy precisos o si están fuertemente correlacionados**.