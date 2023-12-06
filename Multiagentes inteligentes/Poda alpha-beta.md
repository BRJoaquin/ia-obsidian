
La poda alfa-beta (α-β) es una técnica de optimización utilizada junto con el algoritmo [[Minimax|Minimax]] en la teoría de juegos y en la inteligencia artificial para juegos de dos jugadores de suma cero. El propósito principal de la poda alfa-beta es reducir el número de nodos que se evalúan en el árbol de juego de Minimax, lo que aumenta la eficiencia del algoritmo sin afectar el resultado final.

**Principios Básicos de la Poda Alfa-Beta:**

1. **Alfa (α)**: Es el valor de la mejor (más alta) opción ya encontrada en el camino hacia el nodo actual para el maximizador. Inicialmente, α es -∞.
    
2. **Beta (β)**: Es el valor de la mejor (más baja) opción ya encontrada en el camino hacia el nodo actual para el minimizador. Inicialmente, β es +∞.
    
3. **Poda**: Durante la búsqueda, si se encuentra que el valor de un nodo es peor que el valor de α o β actual para el respectivo jugador, entonces ese nodo y sus descendientes no necesitan ser evaluados más, ya que sabemos que no influirán en la decisión final.
    

**Funcionamiento del Algoritmo:**

- Mientras se explora el árbol de juego, se mantienen actualizados los valores de α y β.
- Si en cualquier punto del árbol, α se vuelve mayor o igual a β (α ≥ β), se realiza una poda, lo que significa que se descartan ciertas ramas del árbol que no necesitan ser exploradas porque ya se sabe que no contienen una opción mejor que las ya exploradas.

**Ventajas de la Poda Alfa-Beta:**

- **Eficiencia Mejorada**: Reduce significativamente el número de nodos evaluados en el árbol de juego, lo que resulta en una mayor eficiencia computacional.
- **Profundidad Mayor en la Búsqueda**: Permite buscar más profundamente en el árbol de juego en el mismo tiempo, lo que puede resultar en mejores decisiones en juegos complejos.
- **Optimización de Minimax**: Mejora la eficacia del algoritmo Minimax sin comprometer la exactitud del resultado final.

**Limitaciones y Consideraciones:**

- **Depende del Orden de los Nodos**: La efectividad de la poda alfa-beta puede depender en gran medida del orden en que se examinan los nodos. Una heurística de búsqueda bien diseñada que examina primero los nodos prometedores puede mejorar significativamente la efectividad de la poda.
- **Complejidad en la Implementación**: La implementación de la poda alfa-beta es más compleja que el Minimax estándar, especialmente en juegos con estructuras de árbol más complicadas o con información imperfecta.

**Aplicaciones de la Poda Alfa-Beta:**

La poda alfa-beta se utiliza en programas de IA para juegos de tablero como el ajedrez, las damas y el go, donde se requiere calcular la mejor jugada posible dada una posición actual en el juego. Además, se aplica en cualquier situación de toma de decisiones secuencial donde se busca optimizar el rendimiento mientras se manejan recursos computacionales limitados.

![[Pasted image 20231201121613.png]]
# Links y video

https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=header_search


<iframe width="560" height="315" src="https://www.youtube.com/embed/I0y-TGehf-4?si=q9PmTqpq9Na9TWiN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

