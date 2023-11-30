  
El concepto de Maxmin y Minmax está relacionado con estrategias en juegos de teoría de juegos, especialmente en juegos de suma cero de dos jugadores.

El Maxmin se refiere a la estrategia que maximiza la recompensa mínima que un jugador puede asegurarse sin saber las acciones del oponente. Es decir, el jugador asume que el oponente tomará la acción que resulte en la menor recompensa posible para él y, con eso en mente, elige la acción que maximiza su recompensa mínima garantizada. La estrategia Maxmin para un jugador es aquella que asegura el mejor de los peores resultados posibles.

El Minmax, por otro lado, es la estrategia que minimiza la recompensa máxima que el oponente puede obtener. En este caso, el jugador asume que el oponente está tratando de maximizar su recompensa y, por lo tanto, el jugador elige la acción que minimiza la recompensa máxima del oponente.

En juegos de suma cero, el valor Maxmin para un jugador es igual al valor Minmax para el otro jugador, lo que implica que ambos jugadores están esencialmente tratando de optimizar sus propias estrategias teniendo en cuenta las peores estrategias del oponente. Esto lleva al concepto de equilibrio, donde cada jugador ha ajustado su estrategia a la estrategia óptima del oponente.

El Teorema Minimax de John von Neumann establece que en juegos de suma cero de dos jugadores, existe al menos un par de estrategias ��∗πa∗​ y ��∗πo∗​ para los jugadores tal que:

- $\pi_a^*$ es una estrategia Maxmin, que maximiza la recompensa mínima del jugador.
- *\pi_o^**​ es una estrategia Minmax, que minimiza la recompensa máxima del oponente.

Estas estrategias forman un [[Equilibro de Nash|equilibrio de Nash ]](EN) porque ninguna de ellas se beneficiaría cambiando su estrategia mientras el otro jugador mantenga la suya. En este equilibrio, ambas estrategias son las mejores respuestas mutuas (BR) una de la otra. Cada equilibrio de Nash en un juego de suma cero tiene un valor asociado, llamado valor Minimax del juego, y es la solución del juego.

En resumen, Maxmin y Minmax son conceptos clave en la determinación de estrategias óptimas en juegos de suma cero y son fundamentales para entender cómo los jugadores racionales tomarán decisiones en un entorno competitivo donde cada jugador está intentando maximizar su propia recompensa mientras minimiza la del oponente.

![[Pasted image 20231130144218.png]]

![[Pasted image 20231130144237.png]]

![[Pasted image 20231130144255.png]]