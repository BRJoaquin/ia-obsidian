La optimización de la política a través del gradiente de la política es uno de los enfoques fundamentales en el aprendizaje por refuerzo. Los métodos de gradiente de política operan buscando directamente en el espacio de políticas un óptimo, ajustando las probabilidades de las acciones en dirección al gradiente del rendimiento esperado.

A diferencia de los métodos basados en valor que intentan aprender una función de valor que luego se utiliza para determinar una política, los métodos de gradiente de política trabajan directamente con el parámetro de la política. Esto puede ser particularmente útil en ciertas situaciones, como cuando la política es una función continua y diferenciable de su parámetro, o cuando se busca una política estocástica en lugar de una determinista.

# Gradiente de Política

Para entender cómo funcionan estos métodos, primero debemos entender el concepto de gradiente de política. El gradiente de una política es simplemente el vector de las derivadas parciales de la política con respecto a sus parámetros. Para una política $\pi(a|s, \theta)$ parametrizada por $\theta$, el gradiente de la política es $\nabla_{\theta} \pi(a|s, \theta)$.

El método de gradiente de política ajusta los parámetros de la política moviéndolos en la dirección del gradiente del rendimiento esperado. Supongamos que J($\theta$) es la función objetivo (que representa el rendimiento esperado bajo la política), entonces el ajuste de los parámetros se realiza de la siguiente manera:

$$\Large
\theta_{t+1} = \theta_t + \alpha \nabla_{\theta} J(\theta_t)$$

# Algoritmo REINFORCE

Un algoritmo popular de gradiente de política es el algoritmo REINFORCE. Este algoritmo se basa en la idea de que si una acción tomada en un tiempo específico llevó a una buena recompensa, entonces deberíamos aumentar la probabilidad de tomar esa acción en el futuro.

El algoritmo REINFORCE realiza esto haciendo una actualización proporcional a la gradiente de la política multiplicada por la función de ventaja, que es la recompensa obtenida después de tomar la acción menos el valor del estado desde el que se tomó la acción. En el caso de REINFORCE, esta función de ventaja se estima utilizando toda la recompensa futura obtenida después de tomar la acción.

Aquí está el algoritmo REINFORCE:

```
Inicializar parámetros de política θ arbitrariamente
Para cada episodio:
    Generar un episodio S0, A0, R1, ..., ST-1, AT-1, RT siguiendo π(·|·, θ)
    Para t = 0 hasta T-1:
        G ← retorno desde el paso t
        θ ← θ + α γ^t G ∇θ log π(At|St, θ)
```

![[Pasted image 20230706151020.png]]

## REINFORCE con Línea de Base

Aunque el algoritmo REINFORCE puede aprender políticas efectivas, tiene una alta varianza que puede ralentizar su convergencia. Para reducir esta varianza, podemos introducir una línea de base que se resta de la recompensa antes de la actualización.

La línea de base puede ser cualquier función que no dependa de la acción. Un ejemplo común de línea de base es la función de valor del estado $V(s)$. Cuando se utiliza una línea de base, la actualización del parámetro se realiza con respecto a la diferencia entre la recompensa y la línea de base, que se conoce como la función de ventaja.

Aquí está el algoritmo REINFORCE con línea de base:

```
Inicializar parámetros de política θ y función de valor V arbitrariamente
Para cada episodio:
    Generar un episodio S0, A0, R1, ..., ST-1, AT-1, RT siguiendo π(·|·, θ)
    Para t = 0 hasta T-1:
        G ← retorno desde el paso t
        δ ← G - V(St)
        θ ← θ + α γ^t δ ∇θ log π(At|St, θ)
        V(St) ← V(St) + β δ
```

Donde `β` es un paso de tamaño que se puede ajustar.

![[Pasted image 20230706151054.png]]

Este algoritmo se llama REINFORCE con línea de base porque introduce una línea de base para reducir la varianza de la actualización de los parámetros, lo que puede mejorar la eficiencia del algoritmo.

![[Pasted image 20230706151133.png]]

# Métodos de actor-critico

ver [[Método Actor-Critic]]

# Cuando utilizar Gradiente de Política

Los métodos de gradiente de política son particularmente útiles en ciertos contextos. Por ejemplo, cuando la política tiene una estructura que se puede aprovechar para facilitar el aprendizaje. Por ejemplo, si la política es una función lineal de los parámetros, entonces el gradiente de la política puede ser fácilmente calculado y utilizado para la optimización.

Además, los métodos de gradiente de política son útiles cuando se desea una política estocástica en lugar de una determinista. En algunos casos, una política estocástica puede ser más robusta a las perturbaciones y puede permitir la exploración continua del espacio de acción.

En resumen, los métodos de gradiente de política son un enfoque directo para la optimización de la política en el aprendizaje por refuerzo. El algoritmo REINFORCE, y su extensión que incluye una línea de base, son ejemplos de este enfoque que utilizan la dirección del gradiente de la política para mejorar continuamente la política en términos del rendimiento esperado.


# Videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/e20EY4tFC_Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/y3oqOjHilio" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
