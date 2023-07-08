![[Pasted image 20230708134902.png]]


En el aprendizaje automático, la **selección de modelos**, también conocida como selección del sesgo inductivo, es el proceso de elegir entre diferentes modelos o algoritmos para encontrar el que mejor se adapta a los datos disponibles.

El sesgo inductivo de un algoritmo de aprendizaje es su conjunto de suposiciones sobre la tarea de aprendizaje. Cada algoritmo de aprendizaje automático hace diferentes suposiciones sobre los datos y por lo tanto tiene un sesgo inductivo diferente. Este sesgo es necesario para que un algoritmo haga predicciones en base a los datos de entrada.

La selección del sesgo inductivo es un paso crucial en la construcción de un modelo de aprendizaje automático, ya que el sesgo inductivo del algoritmo determina cómo se generalizará a partir de los datos de entrenamiento a nuevos datos. Un sesgo inductivo que es demasiado fuerte puede resultar en un modelo que no se adapta bien a los datos (subajuste), mientras que un sesgo inductivo que es demasiado débil puede resultar en un modelo que se ajusta demasiado a los datos de entrenamiento y no se generaliza bien a nuevos datos (sobreajuste).

Hay varias formas de realizar la selección de modelos, que van desde métodos de búsqueda exhaustiva que evalúan todas las combinaciones posibles de parámetros hasta métodos más eficientes y sofisticados como la validación cruzada y los criterios de información.

# Selección de Modelos con Holdout (Entrenamiento + Validación + Prueba)

El método **Holdout** es un enfoque común para la selección de modelos y la validación del modelo en aprendizaje automático. En este enfoque, el conjunto de datos se divide en tres conjuntos: conjunto de entrenamiento, conjunto de validación y conjunto de prueba.

- **Conjunto de Entrenamiento**: Este conjunto se utiliza para entrenar el modelo. El modelo aprende de los datos de este conjunto.

- **Conjunto de Validación**: Este conjunto se utiliza para afinar el modelo y seleccionar el mejor modelo durante la fase de entrenamiento. No se utiliza para entrenar el modelo inicialmente, sino que se utiliza para probar el rendimiento del modelo en diferentes configuraciones (como diferentes hiperparámetros o diferentes tipos de modelos). En la selección de modelos, se elige el modelo que tiene el mejor rendimiento en el conjunto de validación.

- **Conjunto de Prueba**: Este conjunto se mantiene completamente separado y sólo se utiliza al final del proceso de aprendizaje, una vez que el modelo ha sido seleccionado y completamente entrenado. Proporciona una medida de cómo el modelo seleccionado se desempeñará en datos no vistos anteriormente.

Por lo tanto, el proceso completo se ve así:

1. Entrenar varios modelos diferentes (o el mismo modelo con diferentes configuraciones) en el conjunto de entrenamiento.

2. Evaluar cada modelo en el conjunto de validación.

3. Seleccionar el modelo que mejor se desempeña en el conjunto de validación.

4. Finalmente, probar el modelo seleccionado en el conjunto de prueba para obtener una estimación imparcial del rendimiento del modelo en datos no vistos.

La principal ventaja de este método es su simplicidad y eficacia. Sin embargo, tiene la desventaja de que la evaluación del rendimiento del modelo puede variar mucho dependiendo de cómo se divida el conjunto de datos en los tres conjuntos. Esto se debe a que cada división proporciona una muestra diferente de los datos. La validación cruzada es una alternativa a la técnica de Holdout que aborda este problema.

<iframe width="560" height="315" src="https://www.youtube.com/embed/KKErl_UtF2M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Selección de Modelos con Repeated Holdout

El método **Repeated Holdout** es una mejora del método Holdout que se mencionó anteriormente. En lugar de dividir el conjunto de datos sólo una vez en entrenamiento, validación y prueba, el método Repeated Holdout repite este proceso varias veces con diferentes divisiones aleatorias de los datos. Este método busca abordar el problema de la variabilidad en las divisiones de datos, una limitación importante del método Holdout.

En cada iteración del proceso:

1. Se divide aleatoriamente el conjunto de datos en un conjunto de entrenamiento y un conjunto de validación/prueba.

2. Se entrena el modelo en el conjunto de entrenamiento y se valida en el conjunto de validación.

3. Se registra el rendimiento del modelo en el conjunto de validación.

4. Se repite el proceso con una nueva división aleatoria de los datos.

Finalmente, el rendimiento promedio de las múltiples ejecuciones proporciona una medida más robusta del rendimiento del modelo. Además, esto permite que cada dato tenga la oportunidad de ser parte del conjunto de validación y del conjunto de entrenamiento, lo que mejora la estimación del error de generalización del modelo.

Una vez completado el proceso de repetición, se selecciona el modelo con el mejor rendimiento promedio en el conjunto de validación a través de todas las iteraciones. Ese modelo finalmente se prueba en el conjunto de prueba para obtener una medida de cómo el modelo seleccionado se desempeñará en datos no vistos.

La principal ventaja del método Repeated Holdout es que reduce la varianza en la estimación del rendimiento del modelo en comparación con la técnica de Holdout. Sin embargo, tiene la desventaja de que requiere más tiempo y recursos computacionales debido a las múltiples ejecuciones.

![[Pasted image 20230708141419.png]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/1whfIOoPTlk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Criterios De Información

Los **Criterios de Información** son una clase de métodos para la selección de modelos que equilibran la calidad del ajuste del modelo con la complejidad del modelo, intentando encontrar el modelo "más simple" que se ajusta suficientemente bien a los datos. 

Estos criterios intentan penalizar la sobreajuste agregando un término a la función de pérdida que está relacionado con la complejidad del modelo (como el número de parámetros). Por lo tanto, un modelo con más parámetros no necesariamente será seleccionado a menos que proporcione una mejora significativa en el ajuste a los datos.

Dos de los criterios de información más utilizados son:

1. **Criterio de Información de Akaike (AIC)**: AIC se define como $2k - 2\log(L)$, donde $k$ es el número de parámetros en el modelo y $L$ es la verosimilitud máxima del modelo. AIC asume que los errores siguen una distribución normal y está diseñado para seleccionar modelos que minimicen la información perdida (es decir, la divergencia de Kullback-Leibler entre el modelo verdadero y el modelo propuesto).

2. **Criterio de Información Bayesiana (BIC)**: BIC se define como $k\log(n) - 2\log(L)$, donde $n$ es el número de observaciones. BIC también penaliza modelos con más parámetros, pero lo hace más severamente que AIC, especialmente cuando el número de observaciones es grande.

Tanto AIC como BIC se utilizan de manera similar: ajustas varios modelos, calculas el AIC (o BIC) para cada uno, y el modelo con el AIC (o BIC) más bajo es el que se elige.


# Validación cruzada

vease [[Validación cruzada (Cross-validation)]]

# Conclusión

La selección del modelo adecuado es crucial para obtener buenos resultados en aprendizaje automático. Existen varias técnicas para hacerlo, desde métodos sencillos como Holdout hasta métodos más sofisticados como validación cruzada y criterios informativos. La elección depende tanto del problema específico como del tiempo y recursos disponibles.






