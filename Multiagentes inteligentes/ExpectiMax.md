Expectimax es un algoritmo utilizado en la toma de decisiones bajo incertidumbre y en la teoría de juegos, especialmente en el contexto de la inteligencia artificial para juegos con elementos de azar. Es una variante del algoritmo Minimax que se utiliza en juegos de información perfecta y sin azar, como el ajedrez. Expectimax, por su parte, es más adecuado para situaciones donde los resultados de ciertas acciones son inciertos y pueden tener diferentes probabilidades de ocurrencia.

**Cómo Funciona Expectimax:**

1. **Árbol de Decisión**: El algoritmo se basa en un árbol de decisión que alterna entre niveles de decisión y niveles de azar (o suerte). Los nodos de decisión representan los lugares donde un jugador toma una decisión, y los nodos de azar representan los resultados aleatorios de estas decisiones.
    
2. **Nodos de Decisión**: En los niveles de decisión, el algoritmo busca la acción que maximiza la utilidad esperada, similar al "max" en Minimax.
    
3. **Nodos de Azar**: En los niveles de azar, en lugar de tomar el mínimo como en Minimax, el algoritmo calcula un valor esperado basado en la probabilidad y la utilidad de cada posible resultado.
    
4. **Cálculo de Utilidad**: La utilidad de un nodo de decisión se calcula como el máximo de las utilidades esperadas de sus hijos, mientras que la utilidad de un nodo de azar es el promedio ponderado, tomando en cuenta las probabilidades de cada resultado.
    

**Importancia de Expectimax:**

- **Toma de Decisiones con Incertidumbre**: Expectimax es particularmente útil para juegos y problemas de decisión donde hay elementos de suerte o incertidumbre, como en el lanzamiento de dados o en la selección de cartas de una baraja.
    
- **Optimización de Estrategias**: Permite a los jugadores o agentes de inteligencia artificial optimizar sus estrategias cuando no todos los resultados son predecibles.
    
- **Mejor que Minimax en Juegos con Azar**: En juegos con elementos aleatorios, [[Minimax]] puede ser demasiado pesimista porque asume que el oponente siempre jugará la estrategia óptima. Expectimax ofrece una evaluación más realista al considerar la aleatoriedad.
    

**Limitaciones de Expectimax:**

- **Complejidad Computacional**: Al igual que Minimax, Expectimax puede sufrir de un crecimiento exponencial en la cantidad de cálculos a medida que aumenta la profundidad del árbol de decisión.
    
- **Necesidad de Evaluación Heurística**: Para árboles muy grandes, a menudo es necesario aplicar funciones heurísticas para evaluar los nodos, ya que no es factible calcular la utilidad exacta en cada nodo debido a la complejidad del árbol. ver [[Funciones de evaluación]]
    
- **Dependencia en Probabilidades**: La efectividad del algoritmo depende en gran medida de cuán precisas sean las probabilidades asignadas a los resultados en los nodos de azar.


Expectimax es una herramienta poderosa en la teoría de juegos y la inteligencia artificial, proporcionando un marco para la toma de decisiones estratégicas en entornos inciertos y ayudando a los agentes a navegar complejas situaciones de decisión.


# Ejemplo

![[Pasted image 20231201110013.png]]

![[Pasted image 20231201110022.png]]
