Label Encoding es otra técnica utilizada para convertir variables categóricas en numéricas. A diferencia del One-Hot Encoding, en lugar de crear una nueva característica para cada categoría, Label Encoding asigna a cada categoría única un valor entero. 

Esto puede ser particularmente útil cuando tienes una variable categórica con muchas categorías únicas, ya que Label Encoding no aumentará la dimensionalidad de tus datos de la misma manera que One-Hot Encoding.

Por ejemplo, considera la variable categórica "Ciudad" con las categorías "Madrid", "Barcelona" y "Valencia". Usando Label Encoding, podrías asignar a "Madrid" el valor 0, a "Barcelona" el valor 1 y a "Valencia" el valor 2. 

Aquí está un ejemplo concreto. Supón que tienes el siguiente conjunto de datos:

ID Ciudad 
1 Madrid
2 Barcelona
3 Valencia
4 Madrid
5 Valencia


Después de aplicar Label Encoding a la columna 'Ciudad', el conjunto de datos se vería así:

ID Ciudad 
1 0
2 1
3 2
4 0
5 2


Es importante tener en cuenta que, aunque Label Encoding es útil en muchos casos, puede introducir un orden en los datos que no estaba presente originalmente. En el ejemplo anterior, puede parecer que "Valencia" (2) es de alguna manera "más" que "Madrid" (0), lo cual no tiene sentido en el contexto original de los datos.

Por lo tanto, debes usar Label Encoding con precaución y considerar si es la mejor opción para tu caso específico. Para algunos algoritmos, como los árboles de decisión, esto no es un problema. Sin embargo, para muchos otros algoritmos, este orden artificial puede resultar en un rendimiento peor y se prefiere [[One-hot encoding]].
