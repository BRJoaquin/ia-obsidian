  
La descomposición del sesgo-varianza es una forma de entender las fuentes del error en los modelos de aprendizaje automático y cómo las diferentes complejidades del modelo pueden afectar este error. La idea es que el error esperado generalizable de un modelo puede ser descompuesto en tres términos: sesgo, varianza y error irreducible.

1.  **Sesgo (Bias)**: Este es el error debido a las suposiciones erróneas en el algoritmo de aprendizaje. Un alto sesgo puede causar que el algoritmo pierda relaciones relevantes entre las características de entrada y la variable objetivo (underfitting). Por lo general, los modelos sencillos, como la regresión lineal, tienen un alto sesgo.

2.  **Varianza (Variance)**: Este es el error debido a la sensibilidad a las fluctuaciones en el conjunto de entrenamiento. Un alto valor de la varianza puede causar overfitting, que es un modelo que aprende demasiado bien el ruido del conjunto de datos de entrenamiento y funciona mal en datos nuevos. Los modelos complejos, como las redes neuronales profundas o los árboles de decisión, tienden a tener una alta varianza.

3.  **Error irreducible (Irreducible Error)**: Este es el error debido al ruido en los datos. Es independiente del algoritmo de aprendizaje y siempre estará presente sin importar el algoritmo utilizado.


La descomposición del error esperado, $E[(Y - f(X))^2]$, en términos de sesgo y varianza para un estimador de una función real $f(X)$ es:
$$
E[(Y - f(X))^2] = (E[f(X)] - f(X))^2 + E[(f(X) - E[f(X)])^2] + σ^2
$$
Donde:

-   $(E[f(X)] - f(X))^2$ es el cuadrado del sesgo.
-   $E[(f(X) - E[f(X)])^2]$ es la varianza.
-   $σ^2$ es el error irreducible.

En la práctica, el objetivo de cualquier buen modelo de aprendizaje automático es encontrar el equilibrio correcto entre el sesgo y la varianza, para minimizar el error total. Esto a menudo se conoce como el compromiso sesgo-varianza (bias-variance trade-off).

![[Pasted image 20230518213202.png]]


# Ejemplo practico

Claro, considera el problema de predecir la altura de una persona basada en su edad.

1.  Decides comenzar con un modelo muy sencillo, una regresión lineal. Después de entrenar tu modelo, te das cuenta de que no se ajusta bien a tus datos de entrenamiento y se desempeña mal en los datos de prueba. Esto se debe a que la relación entre la edad y la altura no es exactamente lineal, especialmente durante las etapas de crecimiento acelerado en la infancia y la adolescencia. En este caso, tu modelo tiene un sesgo alto porque hizo suposiciones muy simplificadas (lineales) sobre la relación entre la edad y la altura.

2.  Para mejorar tu modelo, decides aumentar su complejidad. Ahora utilizas un polinomio de grado 20 para capturar la relación entre la edad y la altura. Este modelo se ajusta casi perfectamente a tus datos de entrenamiento, pero cuando intentas usarlo en tus datos de prueba, se desempeña muy mal. En este caso, tu modelo tiene una alta varianza. Ha aprendido las peculiaridades y el ruido de tus datos de entrenamiento tan bien que no puede generalizar a nuevos datos.

3.  Finalmente, decides utilizar un polinomio de grado 3. Este modelo no se ajusta tan perfectamente a los datos de entrenamiento como el polinomio de grado 20, pero se desempeña mucho mejor en los datos de prueba. Has encontrado un buen equilibrio entre el sesgo y la varianza.

Este ejemplo ilustra el trade-off entre sesgo y varianza. Los modelos demasiado simples pueden tener un alto sesgo, mientras que los modelos demasiado complejos pueden tener una alta varianza. La clave está en encontrar un equilibrio entre ambos.