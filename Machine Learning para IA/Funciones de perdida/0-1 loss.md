
La pérdida 0-1 es utilizada en problemas de clasificación y es bastante simple: si la predicción del modelo es correcta, la pérdida es 0; si la predicción del modelo es incorrecta, la pérdida es 1. Esto se expresa matemáticamente de la siguiente manera:

$$
L(y,\hat{y}) = 1_{y \neq \hat{y}}
$$

donde $1_{y \neq \hat{y}}$ es una función indicadora que es $1$ si $y$ (la etiqueta verdadera) no es igual a $\hat{y}$ (la predicción del modelo) y $0$ en caso contrario. Esta función de pérdida no tiene en cuenta qué tan confiado estaba el modelo en su predicción; solo importa si fue correcto o no.
