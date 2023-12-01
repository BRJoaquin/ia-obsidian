  
Los "infosets" o conjuntos de información son un concepto de la teoría de juegos que representa la información disponible para un jugador en un punto particular del juego. En [[Juegos con Información imperfecta|juegos de información imperfecta]], un jugador puede no conocer todas las acciones que han llevado al estado actual del juego debido a la ocultación de información, como las cartas ocultas en el póker.

En la teoría de juegos, un infoset o conjunto de información es un conjunto de nodos en el árbol de juegos entre los que un jugador no puede distinguir dada la información disponible. Esto es especialmente relevante en juegos de información imperfecta.

## Definición

![[Pasted image 20231201171851.png]]

## Importancia

Los infosets son cruciales para diseñar estrategias en juegos de información imperfecta, ya que el jugador debe tomar decisiones sin conocer el estado completo del juego. Las estrategias deben, por lo tanto, ser formuladas considerando todos los posibles estados del juego que podrían corresponder al mismo conjunto de información.

## Ejemplo

En el póker, el infoset incluiría las cartas propias del jugador y las acciones de los oponentes que ha observado, pero no las cartas ocultas de los oponentes. Cada posible combinación de cartas ocultas de los oponentes que resulta en la misma información observada pertenece al mismo infoset.

Los infosets permiten a los jugadores planificar estrategias en juegos complejos donde la información completa no está disponible, lo que es esencial para el desarrollo de algoritmos de IA en juegos como el póker.
