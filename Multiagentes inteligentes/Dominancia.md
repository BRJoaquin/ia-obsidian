La dominancia en estrategias se refiere a la comparación de la efectividad de diferentes estrategias dentro de un juego. En la teoría de juegos, una estrategia domina a otra si produce un mejor resultado para el jugador, independientemente de las estrategias de los otros jugadores. Hay dos tipos principales de dominancia: estricta y débil.

1. **Dominancia Estricta**:
    - Una estrategia $\pi_p$ domina estrictamente a otra estrategia $\pi'_p$ si, para todas las estrategias posibles de los otros jugadores $\pi_{-p}$, se cumple que $R_p(\pi_p, \pi_{-p}) > R_p(\pi'_p, \pi_{-p})$.
      
      ![[Pasted image 20231130093856.png]]
      
2. **Dominancia Débil**:
    - Una estrategia $\pi_p$ domina débilmente a otra estrategia $\pi'_p$ si, para todas las estrategias posibles de los otros jugadores $\pi_{-p}$, se cumple que $R_p(\pi_p, \pi_{-p}) \geq R_p(\pi'_p, \pi_{-p})$, y existe al menos un $\pi_{-p}$ tal que $R_p(\pi_p, \pi_{-p}) > R_p(\pi'_p, \pi_{-p})$.
      
      ![[Pasted image 20231130093917.png]]
      
3. **Estrategias Equivalentes**:
    - Dos estrategias $\pi_p$ y $\pi'_p$ son equivalentes si, para todas las estrategias posibles de los otros jugadores $\pi_{-p}$, se cumple que $R_p(\pi_p, \pi_{-p}) = R_p(\pi'_p, \pi_{-p})$.
      
    ![[Pasted image 20231130094015.png]]


El concepto de dominancia es utilizado para simplificar el análisis de juegos identificando estrategias que son claramente subóptimas y pueden ser eliminadas del análisis. Por ejemplo, si una estrategia es estrictamente dominada, un jugador racional nunca la elegiría, ya que siempre hay una opción mejor disponible.

![[Pasted image 20231130095508.png]]

