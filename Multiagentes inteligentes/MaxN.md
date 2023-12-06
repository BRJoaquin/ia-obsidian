MaxN es un algoritmo utilizado en [[Teoría de Juegos|teoría de juegos]], especialmente diseñado para juegos de múltiples jugadores. A diferencia de Minimax, que está enfocado en juegos de dos jugadores con objetivos directamente opuestos ([[Juego de suma cero|suma cero]]), MaxN se utiliza en situaciones donde hay más de dos jugadores y cada uno puede tener sus propios objetivos.

![[Pasted image 20231206074326.png]]

1. **Utilidad(s)**: Es una función que asigna un vector de valores a cada estado final del juego, `s`, donde `n` es el número de jugadores. Cada componente del vector corresponde a la utilidad para un jugador específico.

2. **\( V_{max^n}(s)$**: Es el valor del juego para un estado `s` bajo la suposición de que todos los jugadores juegan óptimamente. El valor es definido recursivamente como:
   - Si `s` es un estado final (`EsFinal(s)`), el valor de `s` es simplemente `Utilidad(s)`.
   - Si no es un estado final, y es el turno del jugador `p` (`Jugador(s) = p`), entonces el valor es el máximo sobre todas las acciones posibles `a` que el jugador `p` puede tomar (`a \in Acc(s)`). Aquí, `Acc(s)` representa el conjunto de acciones legales desde el estado `s`.
   - El valor máximo se calcula comparando los vectores de utilidad `u` y `v`, donde `u` es preferido sobre `v` si y solo si la utilidad de `p` en `u` es mayor o igual que en `v` (denotado por `u \geq_p v`).

3. **Árbol de Juego**: La estructura del árbol muestra cómo se despliegan los movimientos a través del juego. Cada nodo representa un estado del juego y cada arista representa una acción que lleva a un estado sucesor.
   - **Nodos etiquetados con A, B, C**: Representan los turnos de los jugadores.
   - **Vectores en los nodos**: Representan la utilidad para cada jugador en ese nodo. Por ejemplo, (1,2,6) significa que el jugador A tiene una utilidad de 1, el jugador B una utilidad de 2, y el jugador C una utilidad de 6.
   - **Nodos cuadrados vs. nodos circulares**: Los nodos cuadrados podrían representar decisiones de jugadores, mientras que los nodos circulares podrían representar eventos aleatorios o decisiones de otros jugadores.
   - **La cruz en un nodo**: Indica que ese nodo es un estado final.

El proceso de toma de decisiones en MaxN implica mirar hacia adelante en el árbol y, en cada paso, seleccionar la acción que maximiza la utilidad del jugador en turno, considerando que los otros jugadores también están maximizando sus propias utilidades. Este algoritmo es particularmente útil para juegos de suma no cero con más de dos jugadores, donde cada jugador tiene diferentes `payoffs` y puede ganar independientemente de los otros.



### Características de MaxN:

1. **Generalización de Minimax**: MaxN es una generalización del algoritmo [[Minimax|Minimax]] para n jugadores. Mientras que Minimax considera el mejor movimiento para un jugador y el peor para el adversario, MaxN busca optimizar los movimientos considerando los intereses de todos los jugadores.
    
2. **Función de Utilidad para Cada Jugador**: En MaxN, cada jugador tiene su propia función de utilidad, que no necesariamente es la negativa de los demás jugadores. Esto permite una mayor flexibilidad para modelar juegos donde los objetivos de los jugadores no son completamente adversarios.
    
3. **Árbol de Juego**: Como en Minimax, MaxN explora un árbol de juego. Sin embargo, en lugar de alternar entre maximizar y minimizar, cada nivel del árbol corresponde a un jugador diferente, y el objetivo en cada nivel es maximizar la utilidad de ese jugador específico.
    
4. **Estrategias Óptimas para Todos los Jugadores**: MaxN trata de encontrar la estrategia óptima para todos los jugadores, no solo para uno. En teoría, esto conduce a una solución más equilibrada y representativa de situaciones reales en juegos de múltiples jugadores.

### Consideraciones:

- **Complejidad**: Al aumentar el número de jugadores, la complejidad del [[Árbol de Juego|árbol de juego]] crece exponencialmente, lo que puede hacer que MaxN sea computacionalmente intensivo.
- **Equilibrio entre Jugadores**: En juegos donde los jugadores tienen objetivos muy diferentes, encontrar una solución que satisfaga a todos puede ser un desafío.


