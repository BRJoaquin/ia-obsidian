Monte Carlo Tree Search (MCTS) es una técnica de búsqueda en árboles de decisión que combina la exploración de movimientos nuevos con la explotación de movimientos conocidos para ser prometedores. La estrategia es útil en juegos y problemas de decisión donde no es factible evaluar todas las posibles secuencias de acciones hasta el final. Aquí está el proceso detallado:

1. **Selección**:
   - Comenzando desde la raíz del árbol, el algoritmo selecciona nodos secuenciales que maximizan un cierto criterio hasta llegar a un nodo que representa un estado de juego no completamente expandido.

2. **Expansión**:
   - Si el nodo no es terminal (no representa un final del juego), se expande añadiendo uno o varios nodos hijos que representan posibles movimientos futuros.

3. **Simulación**:
   - Desde el nuevo nodo, se realiza una simulación de Monte Carlo ([[Rollout]]) para jugar al juego de forma aleatoria o semi-aleatoria hasta llegar a un estado terminal.

4. **Retropropagación**:
   - Después de la simulación, los resultados se propagan hacia atrás a través del árbol, actualizando la información estadística de los nodos visitados durante la selección y expansión.

El criterio que MCTS utiliza durante la selección se basa en la fórmula UCB (Upper Confidence Bound):

$$
UCB(n) = X_{n,m} + C \sqrt{\frac{\log m}{T_n(m)}}
$$

- $X_{n,m}$ es el promedio de las recompensas del nodo $n$.
- $m$ es el número total de simulaciones realizadas en el nodo padre de $n$.
- $T_n(m)$ es el número de simulaciones que han pasado por el nodo $n$.
- $C$ es una constante que equilibra la exploración y explotación.

> Puede utilizarse otro criterio para equilibrar exploracion-explotacion

![[Pasted image 20231201153006.png]]

![[Pasted image 20231201153029.png]]

MCTS ha demostrado ser efectivo porque ajusta dinámicamente su estrategia basándose en los resultados de las simulaciones, concentrándose más en las partes del árbol de juego que son más prometedoras. Se utiliza en una variedad de aplicaciones, desde juegos de mesa hasta la planificación en robótica y muchas otras áreas de la inteligencia artificial.
