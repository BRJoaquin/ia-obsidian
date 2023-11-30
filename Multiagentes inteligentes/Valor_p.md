
El valor para un jugador en una estrategia conjunta es el valor esperado de las recompensas que el jugador obtendrá al seguir esa estrategia. Matemáticamente, este valor, denotado por $V_p(\pi)$ para el jugador $p$ y la estrategia conjunta $\pi$, se calcula como sigue:

$$\Large V_p(\pi) = \mathbb{E}_{a \sim \pi}[ R_p(a) ] = \sum_{a \in A} \pi(a)R_p(a) $$
Aquí:

- $V_p(\pi)$ es el valor para el jugador $p$ de la estrategia conjunta $\pi$.
- $\mathbb{E}_{a \sim \pi}[ \cdot ]$ denota el valor esperado sobre la distribución de probabilidad de las acciones dictadas por la estrategia conjunta $\pi$.
- $R_p(a)$ es la recompensa que el jugador $p$ recibe al tomar la acción $a$.
- $\pi(a)$ es la probabilidad de tomar la acción $a$ según la estrategia conjunta $\pi$.
- $A$ es el conjunto de todas las posibles acciones.

# Ejemplo

![[Pasted image 20231130112323.png]]

En el ejemplo del juego "Matching Pennies", el cálculo del valor esperado $V_1$ para el Jugador 1 se muestra como:

$$
V_1 = \frac{1}{4}(-1) + \frac{1}{4}(0) + \frac{1}{4}(0) + \frac{1}{4}(1) = \frac{1}{2}
$$

Esto indica que, cuando las probabilidades de escoger "Heads" (H) y "Tails" (T) son iguales ($\pi(H) = \pi(T) = \frac{1}{2}$), el valor esperado de la estrategia para el Jugador 1 es $\frac{1}{2}$.
