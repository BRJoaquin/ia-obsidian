  
Los "infosets" o conjuntos de información son un concepto de la teoría de juegos que representa la información disponible para un jugador en un punto particular del juego. En [[Juegos con Información imperfecta|juegos de información imperfecta]], un jugador puede no conocer todas las acciones que han llevado al estado actual del juego debido a la ocultación de información, como las cartas ocultas en el póker.

En la teoría de juegos, un infoset o conjunto de información es un conjunto de nodos en el árbol de juegos entre los que un jugador no puede distinguir dada la información disponible. Esto es especialmente relevante en juegos de información imperfecta.

## Definición

- $H$ es el conjunto de todos los historiales posibles en un juego, y $I_p$ es el conjunto de todos los historiales en los que es el turno del jugador $p$.

$$ H = \bigcup_{p} I_p $$

- $I_p$ es el conjunto de historiales donde el jugador $p$ debe actuar.

$$ I_p = \{ h \mid Agente(h) = p \} $$

- Un infoset $I_p$ es un subconjunto de $I_p$ donde el jugador $p$ tiene exactamente la misma información. En otras palabras, el jugador no puede distinguir entre los historiales dentro del mismo infoset.

- Para cualquier dos historiales $h, h'$ en el mismo infoset $I_p$, el conjunto de acciones posibles es el mismo.

$$ \forall h, h' \in I_p, A(h) = A(h') $$

- $A(I_p)$ es el conjunto de acciones posibles que el jugador puede tomar en el infoset $I_p$.

## Importancia

Los infosets son cruciales para diseñar estrategias en juegos de información imperfecta, ya que el jugador debe tomar decisiones sin conocer el estado completo del juego. Las estrategias deben, por lo tanto, ser formuladas considerando todos los posibles estados del juego que podrían corresponder al mismo conjunto de información.

## Ejemplo

En el póker, el infoset incluiría las cartas propias del jugador y las acciones de los oponentes que ha observado, pero no las cartas ocultas de los oponentes. Cada posible combinación de cartas ocultas de los oponentes que resulta en la misma información observada pertenece al mismo infoset.

Los infosets permiten a los jugadores planificar estrategias en juegos complejos donde la información completa no está disponible, lo que es esencial para el desarrollo de algoritmos de IA en juegos como el póker.
