El **producto matricial** es una operación que produce una matriz a partir de dos matrices, multiplicando filas por columnas. 

El producto matricial es esencial en Deep Learning para realizar operaciones lineales en las neuronas, como en la propagación hacia adelante (forward propagation) en redes neuronales.

![[Pasted image 20231127153333.png]]


# Ejemplo de Producto Matricial

Consideremos dos matrices $A$ y $B$ definidas como:
$$
A = 
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\quad
B = 
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
$$

El producto de $A$ y $B$, denotado como $AB$, se calcula como sigue:
$$
AB = 
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
=
\begin{pmatrix}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{pmatrix}
=
\begin{pmatrix}
19 & 22 \\
43 & 50
\end{pmatrix}
$$

En este caso, el elemento en la primera fila y primera columna de $AB$ es el resultado de sumar el producto de los elementos de la primera fila de $A$ con los elementos correspondientes de la primera columna de $B$, y así sucesivamente para los demás elementos de $AB$.

