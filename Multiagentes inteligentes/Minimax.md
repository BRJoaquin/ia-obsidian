El algoritmo Minimax es una técnica fundamental en la [[Teoría de Juegos|teoría de juegos]] y la inteligencia artificial para encontrar la mejor estrategia en [[Juego de suma cero|juegos de suma cero]] y de [[Juegos con Información perfecta|información perfecta]], especialmente juegos de dos jugadores como el ajedrez o las damas. La idea central del Minimax es **minimizar la pérdida máxima posible (de ahí el nombre) asumiendo que el oponente está jugando su mejor estrategia posible**.

**Principios del Minimax:**

1. **Optimización de Peor Caso**: Los jugadores asumen que el oponente es óptimo y juega para maximizar su utilidad. Por lo tanto, cada jugador minimiza la utilidad máxima que el oponente podría alcanzar.
    
2. **Árboles de Juego**: Minimax utiliza árboles de juego para representar todas las posibles secuencias de movimientos y contra-movimientos en un juego. Los nodos representan las posiciones del juego o estados, y las aristas representan los movimientos posibles.
    
3. **Nodos Min y Max**: En el árbol de juego, los nodos se alternan entre niveles "min" y "max". Los nodos "max" representan las decisiones del jugador que está utilizando Minimax, buscando maximizar su utilidad. Los nodos "min" representan las decisiones del oponente, que intentará minimizar la utilidad del jugador Minimax.
    
4. **Inducción hacia Atrás**: Minimax trabaja desde los nodos terminales del árbol hacia atrás (backward induction), calculando la utilidad de los nodos padre basándose en los valores óptimos de sus nodos hijos.
    
5. **Podado Alfa-Beta**: Para mejorar la eficiencia del algoritmo Minimax y evitar la evaluación de movimientos irrelevantes, se puede utilizar la técnica de podado alfa-beta, que corta ramas del árbol que no influirán en la decisión final. ver [[Poda alpha-beta]]
    
![[Pasted image 20231201113204.png]]


**Ventajas del Minimax:**

- **Estrategia Óptima**: Proporciona un método claro para calcular la estrategia óptima en juegos de dos jugadores con información perfecta.
    
- **Predecible**: Los resultados son predecibles si ambos jugadores juegan racionalmente.
    
- **Completo**: Explora completamente el espacio de búsqueda, lo que garantiza que no se pasen por alto las mejores estrategias.
    

**Desventajas del Minimax:**

- **Complejidad Computacional**: Incluso con [[Poda alpha-beta|podado alfa-beta]], el número de nodos a evaluar puede ser exponencial con respecto a la profundidad del árbol.
    
- **No Apto para Incertidumbre**: Minimax no maneja bien los elementos de azar o la información imperfecta, ya que asume que todos los resultados de las decisiones son conocidos y predecibles.
    
- **Recursos Intensivos**: Para juegos con muchos movimientos posibles, Minimax puede requerir una cantidad de recursos computacionales que lo hacen impracticable.
    

**Aplicaciones de Minimax:**

- **Juegos de Tablero**: Utilizado en programas de computadora que juegan juegos de tablero como el ajedrez, las damas y el go.
    
- **Economía y Negocios**: Puede ayudar a modelar y resolver problemas de decisión estratégica donde las partes tienen intereses opuestos.
    
- **Robótica y Control**: Minimax puede ser utilizado para la planificación de movimientos en entornos donde se conoce completamente el estado del sistema y las acciones de los adversarios o el entorno.

![[Pasted image 20231201113234.png]]
![[Pasted image 20231201113250.png]]
![[Pasted image 20231201113404.png]]

![[Pasted image 20231201113741.png]]

# Ejemplo

![[Pasted image 20231201113144.png]]


# Links

https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/?ref=header_search

