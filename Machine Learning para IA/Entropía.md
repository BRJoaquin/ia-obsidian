La entropía también es una medida de la impureza, la incertidumbre o el desorden dentro de un conjunto de instancias. Al igual que el índice de [[Gini]], se utiliza para decidir dónde dividir los datos en un árbol de decisión. 

Un conjunto de datos que contiene instancias de una sola clase tiene una entropía de 0 (puro), mientras que un conjunto de datos que contiene una mezcla equitativa de clases tiene la máxima entropía. La meta en un árbol de decisión es realizar divisiones de tal manera que se minimice la entropía.
  
Imagina que tienes un cesto lleno de manzanas y naranjas. Si todas las frutas son manzanas, el cesto es "puro" y la entropía es cero, porque no hay incertidumbre: sabes que cualquier fruta que saques será una manzana. Por el contrario, si el cesto tiene la mitad de manzanas y la mitad de naranjas, la entropía es máxima: hay mucha incertidumbre porque es igualmente probable que saques una manzana o una naranja.

La entropía de un conjunto se calcula utilizando la fórmula de la entropía de Shannon:

$$ H(S) = - \sum p_i \log_2 p_i $$

Donde:
* $S$ es el conjunto de datos
* $p_i$ es la probabilidad de que un elemento del conjunto pertenezca a la clase $i$.

Por ejemplo, si tienes un conjunto de datos con 100 elementos, 60 de los cuales pertenecen a la clase 1 y 40 a la clase 2, la entropía del conjunto sería:

$$ H(S) = - \left( \frac{60}{100} \log_2 \frac{60}{100} + \frac{40}{100} \log_2 \frac{40}{100} \right) $$
