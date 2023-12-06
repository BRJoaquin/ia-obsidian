MaxN es un algoritmo utilizado en [[Teoría de Juegos|teoría de juegos]], especialmente diseñado para juegos de múltiples jugadores. A diferencia de Minimax, que está enfocado en juegos de dos jugadores con objetivos directamente opuestos ([[Juego de suma cero|suma cero]]), MaxN se utiliza en situaciones donde hay más de dos jugadores y cada uno puede tener sus propios objetivos.

![[Pasted image 20231206074326.png]]

1. **Utilidad(s)**: Es una función que asigna un vector de valores a cada estado final del juego, `s`, donde `n` es el número de jugadores. Cada componente del vector corresponde a la utilidad para un jugador específico.

2. **$V_{max^n}(s)$**: Es el valor del juego para un estado `s` bajo la suposición de que todos los jugadores juegan óptimamente. El valor es definido recursivamente como:
   - Si `s` es un estado final (`EsFinal(s)`), el valor de `s` es simplemente `Utilidad(s)`.
   - Si no es un estado final, y es el turno del jugador `p` (`Jugador(s) = p`), entonces el valor es el máximo sobre todas las acciones posibles `a` que el jugador `p` puede tomar ($a \in Acc(s)$). Aquí, `Acc(s)` representa el conjunto de acciones legales desde el estado `s`.
   - El valor máximo se calcula comparando los vectores de utilidad `u` y `v`, donde `u` es preferido sobre `v` si y solo si la utilidad de `p` en `u` es mayor o igual que en `v` (denotado por $u \geq_p v$).

3. **Árbol de Juego**: La estructura del árbol muestra cómo se despliegan los movimientos a través del juego. Cada nodo representa un estado del juego y cada arista representa una acción que lleva a un estado sucesor.
   - **Nodos etiquetados con A, B, C**: Representan los turnos de los jugadores.
   - **Vectores en los nodos**: Representan la utilidad para cada jugador en ese nodo. Por ejemplo, (1,2,6) significa que el jugador A tiene una utilidad de 1, el jugador B una utilidad de 2, y el jugador C una utilidad de 6.
   - **Nodos cuadrados vs. nodos circulares**: Los nodos cuadrados podrían representar decisiones de jugadores, mientras que los nodos circulares podrían representar eventos aleatorios o decisiones de otros jugadores.

El proceso de toma de decisiones en MaxN implica mirar hacia adelante en el árbol y, en cada paso, seleccionar la acción que maximiza la utilidad del jugador en turno, considerando que los otros jugadores también están maximizando sus propias utilidades. Este algoritmo es particularmente útil para juegos de suma no cero con más de dos jugadores, donde cada jugador tiene diferentes `payoffs` y puede ganar independientemente de los otros.

![[Pasted image 20231206075151.png]]

1. Se asume que el juego tiene una suma constante de 9 para todos los jugadores en conjunto. Después de evaluar el subárbol izquierdo, se encuentra que el valor para el jugador 1 es al menos 3 (≥3), y para los jugadores 2 y 3 es menos de 6 (≤ C - 3 = 9 - 3 = 6) en el nodo "b".
    
2. Luego, se evalúa el nodo "g", y se obtiene que el valor para el jugador 2 es al menos 7 (≥7), y para los jugadores 1 y 3 es menos de 2 (≤ C - 7 = 9 - 7 = 2) en el nodo "f". Como el valor para el jugador 1 es menor a 3, que es el valor mínimo ya encontrado en el nodo "b", se puede podar el resto de este subárbol porque no se encontrará un valor mejor para el jugador 1.
    
3. Finalmente, se evalúa el nodo "h", y se encuentra que el valor para el jugador 2 es al menos 6 (≥6), y para los jugadores 1 y 3 es menos de 3 (≤ C - 6 = 9 - 6 = 3). Dado que el valor para el jugador 1 es igual al mínimo encontrado en el nodo "b" y el valor para el jugador 2 es menor que el mínimo encontrado en el nodo "f", se puede podar el resto de este subárbol.

La poda superficial funciona en este contexto porque el juego tiene una suma constante, y se puede inferir que si un jugador tiene asegurado un cierto valor, los otros jugadores no pueden superar ciertos valores. Por ejemplo, si un jugador tiene asegurado al menos 3 puntos en una configuración de juego donde la suma total de puntos es 9, entonces se sabe que los otros dos jugadores juntos no pueden superar los 6 puntos restantes.

La imagen muestra un árbol de juego con poda superficial utilizando el algoritmo MaxN. Aquí está la explicación detallada:

