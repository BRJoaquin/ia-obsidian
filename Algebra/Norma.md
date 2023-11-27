La **norma** es una función que asigna una longitud o tamaño a cada vector en un espacio vectorial. 

En matemáticas, la norma se utiliza para determinar la "longitud" de un vector. Un ejemplo común es la **norma euclidiana** (también conocida como norma L2), que para un vector $\mathbf{v} = (v_1, v_2, ..., v_n)$ se calcula como:

$$\text{Norma L2}(\mathbf{v}) = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}$$


Por ejemplo, para el vector $\mathbf{v} = (3, 4)$, la norma L2 sería:
$$\text{Norma L2}(\mathbf{v}) = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

En [[Deep Learning]], la norma se utiliza, por ejemplo, en la [[Regularización]] de los pesos de una red neuronal. Un uso común es la $\textbf{regularización L2}$, donde la norma L2 de los pesos se añade a la función de coste para penalizar los valores grandes de los pesos. Esto ayuda a evitar el [[Sobreajuste (Overfitting)|sobreajuste]], ya que impide que los pesos tomen valores demasiado grandes.

La regularización L2 se puede expresar como:
$$
\text{Coste total} = \text{Coste de pérdida} + \lambda \times \text{Norma L2}(\text{pesos})
$$
Donde $\lambda$ es un parámetro que controla cuánta importancia se le da a la regularización respecto al coste de pérdida original.

En resumen, mientras que en matemáticas la norma se utiliza para medir la longitud de un vector, en Deep Learning se emplea para controlar la magnitud de los pesos de una red, contribuyendo a un entrenamiento más estable y a la prevención del sobreajuste.


![[Pasted image 20231127153154.png]]