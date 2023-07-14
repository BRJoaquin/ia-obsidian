
AdaBoost, o "Adaptive Boosting", es uno de los algoritmos de [[Ensemble]] más utilizados. Fue propuesto por Yoav Freund y Robert Schapire en 1996.

En términos generales, el algoritmo AdaBoost se basa en la idea de crear un "comité" de aprendices débiles (modelos debiles que solo son un poco mejor que la elección al azar, como los pequeños árboles de decisión), y combinarlos de manera que cada uno corrija los errores de sus predecesores. Esto se logra a través de un proceso iterativo en el que, en cada paso, se asignan pesos a los datos de entrenamiento en función de cuán difícil de clasificar han sido en las iteraciones anteriores.

En detalle, AdaBoost procede de la siguiente manera:

1. Inicialmente, se asigna a cada instancia de entrenamiento un peso igual a $1/N$, donde $N$ es el número total de instancias.

2. Se entrena un aprendiz débil (por ejemplo, un pequeño árbol de decisión) en los datos ponderados. Este modelo no tiene que ser perfecto, sólo un poco mejor que la elección al azar.

3. Se calcula la tasa de error ponderada del aprendiz, es decir, la suma de los pesos de las instancias que ha clasificado incorrectamente.

4. Se calcula el peso del aprendiz en el ensamble, el cual será mayor cuanto menor sea su tasa de error. Aquí, los buenos aprendices reciben más peso que los malos. La fórmula es $alpha = 0.5 * log((1 - error) / error)$, donde $alpha$ es el peso del aprendiz.

5. Se actualizan los pesos de las instancias de entrenamiento: se incrementa el peso de las instancias mal clasificadas y se disminuye el peso de las instancias correctamente clasificadas. Luego, se normalizan los pesos para que sumen 1.

6. Se vuelve al paso 2 y se repiten estos pasos hasta que se haya alcanzado un número predefinido de aprendices o hasta que el error del ensamble en el conjunto de entrenamiento sea lo suficientemente pequeño.

Finalmente, para realizar una predicción, AdaBoost simplemente suma las predicciones de todos los aprendices, ponderadas por sus respectivos pesos, y asigna la clase con la suma mayor.

![[Pasted image 20230708200812.png]]

AdaBoost es muy efectivo, tiene pocas desventajas y se adapta a los datos, dando más importancia a las instancias difíciles de clasificar a medida que avanza el proceso. Sin embargo, puede ser sensible a los datos ruidosos y a los valores atípicos debido a la forma en que se centra en las instancias difíciles de clasificar.

# Solo para clasificación?

AdaBoost fue originalmente diseñado para problemas de clasificación binaria. Sin embargo, se han desarrollado variantes de AdaBoost que pueden manejar problemas de clasificación multiclase y también regresión.

En clasificación multiclase, una versión común es AdaBoost.M1, que crea un modelo binario para cada clase, tratando esa clase como positiva y todas las demás como negativas. Luego clasifica una nueva muestra según el modelo que tiene más confianza de que es positivo.

Para la regresión, una variante popular es AdaBoost.R2. En este caso, en lugar de ponderar las muestras por cuánto fueron mal clasificadas, se ponderan por cuánto se alejó su valor verdadero del predicho por el modelo. Aparte de eso, el procedimiento es bastante similar al AdaBoost estándar.

Es importante notar que, aunque AdaBoost se puede adaptar a estas tareas, no siempre será la mejor opción. Otros métodos de ensamble, como Gradient Boosting o Random Forest, pueden proporcionar resultados superiores en algunos casos.

# Ejemplo visual

![[Pasted image 20230708203803.png]]
![[Pasted image 20230708203810.png]]
![[Pasted image 20230708203817.png]]
![[Pasted image 20230708203828.png]]



# Video 

<iframe width="560" height="315" src="https://www.youtube.com/embed/LxcGKNV5-p4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>