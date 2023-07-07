El riesgo empírico en [[Machine Learning]] (aprendizaje automático) **se refiere a la medida del error que un modelo comete al realizar predicciones en base a un conjunto de datos de entrenamiento específico.** Es una forma de evaluar qué tan bien un [[Modelo (Hipotesis)]] ha aprendido de los datos de entrenamiento y, en última instancia, cuál es su capacidad para generalizar a datos no vistos. En términos formales, es la media del error sobre todas las instancias en el conjunto de datos de entrenamiento. Para un modelo de hipótesis h y una función de pérdida L, el riesgo empírico R(h) se define como:

$$\Large R(h) = \frac{1}{N}\sum_{i=1}^{N}L(h(x_i), y_i)$$

Donde:

- $N$ es el número de instancias en el conjunto de datos de entrenamiento.
- $L(h(x_i), y_i)$ es la pérdida incurrida al predecir $h(x_i)$ cuando el verdadero valor es $y_i$.
- $(x_i, y_i)$ es la i-ésima instancia del conjunto de entrenamiento.

![[Pasted image 20230707113140.png]]

El riesgo empírico es una [[Función de pérdida]] promediada sobre todos los ejemplos en el conjunto de datos de entrenamiento. La función de pérdida cuantifica la discrepancia entre las predicciones del modelo y las etiquetas reales. **Un riesgo empírico bajo indica que el modelo ha aprendido bien de los datos de entrenamiento**, mientras que un riesgo empírico alto sugiere que el modelo no se ajusta bien a los datos.

Sin embargo, **es importante tener en cuenta que un riesgo empírico bajo no garantiza un buen rendimiento en datos no vistos**. Un modelo puede sobreajustarse ([[Sobreajuste (Overfitting)]]) a los datos de entrenamiento, lo que significa que ha aprendido patrones específicos del conjunto de entrenamiento que no se aplican a datos no vistos. En este caso, el modelo tendrá un mal rendimiento en el conjunto de datos de prueba, aunque tenga un riesgo empírico bajo.

En Machine Learning, el **Riesgo Empírico** y el **Error Empírico** se utilizan para cuantificar el rendimiento de un modelo en los datos de entrenamiento. Aunque se utilizan de manera intercambiable en algunos contextos, técnicamente se refieren a conceptos diferentes.

# Ejemplo

Supongamos que estamos trabajando en un problema de clasificación binaria para predecir si un correo electrónico es spam o no spam. Tenemos un conjunto de datos de 1000 correos electrónicos etiquetados, de los cuales 800 se utilizan para entrenamiento y 200 para prueba.

Entrenamos un modelo de machine learning utilizando el conjunto de entrenamiento, y calculamos el riesgo empírico utilizando una función de pérdida, como la pérdida logarítmica (log loss). Supongamos que el modelo tiene un riesgo empírico de 0.2, lo que indica que, en promedio, comete errores en el 20% de los ejemplos de entrenamiento.

Para evaluar la capacidad de generalización del modelo, lo probamos en el conjunto de datos de prueba y calculamos el error de prueba. Si el error de prueba es cercano al riesgo empírico, esto indica que el modelo generaliza bien a datos no vistos. Sin embargo, si el error de prueba es significativamente más alto que el riesgo empírico, esto sugiere que el modelo puede estar sobreajustado y no generaliza bien a datos no vistos.

# Minimización del Riesgo Empírico (ERM) en Machine Learning

La **Minimización del Riesgo Empírico** (ERM, por sus siglas en inglés) es un principio en el aprendizaje de máquinas que sostiene que la hipótesis (modelo) que minimiza la pérdida en el conjunto de entrenamiento es la mejor elección. En otras palabras, ERM se refiere a encontrar la hipótesis que tiene el menor riesgo empírico (o error promedio) en el conjunto de entrenamiento.

Formalmente, si tenemos un conjunto de hipótesis $\mathcal{H}$ y una función de pérdida $L$, el objetivo del ERM es encontrar la hipótesis $h \in \mathcal{H}$ que minimiza la pérdida promedio en el conjunto de entrenamiento. Esto se puede escribir como:

$$h_{ERM} = \arg\min_{h\in\mathcal{H}} \frac{1}{N}\sum_{i=1}^{N}L(h(x_i), y_i)$$

Donde:

- $N$ es el número de instancias en el conjunto de datos de entrenamiento.
- $L(h(x_i), y_i)$ es la pérdida incurrida al predecir $h(x_i)$ cuando el verdadero valor es $y_i$.
- $(x_i, y_i)$ es la i-ésima instancia del conjunto de entrenamiento.
![[Pasted image 20230707113725.png]]

El objetivo del aprendizaje de máquinas es encontrar una hipótesis (o modelo) que tenga un buen rendimiento no sólo en los datos de entrenamiento, sino también en los nuevos datos. Aunque el ERM proporciona un método para encontrar un modelo que se ajuste bien a los datos de entrenamiento, no garantiza que el modelo vaya a generalizar bien a nuevos datos. Por lo tanto, a menudo se utilizan técnicas como la regularización y la validación cruzada para ayudar a garantizar una buena generalización.
