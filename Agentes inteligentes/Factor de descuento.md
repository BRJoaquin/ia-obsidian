El factor de descuento es un parámetro que se utiliza para **determinar el peso relativo de las recompensas futuras en relación con las recompensas inmediatas**. También se conoce como tasa de descuento o factor de descuento temporal.

El factor de descuento se representa generalmente con el símbolo $\gamma$ (gamma) y toma valores entre 0 y 1, inclusive. Un valor de $\gamma$ igual a 0 significa que el agente solo se preocupa por las recompensas inmediatas y no tiene en cuenta las futuras. Por otro lado, un valor de $\gamma$ igual a 1 indica que el agente tiene en cuenta todas las recompensas futuras sin importar cuán lejanas estén en el tiempo.

Cuando se utiliza el factor de descuento en la función de valor acción ($Q$-valor), que representa la utilidad esperada de tomar una determinada acción en un estado dado, se consideran tanto las recompensas inmediatas como las futuras. La función de valor acción se define recursivamente utilizando el factor de descuento de la siguiente manera:

$$
Q(s, a) = r + \gamma \cdot \max(Q(s', a'))
$$

Donde:
- $Q(s, a)$ es el $Q$-valor para el estado $s$ y la acción $a$.
- $r$ es la recompensa inmediata después de tomar la acción $a$ en el estado $s$.
- $\gamma$ es el factor de descuento.
- $s'$ es el estado resultante después de tomar la acción $a$ en el estado $s$.
- $\max(Q(s', a'))$ es el $Q$-valor máximo posible para todas las acciones $a'$ en el estado $s'$.

El factor de descuento $\gamma$ permite al agente considerar las recompensas futuras al tomar decisiones, ya que reduce el impacto de las recompensas futuras en función de su distancia temporal. Esto es útil para problemas en los que las recompensas pueden estar más distantes en el tiempo y es necesario equilibrar la toma de decisiones a corto y largo plazo.
