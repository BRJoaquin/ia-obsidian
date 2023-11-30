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

