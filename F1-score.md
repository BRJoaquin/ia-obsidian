Es una medida de la precisión de un modelo de [[Clasificación]]. **Se calcula a partir de la combinación armónica de la precisión y el recall del modelo**.

La precisión es la proporción de verdaderos positivos (instancias correctamente clasificadas como positivas) sobre el total de instancias clasificadas como positivas. Mientras que el recall es la proporción de verdaderos positivos sobre el total de instancias que realmente son positivas.
   $$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

El F1-score combina estas dos métricas en una sola medida, calculando su media armónica. La media armónica da más peso a los valores más bajos, por lo que si tanto la precisión como el recall son altos, el F1-score también será alto. Sin embargo, si uno de ellos es bajo, el F1-score también será bajo.

El F1-score es especialmente útil cuando hay un desequilibrio en las clases del problema, es decir, cuando una clase tiene muchas más instancias que otra. En estos casos, la precisión puede ser alta simplemente porque se clasifican correctamente muchas instancias negativas (la clase mayoritaria), mientras que el recall puede ser bajo porque se clasifican incorrectamente muchas instancias positivas (la clase minoritaria). El F1-score permite tener una visión más equilibrada del rendimiento del modelo en ambos casos.

En resumen, el F1-score es una medida útil para evaluar modelos de clasificación cuando se busca un equilibrio entre la precisión y el recall. 