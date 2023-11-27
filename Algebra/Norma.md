La **norma** es una función que asigna una longitud o tamaño a cada vector en un espacio vectorial. 

En matemáticas, la norma se utiliza para determinar la "longitud" de un vector. Un ejemplo común es la **norma euclidiana** (también conocida como norma L2), que para un vector $\mathbf{v} = (v_1, v_2, ..., v_n)$ se calcula como:

$$\text{Norma L2}(\mathbf{v}) = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}$$


Por ejemplo, para el vector $\mathbf{v} = (3, 4)$, la norma L2 sería:
$$\text{Norma L2}(\mathbf{v}) = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$


En Deep Learning, las normas se utilizan para medir el tamaño de los vectores (como los pesos de una red neuronal) y son fundamentales en la regularización (como L1 o L2) para evitar el sobreajuste.