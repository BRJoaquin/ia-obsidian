El riesgo empírico en [[Machine Learning]] (aprendizaje automático) **se refiere a la medida del error que un modelo comete al realizar predicciones en base a un conjunto de datos de entrenamiento específico.** Es una forma de evaluar qué tan bien un [[Modelo (Hipotesis)]] ha aprendido de los datos de entrenamiento y, en última instancia, cuál es su capacidad para generalizar a datos no vistos.

El riesgo empírico es una [[Función de pérdida]] promediada sobre todos los ejemplos en el conjunto de datos de entrenamiento. La función de pérdida cuantifica la discrepancia entre las predicciones del modelo y las etiquetas reales. **Un riesgo empírico bajo indica que el modelo ha aprendido bien de los datos de entrenamiento**, mientras que un riesgo empírico alto sugiere que el modelo no se ajusta bien a los datos.

Sin embargo, **es importante tener en cuenta que un riesgo empírico bajo no garantiza un buen rendimiento en datos no vistos**. Un modelo puede sobreajustarse ([[Sobreajuste (Overfitting)]]) a los datos de entrenamiento, lo que significa que ha aprendido patrones específicos del conjunto de entrenamiento que no se aplican a datos no vistos. En este caso, el modelo tendrá un mal rendimiento en el conjunto de datos de prueba, aunque tenga un riesgo empírico bajo.

# Ejemplo

Supongamos que estamos trabajando en un problema de clasificación binaria para predecir si un correo electrónico es spam o no spam. Tenemos un conjunto de datos de 1000 correos electrónicos etiquetados, de los cuales 800 se utilizan para entrenamiento y 200 para prueba.

Entrenamos un modelo de machine learning utilizando el conjunto de entrenamiento, y calculamos el riesgo empírico utilizando una función de pérdida, como la pérdida logarítmica (log loss). Supongamos que el modelo tiene un riesgo empírico de 0.2, lo que indica que, en promedio, comete errores en el 20% de los ejemplos de entrenamiento.

Para evaluar la capacidad de generalización del modelo, lo probamos en el conjunto de datos de prueba y calculamos el error de prueba. Si el error de prueba es cercano al riesgo empírico, esto indica que el modelo generaliza bien a datos no vistos. Sin embargo, si el error de prueba es significativamente más alto que el riesgo empírico, esto sugiere que el modelo puede estar sobreajustado y no generaliza bien a datos no vistos.