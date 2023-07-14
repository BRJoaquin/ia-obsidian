Esta es una métrica que mide la impureza de un conjunto de instancias. Cuando se usa en árboles de decisión, el índice de Gini cuantifica la impureza de una partición de datos. Cuando todas las instancias en un conjunto de datos pertenecen a la misma clase, el índice de Gini es 0 (indicando que el conjunto de datos es puro). Si las instancias están distribuidas equitativamente entre todas las clases, el índice de Gini es máximo (1 para un problema de clasificación binaria). Un árbol de decisión intentará dividir los datos de tal manera que minimice el índice de Gini y, por tanto, aumente la pureza de los datos.


  
Imagina que tienes un cesto lleno de manzanas y naranjas. Si todas las frutas en el cesto son manzanas, el índice Gini es 0, porque no hay ninguna posibilidad de clasificar incorrectamente la fruta que saques. Pero si la mitad de las frutas son manzanas y la otra mitad son naranjas, el índice Gini es 0.5 (suponiendo que asignas la clase al azar): hay una alta probabilidad de que clasifiques incorrectamente la fruta que saques.

El índice Gini se calcula con la fórmula:

$$ G(S) = 1 - \sum (p_i)^2 $$

Donde:
* $S$ es el conjunto de datos
* $p_i$ es la probabilidad de que un elemento del conjunto pertenezca a la clase $i$.

Por ejemplo, si tienes un conjunto de datos con 100 elementos, 60 de los cuales pertenecen a la clase 1 y 40 a la clase 2, el índice Gini sería:

$$ G(S) = 1 - \left( \left(\frac{60}{100}\right)^2 + \left(\frac{40}{100}\right)^2 \right) $$

Por lo tanto, tanto la entropía como el índice Gini nos dan una medida de cuán impuro es un conjunto. Cuanto más bajo sea el valor, más "puro" (es decir, más uniforme en términos de la distribución de clase) es el conjunto. ver
