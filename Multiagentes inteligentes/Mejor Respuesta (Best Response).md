La "best response" (mejor respuesta) es una estrategia que produce el mejor resultado posible para un jugador, tomando como fijo el conjunto de estrategias de los otros jugadores. Para cada jugador, la mejor respuesta puede depender de las acciones que espera de los otros jugadores. En un [[Equilibro de Nash]], todas las estrategias elegidas son mejores respuestas a las estrategias de los demás jugadores.

![[Pasted image 20231130102756.png]]

# Caso general (estrategia estocástica)

Para un jugador $p$, su mejor respuesta $\pi_p$ a la estrategia conjunta de los otros jugadores $\pi_{-p}$ se define como la estrategia que resulta en la mayor utilidad esperada para él. Se denota matemáticamente como:

$$\Large
\pi_p = \text{arg max}_{\pi'_p \in \Delta(A_p)} V_p(\pi'_p, \pi_{-p})
$$

Donde:

- $\pi_p$ es la estrategia del jugador $p$.
- $\Delta(A_p)$ representa el conjunto de todas las posibles estrategias mixtas (distribuciones de probabilidad) sobre el conjunto de acciones $A_p$ disponible para el jugador $p$.
- $V_p(\pi'_p, \pi_{-p})$ es la utilidad esperada para el jugador $p$ cuando juega la estrategia $\pi'_p$ mientras que los otros jugadores juegan la estrategia $\pi_{-p}$. ver [[Valor_p]]
- "arg max" es un argumento que maximiza la función, lo que significa que $\pi_p$ es la estrategia que produce la mayor utilidad esperada para $p$, dadas las estrategias de los otros jugadores.

La notación $BR(\pi_{-p})$ se refiere al conjunto de todas las mejores respuestas del jugador $p$ a la estrategia $\pi_{-p}$ de los demás jugadores. Dado que puede haber múltiples estrategias que maximizan la utilidad esperada para un jugador, $BR(\pi_{-p})$ puede contener más de una estrategia.

![[Pasted image 20231130113003.png]]

En el contexto de una estrategia conjunta, calcular la mejor respuesta implica considerar todas las combinaciones posibles de acciones de los demás jugadores y elegir la estrategia que proporcione la mayor utilidad esperada en respuesta a esas combinaciones. Esto se hace típicamente utilizando el cálculo de expectativas basado en las probabilidades de las estrategias de los otros jugadores y las recompensas asociadas con cada combinación de acciones.

## Ejemplo

En un juego de suma cero, las ganancias de un jugador se compensan exactamente con las pérdidas del otro jugador. Matemáticamente, esto se representa como:

$$
\forall a \in A, \ R_1(a) = -R_2(a)
$$

Esto significa que si uno de los jugadores gana un punto, el otro jugador pierde un punto y viceversa. Por lo tanto, la utilidad esperada para el jugador 1, $V_1(\pi)$, es igual al negativo de la utilidad esperada para el jugador 2, $V_2(\pi)$, en todas las estrategias $\pi$:

$$
V_1(\pi) = \sum_{a \in A} \pi(a) R_1(a) = - \sum_{a \in A} \pi(a) R_2(a) = -V_2(\pi)
$$

![[Pasted image 20231130114120.png]]

Para el juego "Matching Pennies", consideramos la estrategia mixta de jugador 2, $\pi_2 = (h_2, t_2) = (\frac{1}{3}, \frac{2}{3})$. La mejor respuesta de jugador 1, $\pi_1$, a esta estrategia sería aquella que maximiza su utilidad esperada $V_1(\pi_1, \pi_2)$.

La utilidad esperada para jugador 1 se calcula como:

$$
V_1(\pi_1, \pi_2) = h_2 (1h_1 - 1t_1) + t_2 (-1h_1 + 1t_1)
$$

Sustituimos los valores de $h_2$ y $t_2$:

$$
V_1(\pi_1, \pi_2) = \frac{1}{3} (h_1 - (1 - h_1)) + \frac{2}{3} (-h_1 + (1 - h_1))
$$

$$
V_1(\pi_1, \pi_2) = \frac{1}{3} (2h_1 - 1) + \frac{2}{3} (-2h_1 + 1)
$$

$$
V_1(\pi_1, \pi_2) = -\frac{2}{3}h_1 + \frac{1}{3}
$$
![[Pasted image 20231130114200.png]]

Para encontrar la mejor respuesta, buscamos el valor de $h_1$ que maximice $V_1(\pi_1, \pi_2)$. Dado que $V_1$ disminuye a medida que $h_1$ aumenta, la mejor respuesta para el jugador 1 es minimizar $h_1$, que es $h_1 = 0$. Entonces, la mejor respuesta de jugador 1, cuando jugador 2 juega $\pi_2$, es jugar "Tails" todo el tiempo (estrategia pura $t_1 = 1$).

La mejor respuesta de jugador 1 a la estrategia mixta de jugador 2 es $BR(\pi_2) = \{(0, 1)\}$, lo que significa que siempre elige "Tails" (T).


