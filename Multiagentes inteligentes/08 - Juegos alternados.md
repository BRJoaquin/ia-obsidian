- [[Juegos Alternados]]
- [[Árbol de Juego]]
- [[ExpectiMax]]
- [[Minimax]]
- [[ExpectiMiniMax]]

  
La elección entre Minimax, Expectimax y Expectiminimax depende del tipo de problema y el modelo del ambiente que estás enfrentando.

1. **Minimax**:
    
    - **Uso**: Minimax es ideal para juegos de suma cero de dos jugadores como ajedrez o damas, donde hay un oponente claramente definido y las acciones del oponente son completamente adversarias.
    - **Características**: En Minimax, cada jugador asume que el oponente jugará de manera óptima para maximizar su propia utilidad, lo que implica minimizar la utilidad del primer jugador. El algoritmo explora el árbol de juego hasta una cierta profundidad y utiliza una función de evaluación para determinar los movimientos más prometedores.
2. **Expectimax**:
    
    - **Uso**: Expectimax es útil en escenarios donde el adversario no es completamente adversario o donde hay elementos de azar, como en algunos juegos de mesa que involucran dados.
    - **Características**: A diferencia de Minimax, que considera el peor caso (movimiento óptimo del adversario), Expectimax utiliza una función de probabilidad para considerar todos los posibles movimientos del adversario y calcular un valor esperado basado en la probabilidad de cada movimiento.
3. **Expectiminimax**:
    
    - **Uso**: Expectiminimax es menos común, pero se usa en situaciones que involucran múltiples agentes con objetivos diferentes, y donde hay incertidumbre tanto en las acciones de los adversarios como en elementos del entorno.
    - **Características**: Este algoritmo combina elementos de Minimax (considerando las mejores jugadas del oponente) y Expectimax (teniendo en cuenta la aleatoriedad o incertidumbre). Es una especie de generalización de ambos, donde se alternan niveles de decisión (Minimax) con niveles de expectativa (Expectimax).

En resumen:

- Usa **Minimax** en juegos competitivos de dos jugadores sin azar.
- Usa **Expectimax** en juegos o situaciones con elementos de azar o donde los oponentes no son completamente adversarios.
- Usa **Expectiminimax** en escenarios más complejos con múltiples agentes, objetivos mixtos y elementos de incertidumbre.