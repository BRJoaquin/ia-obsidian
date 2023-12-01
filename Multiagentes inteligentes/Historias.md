Una **historia** en la teoría de juegos es una secuencia de acciones que se han tomado en el transcurso de un juego. Representan el camino que ha seguido el juego desde el inicio hasta un punto específico.

## Definición

- Una historia $h$ es una secuencia de acciones.
  
- $H$ es el conjunto de todas las historias posibles en el juego.

- $h \subset h'$ si $h$ es un prefijo estricto de $h'$, lo que significa que $h$ es una secuencia de acciones que conduce a $h'$, pero no incluye la última acción de $h'$.

- $h_i$ es el i-ésimo elemento (acción) en la secuencia de la historia $h$.

- $h_{<i}$ es el prefijo de $h$ de longitud $i - 1$, es decir, la secuencia de acciones hasta pero no incluyendo el i-ésimo paso.

- $Z \subset H$ es el conjunto de historias terminales, aquellas que representan un juego completo desde el inicio hasta el final.

- $A(h) = \{ a \mid ha \in H \}$ es el conjunto de acciones posibles que pueden seguir a la historia $h$.

## Importancia

Las historias son cruciales en la teoría de juegos porque permiten a los jugadores y a los algoritmos de IA rastrear el progreso del juego y tomar decisiones informadas basadas en lo que ha ocurrido previamente. Son especialmente importantes en juegos de información imperfecta, donde las historias pueden influir en las creencias y expectativas de los jugadores sobre las acciones futuras de sus oponentes.
