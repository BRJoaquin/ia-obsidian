El **Descenso de Gradiente Estocástico (SGD)** es una variante del algoritmo de [[Descenso de Gradiente]] que se utiliza comúnmente en el aprendizaje automático y las redes neuronales para optimizar una función objetivo que tiene la forma de una suma de otras funciones.

![[Pasted image 20230704131123.png]]

# ¿Cómo funciona?

El algoritmo SGD funciona de la siguiente manera:

1. Inicializa los parámetros del modelo aleatoriamente.
2. Para cada punto de datos en el conjunto de entrenamiento:
   1. Calcula el [[Grandiente]] de la función de error con respecto a los parámetros del modelo utilizando sólo ese punto de datos.
   2. Actualiza los parámetros (pesos) en la dirección **opuesta** al gradiente. La magnitud de la actualización es proporcional a la tasa de aprendizaje y al valor del gradiente.

![[Pasted image 20230704104627.png]]

# Diferencias entre SGD y Descenso de Gradiente

La diferencia principal entre SGD y el descenso de gradiente estándar es que SGD **utiliza un solo punto de datos en cada actualización de los parámetros**, mientras que el descenso de gradiente estándar utiliza todos los puntos de datos (batch o minibatch). Esto hace que SGD sea más ruidoso, pero también más rápido y más capaz de escapar de mínimos locales en problemas no convexos.

# Tasa de Aprendizaje

La tasa de aprendizaje es un [[Hiperparámetros|hiperparamentro]] importante en SGD. Una tasa de aprendizaje demasiado alta puede hacer que el algoritmo oscile alrededor del mínimo y nunca converja, mientras que una tasa de aprendizaje demasiado baja puede hacer que el algoritmo converja demasiado lentamente.

# Ejemplo: aproximación lineal de la función valor

En la aproximación lineal de la función de valor, la función de valor se representa como una combinación lineal de características del estado y/o de la acción. Es decir:

$$\Large
\hat{v}(s; w) = w^T x(s)
$$

donde:

- $\hat{v}(s; w)$ es la estimación de la función de valor del estado $s$ con parámetros $w$.
- $w$ es un vector de pesos, uno para cada característica.
- $x(s)$ es un vector de características del estado $s$.
- $w^T x(s)$ es el producto punto de $w$ y $x(s)$, que da un solo número (la estimación de la función de valor).

![[Pasted image 20230704131732.png]]

## Aprendizaje

El aprendizaje en este caso implica ajustar los pesos $w$ para minimizar la diferencia entre la estimación de la función de valor y el retorno real (en el caso de Montecarlo) o la estimación del próximo valor (en el caso de Diferencia Temporal). Esto se puede hacer con el algoritmo de Descenso de Gradiente Estocástico (SGD).

En cada paso del SGD, se calcula el gradiente del error con respecto a los pesos, y se actualizan los pesos en la dirección opuesta al gradiente. En el caso de una función lineal, el gradiente es simplemente el vector de características, por lo que la actualización de los pesos es:

$$\Large w \leftarrow w + \alpha (U_t - \hat{v}(s_t; w)) \nabla{\hat{v}}(s_t,w)$$
donde:

- $w$ es el vector de pesos.
- $\alpha$ es la tasa de aprendizaje.
- $U_t$ es el retorno real o estimado. En caso de MC es $G_t$
- $\hat{v}(s_t; w)$ es la estimación actual de la función de valor.
- $x(s_t)$ es el vector de características del estado $s_t$.

> en el caso particular de funciones lineales, $\nabla{\hat{v}}(s,w) = x(s)$

![[Pasted image 20230704113844.png]]

## Ventajas y Desventajas

La principal ventaja de la aproximación lineal es su simplicidad. Es fácil de implementar, y tiene propiedades de convergencia bien entendidas.

Las desventajas son que puede no ser capaz de representar funciones de valor que no sean lineales en las características, y que la elección de las características puede tener un gran impacto en la calidad de la aproximación.

# Método de Montecarlo con Descenso de Gradiente Estocástico (SGD)

> es importante de que este metodo es ortogonal, podemos combinarlo con otros metodos como MC y TD

![[Pasted image 20230704131336.png]]