1. La suma constante del juego es 9. Después de evaluar el subárbol izquierdo, el valor mínimo asegurado para el jugador 1 es 3 (≥3) y para los jugadores 2 y 3 es menos de 6 (≤ 6), en el nodo "b".

2. Evaluando el nodo "g", se encuentra que el valor mínimo para el jugador 2 es 7 (≥7), y para los jugadores 1 y 3 es menos de 2 (≤ 2) en el nodo "f". Se realiza una poda ya que no se encontrará un valor mejor para el jugador 1 aquí.

3. En el nodo "h", el valor para el jugador 2 es al menos 6 (≥6), y para los jugadores 1 y 3 es menos de 3 (≤ 3). Se poda el resto ya que el valor para el jugador 1 no mejora al mínimo encontrado en "b".

Esta técnica de poda ayuda a mejorar la eficiencia del algoritmo al reducir el número de nodos que necesitan ser explorados.

![[Pasted image 20231206075436.png]]

La imagen muestra un pseudocódigo para la función `Shallow`, que parece ser una implementación de un algoritmo de poda en un árbol de juego para el algoritmo MaxN. Aquí está la traducción y explicación del pseudocódigo:

```plaintext
def Shallow(s, p, Bound):
    # Bound: cota superior en el valor para p
    # Sum: cota superior en la suma de los valores
    
    # Si s es un estado final del juego, devuelve su utilidad
    if EsFinal(s) then
        return Utilidad(s)
    
    # Evalúa el primer hijo del estado actual s para el jugador p
    Best ← Shallow(p.child[0], p.next, Sum)
    
    # Itera a través del resto de los hijos
    for c in p.child[1...]:
        # Si el mejor valor actual es mayor o igual a la cota, poda el árbol
        if Best[p] >= Bound then
            return Best # Poda
        
        # Calcula el valor para el hijo actual
        Current ← Shallow(c, p.next, Sum - Best[p])
        
        # Si el valor actual es mejor que el mejor valor conocido, actualiza Best
        if Current[p] > Best[p] then
            Best ← Current # Actualizar cota
    
    # Devuelve el mejor valor encontrado
    return Best
```

Este pseudocódigo utiliza la técnica de poda superficial en árboles de juego donde `s` es el estado actual del juego, `p` es el jugador actual, y `Bound` es la cota superior para el valor del jugador `p`. La función `Shallow` evalúa los nodos del árbol de juego de manera recursiva para encontrar el mejor valor para el jugador `p`, realizando podas en el árbol cuando se encuentra que un nodo no puede producir un valor mejor que el mejor valor encontrado hasta el momento (`Bound`). La variable `Sum` representa la cota superior de la suma de los valores de los jugadores, que no está directamente presente en el pseudocódigo, pero se infiere por el comentario y es utilizada en la llamada recursiva para ajustar la cota superior durante la exploración del árbol.

![[Pasted image 20231206075610.png]]


### Características de MaxN:

1. **Generalización de Minimax**: MaxN es una generalización del algoritmo [[Minimax|Minimax]] para n jugadores. Mientras que Minimax considera el mejor movimiento para un jugador y el peor para el adversario, MaxN busca optimizar los movimientos considerando los intereses de todos los jugadores.
    
2. **Función de Utilidad para Cada Jugador**: En MaxN, cada jugador tiene su propia función de utilidad, que no necesariamente es la negativa de los demás jugadores. Esto permite una mayor flexibilidad para modelar juegos donde los objetivos de los jugadores no son completamente adversarios.
    
3. **Árbol de Juego**: Como en Minimax, MaxN explora un árbol de juego. Sin embargo, en lugar de alternar entre maximizar y minimizar, cada nivel del árbol corresponde a un jugador diferente, y el objetivo en cada nivel es maximizar la utilidad de ese jugador específico.
    
4. **Estrategias Óptimas para Todos los Jugadores**: MaxN trata de encontrar la estrategia óptima para todos los jugadores, no solo para uno. En teoría, esto conduce a una solución más equilibrada y representativa de situaciones reales en juegos de múltiples jugadores.

### Consideraciones:

- **Complejidad**: Al aumentar el número de jugadores, la complejidad del [[Árbol de Juego|árbol de juego]] crece exponencialmente, lo que puede hacer que MaxN sea computacionalmente intensivo.
- **Equilibrio entre Jugadores**: En juegos donde los jugadores tienen objetivos muy diferentes, encontrar una solución que satisfaga a todos puede ser un desafío.


