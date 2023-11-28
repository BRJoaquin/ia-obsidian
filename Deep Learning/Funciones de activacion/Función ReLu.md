
La **ReLU** (Unidad Lineal Rectificada) es una [[Agentes inteligentes/Función de Activación]] muy comúnmente utilizada en las [[Redes Neuronales Artificiales]] y el [[Deep Learning]]. **Se ha convertido en la función de activación por defecto para muchos tipos de redes neuronales porque produce resultados muy buenos en la práctica y es computacionalmente eficiente**.

![[Pasted image 20230626090250.png]]

La función ReLU es una función no lineal que "rectifica" la entrada a 0 si es negativa. Si la entrada es positiva, la devuelve sin cambios.

En forma de ecuación, la función ReLU se puede expresar como:

$$
f(x) = \max(0, x)
$$

donde $x$ es la entrada a la función.

Así, la función ReLU tiene la propiedad de convertir todas las entradas negativas en cero, mientras que las entradas positivas se mantienen iguales.

Es importante notar que la función ReLU es una función no diferenciable en $x=0$. Sin embargo, en la práctica, este no es un problema importante, ya que el gradiente se puede definir como 0 o 1 en ese punto y el algoritmo de optimización (como el descenso de gradiente) puede seguir funcionando.

La ReLU tiene algunas variantes, como la función de [[Función Leaky ReLU]] y la Parametric ReLU (PReLU), que permiten un pequeño valor de gradiente cuando la entrada es negativa, lo que puede ayudar a mitigar el problema de las "neuronas muertas" (es decir, las neuronas que siempre se activan a 0).