![[Pasted image 20230704105109.png]]

El método de Montecarlo con Descenso de Gradiente Estocástico (SGD) es una técnica de aprendizaje por refuerzo que se utiliza para estimar la función de valor de una política.

## ¿Cómo funciona?

1. Generar un episodio siguiendo la política actual.
2. Por cada paso en el episodio:
   1. Calcular la recompensa total desde el paso actual hasta el final del episodio (esto se conoce como retorno) ($G_t$).
   2. Calcular el error entre el retorno y la estimación actual de la función de valor para el estado en el paso actual.
   3. Actualizar los parámetros de la función de valor en la dirección que reduce el error. La magnitud de la actualización es proporcional a la tasa de aprendizaje y al gradiente del error con respecto a los parámetros.

## Ventajas y Desventajas

El método de Montecarlo con SGD tiene la ventaja de que es simple y no requiere un modelo del entorno. Además, es capaz de aprender de la experiencia directa, **sin necesidad de bootstraping (como en Temporal Difference learning)**.

Sin embargo, **este método tiene la desventaja de que la estimación del retorno es ruidosa, especialmente al principio del episodio cuando la cantidad de datos es pequeña. Esto puede hacer que la convergencia sea lenta**.

Además, el método de Montecarlo con SGD sólo puede aprender de los episodios completos, lo que significa que no puede ser utilizado en tareas de aprendizaje por refuerzo que no tienen un estado terminal claro.

## Uso en Aprendizaje por Refuerzo

En el aprendizaje por refuerzo, el método de Montecarlo con SGD se puede utilizar para estimar tanto la función de valor de estado $V(s)$ como la función de valor de acción $Q(s, a)$. El algoritmo es el mismo en ambos casos, excepto que para estimar $Q(s, a)$, los retornos se calculan a partir de las acciones en lugar de los estados.

# Algoritmo Semi-Gradiente TD(0)

![[Pasted image 20230704124607.png]]
![[Pasted image 20230704131517.png]]

El algoritmo Semi-Gradiente TD(0) es una versión del algoritmo de Diferencia Temporal para la estimación de la función de valor $V$ que utiliza una aproximación de función y actualiza los parámetros en cada paso en lugar de al final del episodio. La actualización utiliza el gradiente de la función de valor estimada con respecto a los parámetros, pero solo la parte que depende de los parámetros que se están actualizando.

El algoritmo puede describirse de la siguiente manera:

1. Inicializar los pesos $w$ de manera aleatoria.
2. Por cada episodio:
    1. Inicializar el estado $s$.
    2. Por cada paso del episodio:
        1. Elegir una acción $a$ segun $\pi$
        2. Tomar la acción $a$, observar la recompensa $r$ y el próximo estado $s'$.
        3. Calcular el objetivo de aprendizaje $U_t = r + \gamma \hat{v}(s'; w)$.
        4. Actualizar los pesos en la dirección del semi-gradiente: $w \leftarrow w + \alpha (U_t - \hat{v}(s; w)) \nabla{\hat{v}}(s,w)$.
        5. Actualizar el estado: $s \leftarrow s'$.
    3. Repetir hasta que se cumpla una condición de finalización.

donde:

- $\hat{v}(s; w)$ es la estimación de la función de valor del estado $s$ con parámetros $w$.
- $w$ es el vector de pesos.
- $\alpha$ es la tasa de aprendizaje.
- $U_t$ es el objetivo de aprendizaje, que es una combinación de la recompensa observada y la estimación de la función de valor del próximo estado (**bootstrapping**).
- $\nabla{\hat{v}}(s,w)$ es el gradiente de la función de

> Lo mas importante: $U_t$ no se deriva ya que podría ocurrir que cambio los pesos para que se acerquen a mi estimación, y no los pesos para que se acerquen a lo real.

> TODOS los que utilizan bootstrap usan semi-gradiente

## Para estimar $q_{\pi}$

![[Pasted image 20230704125327.png]]


### SARSA

![[Pasted image 20230704125649.png]]


### Q-learning

![[Pasted image 20230704125938.png]]
> Acá esta mal cuando toma una accion: A' es A y S' es S en realidad

