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

# Equilibrio dominante iterado

![[Pasted image 20231130100805.png]]

El Equilibrio Dominante Iterado es un concepto de la [[Teoría de Juegos|teoría de juegos]] que se utiliza para predecir el resultado de juegos estratégicos en los que cada jugador elige su estrategia de manera racional y con conocimiento de las estrategias de los demás jugadores.

El proceso funciona de la siguiente manera:

1. Se identifican estrategias que son dominadas (estrictamente o débilmente) y se eliminan del conjunto de estrategias posibles de cada jugador.
    
2. Después de eliminar una estrategia dominada, se revisa nuevamente el conjunto de estrategias restantes para ver si la eliminación de una estrategia ha llevado a que otra se vuelva dominada. Si es así, esta nueva estrategia dominada también se elimina.
    
3. Este proceso se repite iterativamente hasta que no quedan más estrategias dominadas para eliminar.


El resultado final, si existe, es una estrategia que no está dominada después de que todas las estrategias dominadas hayan sido eliminadas. Esta estrategia es robusta en el sentido de que sobrevive a la eliminación de todas las estrategias inferiores.

En el juego presentado en la imagen, el análisis muestra que:

- Independientemente de lo que haga el Jugador 2, la estrategia U del Jugador 1 está dominada por D, porque D proporciona una recompensa mayor o igual en todas las posibles respuestas del Jugador 2.
    
- Si el Jugador 2 sabe que el Jugador 1 nunca jugará U (porque está dominada por D), entonces el Jugador 2 puede eliminar la columna U de su análisis.
    
- Si el Jugador 1 sabe que el Jugador 2 sabe que U no será jugada, entonces el Jugador 1 puede concluir que el Jugador 2 jugará C (dado que ahora es la estrategia óptima para el Jugador 2).
    
- Al final, el Jugador 1 jugará D, porque es la respuesta óptima a la elección de C por parte del Jugador 2.


La idea subyacente del Equilibrio Dominante Iterado es que los jugadores racionales usarán su conocimiento común sobre la racionalidad para eliminar estrategias que no son óptimas. Esto puede llevar a una previsión más precisa de las acciones que los jugadores probablemente tomarán en el juego.