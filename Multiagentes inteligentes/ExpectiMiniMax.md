
Expectiminimax es una variante del algoritmo Minimax que se utiliza para juegos con elementos de azar además de la toma de decisiones estratégica. A diferencia de Minimax, que se aplica en situaciones de información perfecta y deterministas, Expectiminimax maneja la incertidumbre al incorporar los nodos de azar que calculan la utilidad esperada basada en la probabilidad de los diferentes resultados.

**Principios del Expectiminimax:**

1. **Incorporación de Azar**: Expectiminimax extiende Minimax al incluir nodos de azar (o nodos de expectativa) que representan eventos aleatorios cuyos resultados afectan la utilidad de las decisiones.
    
2. **Nodos de Expectativa**: Estos nodos calculan un valor esperado de las utilidades de los nodos hijos, ponderados por la probabilidad de cada resultado aleatorio.
    
3. **Nodos Min y Max**: Al igual que Minimax, Expectiminimax alterna entre nodos min y max. Los nodos max buscan maximizar la utilidad para el jugador, mientras que los nodos min representan el mejor juego del oponente.
    
4. **Calculo de la Utilidad**: En Expectiminimax, la utilidad de los nodos se calcula de manera similar a Minimax, pero con la adición de tomar un promedio ponderado en los nodos de expectativa.
    

![[Pasted image 20231201113526.png]]

**Ventajas del Expectiminimax:**

- **Manejo de Incertidumbre**: Es más realista para juegos que incluyen elementos de azar, como juegos de cartas o cualquier escenario donde las decisiones tienen resultados inciertos.
    
- **Estrategias Óptimas para Juegos Complejos**: Ofrece un método para determinar estrategias óptimas en juegos más complejos que incluyen tanto la estrategia como el azar.
    
- **Extensible**: Puede ser extendido y adaptado a una amplia variedad de juegos y situaciones de toma de decisiones.
    

**Desventajas del Expectiminimax:**

- **Mayor Complejidad Computacional**: La adición de nodos de azar aumenta la complejidad del árbol de decisión y, por ende, los recursos computacionales necesarios para evaluarlo.
    
- **Dependencia de Probabilidades**: El algoritmo depende de probabilidades conocidas o estimadas para los eventos aleatorios, lo que puede ser una limitación si dichas probabilidades no son conocidas con precisión.

```
function expectiminimax(node, depth)
    if node is a terminal node or depth = 0
        return the heuristic value of node
    if the adversary is to play at node
        // Return value of minimum-valued child node
        let α := +∞
        foreach child of node
            α := min(α, expectiminimax(child, depth-1))
    else if we are to play at node
        // Return value of maximum-valued child node
        let α := -∞
        foreach child of node
            α := max(α, expectiminimax(child, depth-1))
    else if random event at node
        // Return weighted average of all child nodes' values
        let α := 0
        foreach child of node
            α := α + (Probability[child] × expectiminimax(child, depth-1))
    return α
```


# Ejemplo

![[Pasted image 20231201113500.png]]

![[Pasted image 20231201113511.png]]
